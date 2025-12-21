'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''

from datetime import datetime, timedelta, timezone
import jwt
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic import BaseModel
from typing import Annotated
from jwt.exceptions import InvalidTokenError

router = APIRouter()

# TODO: handle and generate secret key a lot better than this...
SECRET_KEY = 'some-secret-value-mairze-dotes-and-doze-dotes-and-litle-daizey-diveys'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10

# ----------------------- Password hashing -----------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ----------------------- OAuth2 scheme -----------------------
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

##############################################################
# WHAT FOLLOWS BELOW FOR THE TIME BEING IS ROUGH CODE TO GET
# LOGIN & GRANTING OF TOKEN AND THEN USE WITH REQUESTS

class User(BaseModel):
     username: str
     disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

# ----------------------- Fake DB (replace with real DB) -----------------------
fake_users_db = {
    "freddiano": {
        "username": "freddiano",
        #"hashed_password": pwd_context.hash("secret"),  # In real app: hash on registration
        "hashed_password": "hashedvalue",
        "disabled": False,
    },
    # Add more users...
}



def authenticate_user():
    return  User(username="freddiano")

@router.post("/", response_model=Token)
async def login_and_get_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):

    user = authenticate_user()
    if not user:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Bad username and/or password",
                headers={"WWW-Authenticate": "Bearer"})

    access_token = create_access_token(data={"sub":user.username})
    return {"access_token": access_token, "token_type": "bearer"}
    
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    if token_data.username is None:
        print("TODO: need to log properly")
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user



async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Another protected endpoint
@router.get("/protected")
async def protected_route(current_user: Annotated[User, Depends(dependency=get_current_active_user)]):
#async def protected_route():
    pass # TODO do something useful