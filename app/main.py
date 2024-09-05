from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, database
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORSミドルウェアを追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Reactアプリのオリジン
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# データベースのテーブルを作成
models.Base.metadata.create_all(bind=database.engine)

@app.get("/measurements/", response_model=List[schemas.Measurement])
def read_measurements(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    measurements = db.query(models.Measurement).order_by(models.Measurement.timestamp.desc()).offset(skip).limit(limit).all()
    return measurements

@app.get("/measurements/latest/", response_model=schemas.Measurement)
def read_latest_measurement(db: Session = Depends(database.get_db)):
    measurement = db.query(models.Measurement).order_by(models.Measurement.timestamp.desc()).first()
    if measurement is None:
        raise HTTPException(status_code=404, detail="No measurements found")
    return measurement