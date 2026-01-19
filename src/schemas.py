from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Raw incoming data schema
class RawDataItem(BaseModel):
    invoice_no: str
    stock_code: str
    description: Optional[str]
    quantity: int  # allow negative for returns
    invoice_date: str
    price: float = Field(..., gt=0.0)
    customer_id: Optional[float]
    country: str


# Processed data schema after transformations
class ProcessedDataItem(BaseModel):
    invoice_id: str
    product_id: str
    quantity: int   # allow negative for returns
    unit_price: float = Field(..., gt=0.0)
    total_price: float   # allow negative for returns
    invoice_datetime: datetime
    customer_id: Optional[str]
    country: str
    is_return: bool = Field(False, description="Flag if transaction is a return")

