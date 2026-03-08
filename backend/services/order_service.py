import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.order_service import create_order

router = APIRouter(
prefix="/api/order"
)

@router.post("/checkout")

def checkout(amount:float,db:Session=Depends(get_db)):

    order = create_order(db,amount)

    return {

        "message":"Order placed successfully",

        "order_id":order.id,

        "amount":amount
    }