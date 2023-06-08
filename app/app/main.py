import os
import sys

sys.path.append('../')
import logging
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings
from dotenv import load_dotenv

load_dotenv(verbose=True)
app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    gunicorn_logger = logging.getLogger(os.getenv("logger_name"))
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
#     app.run()
