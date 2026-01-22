from sqlalchemy import Column, Integer, String, Float, Date, DateTime, Boolean
from .config import Base

class RawData(Base):
    __tablename__ = "raw_data"

    id = Column(Integer, primary_key=True, index=True)
    invoice_no = Column(String, nullable=False)
    stock_code = Column(String, nullable=False)
    description = Column(String)
    quantity = Column(Integer, nullable=False)
    invoice_date = Column(Date, nullable=False)
    price = Column(Float, nullable=False)
    customer_id = Column(Float, nullable=False)
    country = Column(String, nullable=False)

class ProcessedData(Base):
    __tablename__ = "processed_data"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(String, nullable=False)   # ✅ added
    product_id = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)
    invoice_datetime = Column(DateTime, nullable=False)
    customer_id = Column(String, nullable=False)
    country = Column(String, nullable=False)
    is_return = Column(Boolean, default=False)
