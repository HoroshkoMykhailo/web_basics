from sqlalchemy.orm import Session
from . import model, schema

def create_author_book(db: Session, relation: schema.AuthorBookCreate):
    db_relation = model.AuthorBook(author_id=relation.author_id, book_id=relation.book_id)
    db.add(db_relation)
    db.commit()
    db.refresh(db_relation)
    return db_relation

def get_author_books(db: Session):
    return db.query(model.AuthorBook).all()

def get_author_book(db: Session, relation_id: int):
    return db.query(model.AuthorBook).filter(model.AuthorBook.id == relation_id).first()

def update_author_book(db: Session, relation_id: int, relation: schema.AuthorBookCreate):
    db_relation = db.query(model.AuthorBook).filter(model.AuthorBook.id == relation_id).first()
    if not db_relation:
        return None
    db_relation.author_id = relation.author_id
    db_relation.book_id = relation.book_id
    db.commit()
    db.refresh(db_relation)
    return db_relation

def delete_author_book(db: Session, relation_id: int):
    db_relation = db.query(model.AuthorBook).filter(model.AuthorBook.id == relation_id).first()
    if not db_relation:
        return False
    db.delete(db_relation)
    db.commit()
    return True
