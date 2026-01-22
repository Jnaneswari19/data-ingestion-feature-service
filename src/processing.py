import pandas as pd
from typing import List
from src.schemas import RawDataItem, ProcessedDataItem
from datetime import datetime


def transform_data(raw_data: List[RawDataItem]) -> List[ProcessedDataItem]:
    # Convert list of RawDataItem → DataFrame
    df = pd.DataFrame([item.dict() for item in raw_data])

    # --- Cleaning & Transformation Steps ---
    # 1. Convert invoice_date → datetime
    df["invoice_datetime"] = pd.to_datetime(df["invoice_date"], errors="coerce")

    # Handle missing customer_id → "UNKNOWN", normalize floats
    df["customer_id"] = df["customer_id"].apply(
        lambda x: (
            "UNKNOWN"
            if pd.isna(x)
            else str(int(x)) if isinstance(x, float) and x.is_integer() else str(x)
        )
    )

    # 3. Calculate total_price = quantity * price
    df["total_price"] = df["quantity"] * df["price"]

    # 4. Derive is_return flag (negative quantity means return)
    df["is_return"] = df["quantity"] < 0

    # 5. Standardize IDs
    df["invoice_id"] = "INV-" + df["invoice_no"].astype(str)
    df["product_id"] = "PROD-" + df["stock_code"].astype(str)

    # Example aggregated feature: customer_total_spend
    customer_spend = df.groupby("customer_id")["total_price"].transform("sum")
    df["customer_total_spend"] = customer_spend

    # --- Map to ProcessedDataItem ---
    processed_items = []
    for record in df.to_dict(orient="records"):
        item = ProcessedDataItem(
            invoice_id=record["invoice_id"],
            product_id=record["product_id"],
            quantity=record["quantity"],
            unit_price=record["price"],
            total_price=record["total_price"],
            invoice_datetime=record["invoice_datetime"],
            customer_id=record["customer_id"],
            country=record["country"],
            is_return=record["is_return"],
        )
        processed_items.append(item)

    return processed_items
