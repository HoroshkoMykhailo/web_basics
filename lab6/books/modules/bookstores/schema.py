from typing import List
from pydantic import BaseModel
from ..books.schema_complex import BookComplex

class BookstoreBase(BaseModel):
    name: str
    location: str

class BookstoreCreate(BookstoreBase):
    pass

class Bookstore(BookstoreBase):
    id: int
    books: List[BookComplex] = [] 

    class Config:
        orm_mode = True
