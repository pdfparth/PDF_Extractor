from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core import security
from app.core.config import settings
from app.db.session import SessionLocal

# reusable_oauth2 = OAuth2PasswordBearer(
#     tokenUrl=f"{settings.API_V1_STR}/login/"
# )


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# def get_current_company(db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)) -> models.Companies:
#     try:
#         payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[security.ALGORITHM])
#         token_data = schemas.TokenPayload(**payload)
#     except (jwt.JWTError, ValidationError):
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials")
#     company = crud.companies.check_valid_company(db, access_token=token_data.sub)
#     if not company:
#         raise HTTPException(status_code=404, detail="Company not found")
#     return company


# def get_current_active_company(current_company: models.Companies = Depends(get_current_company)) -> models.Companies:
#     if not crud.companies.is_active(current_company):
#         raise HTTPException(status_code=400, detail="Inactive Company")
#     return current_company
