from sqlalchemy.orm import Session, joinedload
from . import model, schema

def get_books(db: Session):
    return db.query(model.Book).options(joinedload(model.Book.authors)).all()

def create_book(db: Session, book: schema.BookCreate):
    db_book = model.Book(title=book.title, year_of_publication=book.year_of_publication, price=book.price, publisher_id=book.publisher_id, bookstore_id=book.bookstore_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_book(db: Session, book_id: int):
    return db.query(model.Book).filter(model.Book.id == book_id).first()

def update_book(db: Session, book_id: int, book: schema.BookCreate):
    db_book = db.query(model.Book).filter(model.Book.id == book_id).first()
    if not db_book:
        return None
    db_book.title = book.title
    db_book.year_of_publication=book.year_of_publication
    db_book.price=book.price
    db_book.publisher_id=book.publisher_id
    db_book.bookstore_id=book.bookstore_id
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = db.query(model.Book).filter(model.Book.id == book_id).first()
    if not db_book:
        return False
    db.delete(db_book)
    db.commit()
    return True
