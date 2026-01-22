from fastapi import FastAPI
from src.api import router
from src.config import Base, engine
import src.models  # ✅ ensures models are registered

app = FastAPI()

# ✅ Create tables after models are imported
Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
