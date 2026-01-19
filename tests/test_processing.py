import pytest
from src.schemas import RawDataItem, ProcessedDataItem
from src.processing import transform_data
from datetime import datetime

def test_transform_data_basic():
    raw_items = [
        RawDataItem(
            invoice_no="1001",
            stock_code="A001",
            description="Test product",
            quantity=2,
            invoice_date="2021-01-01",
            price=10.0,
            customer_id=123.0,
            country="UK"
        ),
        RawDataItem(
            invoice_no="1002",
            stock_code="A002",
            description="Returned product",
            quantity=-1,
            invoice_date="2021-01-02",
            price=5.0,
            customer_id=None,
            country="UK"
        )
    ]

    processed = transform_data(raw_items)

    # Check first item
    p1 = processed[0]
    assert isinstance(p1, ProcessedDataItem)
    assert p1.total_price == 20.0
    assert p1.is_return is False
    assert p1.customer_id == "123"

    # Check second item
    p2 = processed[1]
    assert p2.is_return is True
    assert p2.customer_id == "UNKNOWN"
    assert p2.total_price == -5.0
    assert p2.invoice_id.startswith("INV-")
    assert p2.product_id.startswith("PROD-")
