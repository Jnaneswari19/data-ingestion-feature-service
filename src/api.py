
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config import SessionLocal
from src.schemas import RawDataItem, ProcessedDataItem
from src.crud import insert_raw, insert_processed, get_all_raw, get_all_processed

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/raw")
def create_raw(raw_item: RawDataItem, db: Session = Depends(get_db)):
    return insert_raw(raw_item)

@router.get("/raw")
def list_raw(db: Session = Depends(get_db)):
    return get_all_raw()

@router.post("/processed")
def create_processed(processed_item: ProcessedDataItem, db: Session = Depends(get_db)):
    return insert_processed(processed_item)

@router.get("/processed")
def list_processed(db: Session = Depends(get_db)):
    return get_all_processed()
