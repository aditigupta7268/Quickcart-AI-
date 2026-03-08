import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.product_service import fetch_product

router = APIRouter(
prefix="/api/products"
)

@router.get("/{product_id}")

def get_product(product_id:str,db:Session=Depends(get_db)):

    product = fetch_product(db,product_id)

    if not product:

        return {"error":"not found"}

    return product