from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/bookstores", tags=["bookstores"])

@router.post("/", response_model=schemas.BookStore)
def create_store(store: schemas.BookStoreCreate, db: Session = Depends(database.get_db)):
    return crud.create_store(db, store)

@router.get("/", response_model=list[schemas.BookStore])
def list_stores(db: Session = Depends(database.get_db)):
    return crud.get_stores(db)