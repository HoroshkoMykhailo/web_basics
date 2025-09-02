from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...database import get_db
from . import repository, schema

router = APIRouter(prefix="/author-book", tags=["author-book"])

@router.post("/", response_model=schema.AuthorBook)
def create_author_book(relation: schema.AuthorBookCreate, db: Session = Depends(get_db)):
    return repository.create_author_book(db, relation)

@router.get("/", response_model=list[schema.AuthorBook])
def read_author_books(db: Session = Depends(get_db)):
    return repository.get_author_books(db)

@router.get("/{relation_id}", response_model=schema.AuthorBook)
def read_author_book(relation_id: int, db: Session = Depends(get_db)):
    relation = repository.get_author_book(db, relation_id)
    if not relation:
        raise HTTPException(status_code=404, detail="Relation not found")
    return relation

@router.put("/{relation_id}", response_model=schema.AuthorBook)
def update_author_book(relation_id: int, relation: schema.AuthorBookCreate, db: Session = Depends(get_db)):
    updated_relation = repository.update_author_book(db, relation_id, relation)
    if not updated_relation:
        raise HTTPException(status_code=404, detail="Relation not found")
    return updated_relation

@router.delete("/{relation_id}", response_model=dict)
def delete_author_book(relation_id: int, db: Session = Depends(get_db)):
    success = repository.delete_author_book(db, relation_id)
    if not success:
        raise HTTPException(status_code=404, detail="Relation not found")
    return {"message": "Relation deleted successfully"}
