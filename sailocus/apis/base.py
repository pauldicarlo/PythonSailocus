'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''

from .v1 import route_coe
from .v1 import route_sailocus
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(route_coe.router, prefix="/sailocus/api/v1/coe", tags=["coe"])


# for webapp
api_router.include_router(route_sailocus.router, prefix="/sailocus/simple", tags=["sailocus"])