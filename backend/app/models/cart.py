from sqlalchemy import Column, Integer, String
from app.database import Base

class Cart(Base):

    __tablename__ = "cart"

    id = Column(Integer, primary_key=True)

    product_id = Column(String(50))

    quantity = Column(Integer)