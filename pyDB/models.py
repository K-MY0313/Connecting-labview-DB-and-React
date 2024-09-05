from sqlalchemy import Column, Integer, String, DateTime, Date, Interval, ForeignKey,Float
from .database import Base

class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime(timezone=True), nullable=False)

