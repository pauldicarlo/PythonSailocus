'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

password_hasher = PasswordHasher(
    # TODO: Fine tun parameters
)

def hash_password(plain_password: str) -> str:
    return password_hasher.hash(plain_password)

def verify_password(password_hash: str, password: str) -> bool:
    try:
        password_hasher.verify(password_hash, password)

        '''
        From needs_check_rehash doc:
        Check whether hash was created using the instance's parameters.
        Whenever your Argon2 parameters -- or argon2-cffi's defaults! -- change, 
        you should rehash your passwords at the next opportunity. The common 
        approach is to do that whenever a user logs in, since that should be the 
        only time when you have access to the cleartext password.  Therefore 
        it's best practice to check -- and if necessary rehash -- passwords after 
        each successful authentication.
        '''
        if password_hasher.check_needs_rehash(password_hash):
            # Re-hash with current parameters and update DB
            # TODO - need to rehash and store in db
            print("TODO - need to rehash a password") 
            return True  
        return True
    except VerifyMismatchError:
        return False
    except Exception:
        return False