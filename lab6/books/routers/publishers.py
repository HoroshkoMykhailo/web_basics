from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/publishers", tags=["publishers"])

@router.post("/", response_model=schemas.Publisher)
def create_publisher(publisher: schemas.PublisherCreate, db: Session = Depends(database.get_db)):
    return crud.create_publisher(db, publisher)

@router.get("/", response_model=list[schemas.Publisher])
def list_publishers(db: Session = Depends(database.get_db)):
    return crud.get_publishers(db)