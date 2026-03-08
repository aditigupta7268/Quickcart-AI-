import uuid
from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/payment", tags=["payment"])


class PayRequest(BaseModel):
    order_id: int
    method: str   # "upi" | "card" | "wallet"
    amount: float


@router.post("/pay")
def pay(body: PayRequest):
    """
    Simulated payment endpoint.
    In production, call Razorpay / Stripe here with real credentials.
    """
    transaction_id = f"TXN{uuid.uuid4().hex[:10].upper()}"
    return {
        "status": "success",
        "transaction_id": transaction_id,
        "order_id": body.order_id,
        "amount": body.amount,
        "method": body.method,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "message": "Payment processed successfully"
    }
