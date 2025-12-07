'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''

from fastapi import APIRouter

from . import route_sailocus

web_router = APIRouter()
# for webapp
web_router.include_router(route_sailocus.router, prefix="/sailocus/simple", tags=["sailocus"])