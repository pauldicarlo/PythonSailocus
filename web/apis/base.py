'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''

from .v1 import route_coe, route_token
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(route_coe.router, prefix="/sailocus/api/v1/coe", tags=["coe"])
api_router.include_router(route_token.router, prefix="/token", tags=["token"])

