from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os, time

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./local_test.db")

# Retry loop for Postgres startup
for i in range(5):
    try:
        if DATABASE_URL.startswith("sqlite"):
            engine = create_engine(
                DATABASE_URL, connect_args={"check_same_thread": False}
            )
        else:
            engine = create_engine(DATABASE_URL)
        break
    except Exception as e:
        print(f"Database connection failed, retrying... ({i+1}/5)")
        time.sleep(5)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
