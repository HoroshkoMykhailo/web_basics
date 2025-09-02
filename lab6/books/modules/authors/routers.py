from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...database import get_db
from . import repository, schema, schema_complex

router = APIRouter(prefix="/authors", tags=["authors"])

@router.get("/", response_model=list[schema_complex.AuthorWithBooks])
def read_authors(db: Session = Depends(get_db)):
    return repository.get_authors(db)

@router.post("/", response_model=schema.Author)
def create_author(author: schema.AuthorCreate, db: Session = Depends(get_db)):
    return repository.create_author(db, author)

@router.get("/{author_id}", response_model=schema_complex.AuthorWithBooks)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = repository.get_author(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.put("/{author_id}", response_model=schema.Author)
def update_author(author_id: int, author: schema.AuthorCreate, db: Session = Depends(get_db)):
    updated_author = repository.update_author(db, author_id, author)
    if not updated_author:
        raise HTTPException(status_code=404, detail="Author not found")
    return updated_author

@router.delete("/{author_id}", response_model=dict)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    success = repository.delete_author(db, author_id)
    if not success:
        raise HTTPException(status_code=404, detail="Author not found")
    return {"message": "Author deleted successfully"}
