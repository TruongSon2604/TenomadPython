from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title:str
    author:str
    description: str = ""
    image:str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True

class BookUpdate(BookBase):
    title: Optional[str] = None
    author: Optional[str] = None
    price: Optional[float] = None
    image:Optional[str] = None

    class Config:
        from_attributes = True