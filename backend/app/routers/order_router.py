import uuid
from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional

from app.database import get_db
from app.services.order_service import create_order

router = APIRouter(prefix="/api/order", tags=["order"])


class OrderItem(BaseModel):
    product_id: str
    name: str
    price: float
    quantity: int


class CheckoutRequest(BaseModel):
    items: List[OrderItem]
    total: float
    user_id: Optional[int] = None


@router.post("/checkout")
def checkout(body: CheckoutRequest, db: Session = Depends(get_db)):
    order = create_order(db, body.total, user_id=body.user_id)
    return {
        "message": "Order placed successfully",
        "order_id": order.id,
        "items": [item.dict() for item in body.items],
        "total": body.total,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "receipt_number": f"QC{uuid.uuid4().hex[:8].upper()}"
    }