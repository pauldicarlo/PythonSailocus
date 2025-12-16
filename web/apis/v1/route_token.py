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

router = APIRouter()

# TODO: handle and generate secret key a lot better than this...
SECRET_KEY = 'some-secret-value-mairze-dotes-and-doze-dotes-and-litle-daizey-diveys'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10

payload = {

}


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


# TODO: Implement user database and management forms
class User(BaseModel):
     username: str

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
    
