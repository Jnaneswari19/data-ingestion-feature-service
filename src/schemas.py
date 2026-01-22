from typing import Optional
from pydantic import BaseModel, Field
from datetime import date, datetime

# --- Raw Data Schemas ---

class RawDataCreate(BaseModel):
    invoice_no: str
    stock_code: str
    description: str
    quantity: int = Field(..., gt=0)   # must be > 0
    invoice_date: date
    price: float = Field(..., gt=0)    # must be > 0
    customer_id: float
    country: str

class RawDataItem(RawDataCreate):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# --- Processed Data Schemas ---

class ProcessedDataCreate(BaseModel):
    invoice_id: str
    product_id: str
    quantity: int   # allow negative for returns
    unit_price: float
    total_price: float
    invoice_datetime: datetime
    customer_id: Optional[str] = None  # allow None
    country: str
    is_return: bool

class ProcessedDataItem(ProcessedDataCreate):
    id: Optional[int] = None

    class Config:
        orm_mode = True
