from sqlalchemy import Boolean, Column, String, Integer
from .db import Base

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    link = Column(String)
    size = Column(String)
    downloaded = Column(Boolean)