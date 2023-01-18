"""
Created on 2022-12-08 15:19
@author: johannes
"""
from fastapi import APIRouter
from app.feat.endpoints import router

api_router = APIRouter(prefix="/api")
api_router.include_router(router)
