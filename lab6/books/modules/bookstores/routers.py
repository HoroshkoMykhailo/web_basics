from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...database import get_db
from . import repository, schema

router = APIRouter(prefix="/bookstores", tags=["bookstores"])

@router.get("/", response_model=list[schema.Bookstore])
def read_bookstores(db: Session = Depends(get_db)):
    return repository.get_bookstores(db)

@router.post("/", response_model=schema.Bookstore)
def create_bookstore(bookstore: schema.BookstoreCreate, db: Session = Depends(get_db)):
    return repository.create_bookstore(db, bookstore)

@router.get("/{bookstore_id}", response_model=schema.Bookstore)
def get_bookstore(bookstore_id: int, db: Session = Depends(get_db)):
    bookstore = repository.get_bookstore(db, bookstore_id)
    if not bookstore:
        raise HTTPException(status_code=404, detail="Bookstore not found")
    return bookstore

@router.put("/{bookstore_id}", response_model=schema.Bookstore)
def update_bookstore(bookstore_id: int, bookstore: schema.BookstoreCreate, db: Session = Depends(get_db)):
    updated_bookstore = repository.update_bookstore(db, bookstore_id, bookstore)
    if not updated_bookstore:
        raise HTTPException(status_code=404, detail="Bookstore not found")
    return updated_bookstore

@router.delete("/{bookstore_id}", response_model=dict)
def delete_bookstore(bookstore_id: int, db: Session = Depends(get_db)):
    success = repository.delete_bookstore(db, bookstore_id)
    if not success:
        raise HTTPException(status_code=404, detail="Bookstore not found")
    return {"message": "Bookstore deleted successfully"}
