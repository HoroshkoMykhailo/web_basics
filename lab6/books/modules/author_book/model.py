from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ...database import Base

class AuthorBook(Base):
    __tablename__ = "author_book"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    book_id = Column(Integer, ForeignKey("books.id"))

    author = relationship("Author", back_populates="author_books")
    book = relationship("Book", back_populates="book_authors")
