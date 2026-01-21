import pytest
from src.config import Base, engine, SessionLocal
from src.crud import insert_raw, insert_processed, get_all_raw, get_all_processed
from src.schemas import RawDataItem, ProcessedDataItem
from datetime import datetime

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_insert_and_retrieve_raw():
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
    insert_raw(raw)
    items = get_all_raw()
    assert len(items) == 1
    assert items[0].invoice_no == "2001"

def test_insert_and_retrieve_processed():
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
    insert_processed(processed)
    items = get_all_processed()
    assert len(items) == 1
    assert items[0].invoice_id == "INV-2001"
from fastapi.testclient import TestClient
from src.main import app
from datetime import datetime

client = TestClient(app)

def test_post_and_get_raw():
    payload = {
        "invoice_no": "3001",
        "stock_code": "C001",
        "description": "API test product",
        "quantity": 4,
        "invoice_date": "2021-01-04",
        "price": 12.5,
        "customer_id": 789.0,
        "country": "IN"
    }
    response = client.post("/raw", json=payload)
    assert response.status_code == 200

    response = client.get("/raw")
    assert response.status_code == 200
    data = response.json()
    assert any(item["invoice_no"] == "3001" for item in data)

def test_post_and_get_processed():
    payload = {
        "invoice_id": "INV-3001",
        "product_id": "PROD-C001",
        "quantity": 4,
        "unit_price": 12.5,
        "total_price": 50.0,
        "invoice_datetime": datetime(2021, 1, 4, 10, 0).isoformat(),
        "customer_id": "789",
        "country": "IN",
        "is_return": False
    }
    response = client.post("/processed", json=payload)
    assert response.status_code == 200

    response = client.get("/processed")
    assert response.status_code == 200
    data = response.json()
    assert any(item["invoice_id"] == "INV-3001" for item in data)

