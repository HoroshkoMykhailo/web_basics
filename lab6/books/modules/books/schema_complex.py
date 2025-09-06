from typing import List
from .schema import Book
from ..authors.schema import Author


class BookComplex(Book):
    authors: List[Author] = []

    class Config:
        orm_mode = True
