from sqlalchemy.orm import Session
from . import model, schema

def get_publishers(db: Session):
    return db.query(model.Publisher).all()

def create_publisher(db: Session, publisher: schema.PublisherCreate):
    db_publisher = model.Publisher(name=publisher.name, address=publisher.address)
    db.add(db_publisher)
    db.commit()
    db.refresh(db_publisher)
    return db_publisher

def get_publisher(db: Session, publisher_id: int):
    return db.query(model.Publisher).filter(model.Publisher.id == publisher_id).first()

def update_publisher(db: Session, publisher_id: int, publisher: schema.PublisherCreate):
    db_publisher = db.query(model.Publisher).filter(model.Publisher.id == publisher_id).first()
    if not db_publisher:
        return None
    db_publisher.name = publisher.name
    db_publisher.address = publisher.address
    db.commit()
    db.refresh(db_publisher)
    return db_publisher

def delete_publisher(db: Session, publisher_id: int):
    db_publisher = db.query(model.Publisher).filter(model.Publisher.id == publisher_id).first()
    if not db_publisher:
        return False
    db.delete(db_publisher)
    db.commit()
    return True
