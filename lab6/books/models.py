from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Table
from sqlalchemy.orm import relationship
from .database import Base

book_authors = Table(
    "book_authors",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True),
    Column("author_id", Integer, ForeignKey("authors.id"), primary_key=True)
)

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    address = Column(String)

    books = relationship("Book", secondary=book_authors, back_populates="authors")


class Publisher(Base):
    __tablename__ = "publishers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String)

    books = relationship("Book", back_populates="publisher")


class BookStore(Base):
    __tablename__ = "bookstores"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String)

    books = relationship("Book", back_populates="store")


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    publish_year = Column(Integer)
    price = Column(DECIMAL(10, 2))

    publisher_id = Column(Integer, ForeignKey("publishers.id"))
    store_id = Column(Integer, ForeignKey("bookstores.id"))

    publisher = relationship("Publisher", back_populates="books")
    store = relationship("BookStore", back_populates="books")
    authors = relationship("Author", secondary=book_authors, back_populates="books")