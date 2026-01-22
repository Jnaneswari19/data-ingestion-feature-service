from sqlalchemy.orm import Session
from .models import RawData, ProcessedData
from .schemas import RawDataCreate, RawDataItem, ProcessedDataCreate, ProcessedDataItem

# --- Raw Data CRUD ---

def create_raw(db: Session, raw: RawDataCreate) -> RawData:
    db_raw = RawData(**raw.dict())
    db.add(db_raw)
    db.commit()
    db.refresh(db_raw)
    return db_raw

def insert_raw(raw_item: RawDataItem, db: Session):
    db_item = RawData(**raw_item.dict(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_all_raw(db: Session):
    return db.query(RawData).all()


# --- Processed Data CRUD ---

def create_processed(db: Session, processed: ProcessedDataCreate) -> ProcessedData:
    db_processed = ProcessedData(**processed.dict())
    db.add(db_processed)
    db.commit()
    db.refresh(db_processed)
    return db_processed

def insert_processed(processed_item: ProcessedDataItem, db: Session):
    db_item = ProcessedData(**processed_item.dict(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_all_processed(db: Session):
    return db.query(ProcessedData).all()
