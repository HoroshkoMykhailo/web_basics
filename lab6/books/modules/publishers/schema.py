from pydantic import BaseModel
from typing import List
from ..books.schema_complex import BookComplex

class PublisherBase(BaseModel):
    name: str
    address: str

class PublisherCreate(PublisherBase):
    pass

class Publisher(PublisherBase):
    id: int
    books: List[BookComplex] = []

    class Config:
        orm_mode = True
