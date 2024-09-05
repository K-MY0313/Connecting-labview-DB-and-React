import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from sqlalchemy.orm import Session
from pyDB import models, database
from datetime import datetime

# LabVIEWとの連携用関数
def update_measurement(data):
    db = database.SessionLocal()
    value=data
    new_measurement = models.Measurement(value=data, timestamp=datetime.now())
    db.add(new_measurement)
    db.commit()
    db.refresh(new_measurement)
    return  value
   