from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.cart import Cart


def add_cart(db: Session, product_id: str):
    item = Cart(product_id=product_id, quantity=1)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get_cart(db: Session):
    items = db.query(Cart).all()
    # Enrich with mock product data — replace with real DB join when products table exists
    result = []
    for item in items:
        result.append({
            "id": item.id,
            "product_id": item.product_id,
            "name": f"Product {item.product_id}",
            "price": 99.0,
            "quantity": item.quantity,
            "subtotal": round(99.0 * item.quantity, 2)
        })
    return result


def remove_cart_item(db: Session, item_id: int):
    item = db.query(Cart).filter(Cart.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    db.delete(item)
    db.commit()
    return {"message": "Item removed", "item_id": item_id}


def update_cart_quantity(db: Session, item_id: int, quantity: int):
    item = db.query(Cart).filter(Cart.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    item.quantity = max(1, quantity)
    db.commit()
    db.refresh(item)
    return {"message": "Quantity updated", "item_id": item_id, "quantity": item.quantity}