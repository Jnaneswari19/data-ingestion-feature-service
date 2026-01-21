from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from src.config import Base, SessionLocal
from src.schemas import RawDataItem, ProcessedDataItem

# --- Models ---
class RawData(Base):
    __tablename__ = "raw_data"

    id = Column(Integer, primary_key=True, index=True)
    invoice_no = Column(String, index=True)
    stock_code = Column(String)
    description = Column(String)
    quantity = Column(Integer)
    invoice_date = Column(String)
    price = Column(Float)
    customer_id = Column(String)
    country = Column(String)

class ProcessedData(Base):
    __tablename__ = "processed_data"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(String, index=True)
    product_id = Column(String)
    quantity = Column(Integer)
    unit_price = Column(Float)
    total_price = Column(Float)
    invoice_datetime = Column(DateTime)
    customer_id = Column(String)
    country = Column(String)
    is_return = Column(Boolean)

# --- CRUD Functions ---
def init_db():
    Base.metadata.create_all(bind=SessionLocal.kw["bind"])

def insert_raw(raw_item: RawDataItem):
    db = SessionLocal()
    db_item = RawData(**raw_item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item

def insert_processed(processed_item: ProcessedDataItem):
    db = SessionLocal()
    db_item = ProcessedData(**processed_item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item

def get_all_raw():
    db = SessionLocal()
    items = db.query(RawData).all()
    db.close()
    return items

def get_all_processed():
    db = SessionLocal()
    items = db.query(ProcessedData).all()
    db.close()
    return items

