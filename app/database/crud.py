from sqlalchemy.orm import Session
from . import models

def get_item(db: Session, name: str):
    return db.query(models.Item).filter(models.Item.name == name).first()

def get_items(db: Session):
    return db.query(models.Item).all()