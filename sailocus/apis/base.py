from .v1 import route_coe
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(route_coe.router, prefix="/api/v1", tags=["coe"])