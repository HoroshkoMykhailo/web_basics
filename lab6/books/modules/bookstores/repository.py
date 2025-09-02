from sqlalchemy.orm import Session
from . import model, schema

def get_bookstores(db: Session):
    return db.query(model.Bookstore).all()

def create_bookstore(db: Session, bookstore: schema.BookstoreCreate):
    db_bookstore = model.Bookstore(name=bookstore.name, location=bookstore.location)
    db.add(db_bookstore)
    db.commit()
    db.refresh(db_bookstore)
    return db_bookstore

def get_bookstore(db: Session, bookstore_id: int):
    return db.query(model.Bookstore).filter(model.Bookstore.id == bookstore_id).first()

def update_bookstore(db: Session, bookstore_id: int, bookstore: schema.BookstoreCreate):
    db_bookstore = db.query(model.Bookstore).filter(model.Bookstore.id == bookstore_id).first()
    if not db_bookstore:
        return None
    db_bookstore.name = bookstore.name
    db_bookstore.location = bookstore.location
    db.commit()
    db.refresh(db_bookstore)
    return db_bookstore

def delete_bookstore(db: Session, bookstore_id: int):
    db_bookstore = db.query(model.Bookstore).filter(model.Bookstore.id == bookstore_id).first()
    if not db_bookstore:
        return False
    db.delete(db_bookstore)
    db.commit()
    return True
