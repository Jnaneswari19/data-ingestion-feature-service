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
