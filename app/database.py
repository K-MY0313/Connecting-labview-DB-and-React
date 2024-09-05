from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:r6Jg8Pfq@localhost/postgres"

# データベースエンジンを作成
engine = create_engine(DATABASE_URL)

# セッションを作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ベースクラスを作成
Base = declarative_base()

# Define a function to get the database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
