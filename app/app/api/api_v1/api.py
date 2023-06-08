from fastapi import APIRouter

from app.api.api_v1.endpoints import document
api_router = APIRouter()
api_router.include_router(document.router, prefix="/document", tags=["document"])
