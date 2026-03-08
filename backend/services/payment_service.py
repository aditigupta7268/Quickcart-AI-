import razorpay
from app.config import RAZORPAY_KEY, RAZORPAY_SECRET

client = razorpay.Client(
auth=(RAZORPAY_KEY,RAZORPAY_SECRET)
)

def create_payment(amount):

    order = client.order.create({

        "amount": int(amount*100),

        "currency":"INR",

        "payment_capture":1

    })

    return order