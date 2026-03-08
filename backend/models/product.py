from sqlalchemy import Column, String, Float, Integer
from app.database import Base

class Product(Base):

    __tablename__ = "products"

    id = Column(String(50), primary_key=True)

    name = Column(String(255))

    brand = Column(String(255))

    category = Column(String(100))

    price = Column(Float)

    stock = Column(Integer)