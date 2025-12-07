'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''

from .connection import Session
from sailocus.sail import sail

from typing import Union



class User:
    def __init__(self, user_id: str):
        self.user_id = user_id

def get_sail(session: Session, sail_id: str) -> Union[sail.Sail, None]:
    pass

def create_sail(session: Session, sail: sail.Sail, user: User):
    pass

def update_sail(session: Session, sail: sail.Sail, user: User):
    pass

def delete_sail(session: Session, sail: sail.Sail, user: User):
    pass