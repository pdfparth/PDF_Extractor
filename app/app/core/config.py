import os
from typing import Any, Dict, List, Optional, Union

from dotenv import load_dotenv
from pydantic import (AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn,
                      validator)

load_dotenv(verbose=True)


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 1
    SERVER_NAME: str = "PDF Exctractor"
    SERVER_HOST: AnyHttpUrl = "http://localhost:8082"
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = "PDF Extractor"
    SENTRY_DSN: Optional[HttpUrl] = None

    @validator("SENTRY_DSN", pre=True)
    def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
        if not v or len(v) == 0:
            return None
        return v

    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = os.getenv(
        "SQLALCHEMY_DATABASE_URI")

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None

    @validator("EMAILS_FROM_NAME")
    def get_project_name(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if not v:
            return values["PROJECT_NAME"]
        return v

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAILS_ENABLED: bool = False

    @validator("EMAILS_ENABLED", pre=True)
    def get_emails_enabled(cls, v: bool, values: Dict[str, Any]) -> bool:
        return bool(
            values.get("SMTP_HOST")
            and values.get("SMTP_PORT")
            and values.get("EMAILS_FROM_EMAIL")
        )

    EMAIL_TEST_USER: EmailStr = "test@example.com"  # type: ignore
    FIRST_SUPERUSER: EmailStr = "aakash@teaminnovatics.com"
    FIRST_SUPERUSER_PASSWORD: str = "test@123"
    USERS_OPEN_REGISTRATION: bool = False

    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    SENDGRID_API_KEY: str = os.getenv("SENDGRID_API_KEY")
    SENDGRID_FROM_ACCOUNT: str = os.getenv("SENDGRID_FROM_ACCOUNT")
    OTP_VALIDITY_MINUTES: int = 10
    CHROMA_DB_PATH: str = os.getenv("CHROMA_DB_PATH")
    FREE_USAGE_TOKENS: int = os.getenv("FREE_USAGE_TOKENS")
    REDIS_HOST: str = os.getenv("REDIS_HOST")
    DOCUMENT_MAIN_FOLDER: str = os.getenv("DOCUMENT_MAIN_FOLDER")

    ODOO_BASE_URI: str = os.getenv("ODOO_BASE_URI")
    SCRAPPY_URL:str = os.getenv("SCRAPPY_URL")

    class Config:
        case_sensitive = True
        env_prefix = ''
        env_file = '.env'


settings = Settings()
