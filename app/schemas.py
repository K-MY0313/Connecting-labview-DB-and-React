from pydantic import BaseModel
from datetime import datetime

class MeasurementBase(BaseModel):
    value: float
    timestamp: datetime

class MeasurementCreate(MeasurementBase):
    pass

class Measurement(MeasurementBase):
    id: int

    class Config:
        orm_mode = True