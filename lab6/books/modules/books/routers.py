from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...database import get_db
from . import repository, schema
from .schema_complex import BookComplex

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=list[BookComplex])
def read_books(db: Session = Depends(get_db)):
    return repository.get_books(db)

@router.post("/", response_model=schema.Book)
def create_book(book: schema.BookCreate, db: Session = Depends(get_db)):
    
    return repository.create_book(db, book)

@router.get("/{book_id}", response_model=schema.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = repository.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=schema.Book)
def update_book(book_id: int, book: schema.BookCreate, db: Session = Depends(get_db)):
    updated_book = repository.update_book(db, book_id, book)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@router.delete("/{book_id}", response_model=dict)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    success = repository.delete_book(db, book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
