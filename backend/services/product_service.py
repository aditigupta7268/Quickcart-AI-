import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from sqlalchemy.orm import Session
from app.models.product import Product
from app.cache.redis_cache import get_cached_product

def fetch_product(db:Session,product_id:str):

    cached = get_cached_product(product_id)

    if cached:

        return cached

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    return product