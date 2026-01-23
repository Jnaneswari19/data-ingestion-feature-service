from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

logging.basicConfig(level="INFO", format="%(asctime)s - %(levelname)s - %(message)s")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Prometheus metrics
Instrumentator().instrument(app).expose(app)

@app.get("/health")
def health_check():
    return {"status": "ok"}

# In-memory storage for demo purposes
raw_data_store = []
processed_data_store = []

@app.post("/raw")
def create_raw(payload: dict):
    raw_data_store.append(payload)
    return payload  # ✅ return the payload directly

@app.get("/raw")
def get_raw():
    return raw_data_store  # ✅ return the list directly

@app.post("/processed")
def create_processed(payload: dict):
    processed_data_store.append(payload)
    return payload  # ✅ return the payload directly

@app.get("/processed")
def get_processed():
    return processed_data_store  # ✅ return the list directly
