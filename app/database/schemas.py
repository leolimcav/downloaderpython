from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    link: str
    size: str

class Item(ItemBase):
    id: int
    downloaded: int
    
    class Config:
        orm_mode: True