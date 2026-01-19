
import pytest
from pydantic import ValidationError
from src.schemas import RawDataItem, ProcessedDataItem
from datetime import datetime

def test_valid_raw_data():
    item = RawDataItem(
        invoice_no="12345",
        stock_code="A001",
        description="Test product",
        quantity=2,
        invoice_date="2021-01-01",
        price=10.5,
        customer_id=123.0,
        country="UK"
    )
    assert item.quantity == 2
    assert item.price == 10.5

def test_invalid_quantity():
    with pytest.raises(ValidationError):
        RawDataItem(
            invoice_no="12345",
            stock_code="A001",
            description="Test product",
            quantity=-1,  # ❌ invalid
            invoice_date="2021-01-01",
            price=10.5,
            customer_id=123.0,
            country="UK"
        )

def test_invalid_price():
    with pytest.raises(ValidationError):
        RawDataItem(
            invoice_no="12345",
            stock_code="A001",
            description="Test product",
            quantity=1,
            invoice_date="2021-01-01",
            price=-5.0,  # ❌ invalid
            customer_id=123.0,
            country="UK"
        )

def test_valid_processed_data():
    item = ProcessedDataItem(
        invoice_id="INV-001",
        product_id="PROD-001",
        quantity=3,
        unit_price=5.0,
        total_price=15.0,
        invoice_datetime=datetime(2021, 1, 1, 12, 0),
        customer_id="123",
        country="UK",
        is_return=False
    )
    assert item.total_price == 15.0
    assert item.is_return is False
