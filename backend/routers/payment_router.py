from fastapi import APIRouter
from app.services.payment_service import create_payment

router = APIRouter(prefix="/api/payment")

@router.post("/create")

def create(amount:float):

    order = create_payment(amount)

    return order