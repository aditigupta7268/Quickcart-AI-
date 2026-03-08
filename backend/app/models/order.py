from sqlalchemy import Column, Integer, Float, String, DateTime
from app.database import Base
from datetime import datetime

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=True) # Optional link to user who made order
    total_amount = Column(Float, nullable=False)
    status = Column(String(50), nullable=False, default="completed") # 'completed', 'review', etc.
    processing_time_ms = Column(Integer, nullable=False, default=0) # Simulated AI metric
    created_at = Column(DateTime, default=datetime.utcnow)
