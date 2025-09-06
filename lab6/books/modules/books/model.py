from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from ...database import Base
from ..author_book.model import AuthorBook

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year_of_publication = Column(Integer)
    price = Column(Integer)

    publisher_id = Column(Integer, ForeignKey("publishers.id"))
    bookstore_id = Column(Integer, ForeignKey("bookstores.id"))

    publisher = relationship("Publisher", back_populates="books")
    bookstore = relationship("Bookstore", back_populates="books")
    book_authors = relationship("AuthorBook", back_populates="book")
    authors = relationship("Author", secondary="author_book", back_populates="books")
