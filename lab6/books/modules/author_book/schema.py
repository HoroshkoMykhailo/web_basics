from pydantic import BaseModel

class AuthorBookBase(BaseModel):
    author_id: int
    book_id: int

class AuthorBookCreate(AuthorBookBase):
    pass

class AuthorBook(AuthorBookBase):
    id: int

    class Config:
        orm_mode = True
