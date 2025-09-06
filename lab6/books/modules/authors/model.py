from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ...database import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)

    author_books = relationship("AuthorBook", back_populates="author")
    books = relationship("Book", secondary="author_book", back_populates="authors")
