from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .config import SessionLocal
from .schemas import RawDataCreate, ProcessedDataCreate
from .crud import create_raw, create_processed, get_all_raw, get_all_processed

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/raw")
def post_raw(raw: RawDataCreate, db: Session = Depends(get_db)):
    return create_raw(db, raw)

@router.get("/raw")
def get_raw(db: Session = Depends(get_db)):
    return get_all_raw(db)

@router.post("/processed")
def post_processed(processed: ProcessedDataCreate, db: Session = Depends(get_db)):
    return create_processed(db, processed)

@router.get("/processed")
def get_processed(db: Session = Depends(get_db)):
    return get_all_processed(db)
