from typing import List
from .schema import Author
from ..books.schema import Book


class AuthorWithBooks(Author):
    books: List[Book] = []

    class Config:
        orm_mode = True