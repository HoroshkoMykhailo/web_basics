from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    year_of_publication: int
    price: int
    publisher_id: int
    bookstore_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True