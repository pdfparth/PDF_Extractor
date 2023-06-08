from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from app.db.base_class import Base


class Document(Base):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True, index=True)
    image_name = Column(String)
    image_text = Column(String)
