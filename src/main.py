from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

logging.basicConfig(level="INFO", format="%(asctime)s - %(levelname)s - %(message)s")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    Instrumentator().instrument(app).expose(app)

@app.get("/health")
def health_check():
    return {"status": "ok"}
