import pytest
from datetime import datetime
from src.config import Base, engine, SessionLocal
from src.crud import insert_raw, insert_processed, get_all_raw, get_all_processed
from src.schemas import RawDataItem, ProcessedDataItem

@pytest.fixture(scope="module")
def db():
    # Reset DB for tests
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_insert_and_retrieve_raw(db):
    raw = RawDataItem(
        invoice_no="2001",
        stock_code="B001",
        description="DB test product",
        quantity=3,
        invoice_date="2021-01-03",
        price=15.0,
        customer_id=456.0,
        country="US"
    )
    insert_raw(raw, db)   # ✅ pass db
    items = get_all_raw(db)
    assert len(items) == 1
    assert items[0].invoice_no == "2001"

def test_insert_and_retrieve_processed(db):
    processed = ProcessedDataItem(
        invoice_id="INV-2001",
        product_id="PROD-B001",
        quantity=3,
        unit_price=15.0,
        total_price=45.0,
        invoice_datetime=datetime(2021, 1, 3, 10, 0),
        customer_id="456",
        country="US",
        is_return=False
    )
    insert_processed(processed, db)   # ✅ pass db
    items = get_all_processed(db)
    assert len(items) == 1
    assert items[0].invoice_id == "INV-2001"
