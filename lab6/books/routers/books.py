from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/books", tags=["books"])

@router.post("/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    return crud.create_book(db, book)

@router.get("/", response_model=list[schemas.Book])
def list_books(db: Session = Depends(database.get_db)):
    return crud.get_books(db)