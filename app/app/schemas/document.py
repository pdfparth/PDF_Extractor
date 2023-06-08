from typing import Optional

from pydantic import BaseModel, AnyUrl


# class DocumentCreate(BaseModel):
#     assistant_token: str
#     link: AnyUrl

class DocumentResponse(BaseModel):
    success: bool
    message: str
    data: str
