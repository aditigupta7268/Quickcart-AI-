from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List

from app.database import get_db
from app.services.cart_service import add_cart, get_cart, remove_cart_item, update_cart_quantity

router = APIRouter(prefix="/api/cart", tags=["cart"])


class UpdateQtyRequest(BaseModel):
    quantity: int


@router.post("/add")
def add(product_id: str, db: Session = Depends(get_db)):
    item = add_cart(db, product_id)
    return {"message": "added", "item_id": item.id}


@router.get("/")
def get_all_cart(db: Session = Depends(get_db)):
    return get_cart(db)


@router.delete("/{item_id}")
def remove_item(item_id: int, db: Session = Depends(get_db)):
    return remove_cart_item(db, item_id)


@router.put("/{item_id}")
def update_item(item_id: int, body: UpdateQtyRequest, db: Session = Depends(get_db)):
    return update_cart_quantity(db, item_id, body.quantity)