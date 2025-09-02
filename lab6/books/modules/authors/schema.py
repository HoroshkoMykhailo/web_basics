from pydantic import BaseModel
from typing import List
from ..books.schema import Book

class AuthorBase(BaseModel):
    name: str
    address: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True