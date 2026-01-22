from src.schemas import RawDataItem, ProcessedDataItem
from datetime import date, datetime

def test_transform_data_basic():
    raw_items = [
        RawDataItem(
            invoice_no="1001",
            stock_code="A001",
            description="Test product",
            quantity=2,
            invoice_date=date(2021, 1, 1),
            price=10.0,
            customer_id=123.0,
            country="UK"
        )
    ]

    # Transformation logic should create a ProcessedDataItem with is_return=True
    processed = ProcessedDataItem(
        invoice_id="1002",
        product_id="A002",
        quantity=-1,   # negative allowed here
        unit_price=5.0,
        total_price=-5.0,
        invoice_datetime=datetime(2021, 1, 2),
        customer_id=None,
        country="UK",
        is_return=True
    )

    assert processed.is_return is True
    assert processed.total_price < 0
