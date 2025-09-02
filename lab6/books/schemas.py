from pydantic import BaseModel
from typing import Optional, List

class AuthorBase(BaseModel):
    full_name: str
    address: Optional[str] = None

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    class Config:
        orm_mode = True

class PublisherBase(BaseModel):
    name: str
    address: str

class PublisherCreate(PublisherBase):
    pass

class Publisher(PublisherBase):
    id: int
    class Config:
        orm_mode = True


class BookStoreBase(BaseModel):
    name: str
    address: str

class BookStoreCreate(BookStoreBase):
    pass

class BookStore(BookStoreBase):
    id: int
    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    publish_year: int
    price: float
    publisher_id: int
    store_id: int
    author_ids: List[int]

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    class Config:
        orm_mode = True