# This module contains functions related to order management.

import random
from app.models.order import Order as DBOrder

class Order:
    def __init__(self, order_id, amount):
        self.id = order_id
        self.amount = amount

def create_order(db, amount, user_id=None):
    """
    Create a new order.

    Args:
        db (Session): The database session.
        amount (float): The order amount.
        user_id (int, optional): The user making the order.

    Returns:
        Order: An Order object containing the created order information.
    """
    # Simulate AI Fraud check and scan time
    process_time = random.randint(15, 65)
    # 5% chance of being flagged for review
    status = "review" if random.random() < 0.05 else "completed" 

    db_order = DBOrder(
        user_id=user_id,
        total_amount=amount,
        status=status,
        processing_time_ms=process_time
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    
    return Order(order_id=db_order.id, amount=db_order.total_amount)