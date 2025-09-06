from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...database import get_db
from . import repository, schema

router = APIRouter(prefix="/publishers", tags=["publishers"])

@router.get("/", response_model=list[schema.Publisher])
def read_publishers(db: Session = Depends(get_db)):
    return repository.get_publishers(db)

@router.post("/", response_model=schema.Publisher)
def create_publisher(publisher: schema.PublisherCreate, db: Session = Depends(get_db)):
    return repository.create_publisher(db, publisher)

@router.get("/{publisher_id}", response_model=schema.Publisher)
def get_publisher(publisher_id: int, db: Session = Depends(get_db)):
    publisher = repository.get_publisher(db, publisher_id)
    if not publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return publisher

@router.put("/{publisher_id}", response_model=schema.Publisher)
def update_publisher(publisher_id: int, publisher: schema.PublisherCreate, db: Session = Depends(get_db)):
    updated_publisher = repository.update_publisher(db, publisher_id, publisher)
    if not updated_publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return updated_publisher

@router.delete("/{publisher_id}", response_model=dict)
def delete_publisher(publisher_id: int, db: Session = Depends(get_db)):
    success = repository.delete_publisher(db, publisher_id)
    if not success:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return {"message": "Publisher deleted successfully"}
