'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''

from .connection import Session

from typing import Union

class User:
    def __init__(self, user_id: str):
        self.user_id = user_id

def get_user(session: Session) -> Union[User, None]:
    pass

def create_user(session: Session, user: User):
    pass

def update_user(session: Session, user: User):
    pass

def delete_user(session: Session, user: User):
    pass
