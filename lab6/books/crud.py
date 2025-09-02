from sqlalchemy.orm import Session
from . import models, schemas

def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(**author.model_dump()())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_authors(db: Session):
    return db.query(models.Author).all()

def create_publisher(db: Session, publisher: schemas.PublisherCreate):
    db_publisher = models.Publisher(**publisher.model_dump()())
    db.add(db_publisher)
    db.commit()
    db.refresh(db_publisher)
    return db_publisher

def get_publishers(db: Session):
    return db.query(models.Publisher).all()

def create_store(db: Session, store: schemas.BookStoreCreate):
    db_store = models.BookStore(**store.model_dump()())
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store

def get_stores(db: Session):
    return db.query(models.BookStore).all()

def create_book(db: Session, book: schemas.BookCreate):
    authors = db.query(models.Author).filter(models.Author.id.in_(book.author_ids)).all()
    publisher = db.query(models.Publisher).get(book.publisher_id)
    store = db.query(models.BookStore).get(book.store_id)

    db_book = models.Book(
        title=book.title,
        publish_year=book.publish_year,
        price=book.price,
        publisher=publisher,
        store=store,
        authors=authors
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(models.Book).all()