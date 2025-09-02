from sqlalchemy.orm import Session, joinedload
from . import model, schema

def get_authors(db: Session):
    return db.query(model.Author).options(joinedload(model.Author.books)).all()

def create_author(db: Session, author: schema.AuthorCreate):
    db_author = model.Author(name=author.name, address=author.address)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_author(db: Session, author_id: int):
    return db.query(model.Author).filter(model.Author.id == author_id).first()

def update_author(db: Session, author_id: int, author: schema.AuthorCreate):
    db_author = db.query(model.Author).filter(model.Author.id == author_id).first()
    if not db_author:
        return None
    db_author.name = author.name
    db_author.address = author.address
    db.commit()
    db.refresh(db_author)
    return db_author

def delete_author(db: Session, author_id: int):
    db_author = db.query(model.Author).filter(model.Author.id == author_id).first()
    if not db_author:
        return False
    db.delete(db_author)
    db.commit()
    return True
