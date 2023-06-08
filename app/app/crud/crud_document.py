"""

"""
# Built-in libraries
import shutil

# third party libraries
import PyPDF2
import tempfile
from sqlalchemy.orm import Session

# custom libraries
from app.models.document_metadata import Document


class CRUDDocument:
    def extract_text_from_pdf(self, file):
        text = ""
        temp_file = tempfile.NamedTemporaryFile()
        
        with open(temp_file.name, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)
            
        with open(temp_file.name, "rb") as file:
            reader = PyPDF2.PdfFileReader(file,strict=False)
            num_pages = reader.numPages        
            for page_num in range(num_pages):
                page = reader.getPage(page_num)
                text += page.extractText()
        return text


    def create_file_text(self, db: Session,file) -> dict:        
        if not file.filename.endswith(".pdf") :
            return {'success': False, 'msg': 'Something went wrong','data': ""}
            
        else:
            text = self.extract_text_from_pdf(file)
            if not text:
                return {'success': False, 'msg': 'you entered wrong pdf','data': ""}
            else:                        
                document_id = Document(
                    **{'image_name': file.filename, 'image_text': text})
                db.add(document_id)
                db.commit()
                db.refresh(document_id)

                return {'success': True, 'msg': 'text Created successfully','data':text}

document = CRUDDocument()
