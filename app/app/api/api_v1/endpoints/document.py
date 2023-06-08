from typing import Any

from fastapi import APIRouter, Depends, Form, File, UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app import crud
from app import schemas
from app.api import deps


router = APIRouter()


@router.post("/create/text/", response_model=schemas.DocumentResponse)
def create_file(*, db: Session = Depends(deps.get_db), file: UploadFile = File(...)) -> Any:
    try:
        response = crud.document.create_file_text(db,file)
        return JSONResponse(status_code=200 if response.get('success') else 400,
                            content={'success': response.get('success'), "message": response.get('msg'), "data": response.get('data')})
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JSONResponse(status_code=400, content={'success': False, "message": str(e)})


