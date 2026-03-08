async function checkout(total){

const res = await fetch(
"http://localhost:8000/api/payment/create-order",

{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({amount:total})
}
)

const order = await res.json()

const options = {

key:"RAZORPAY_KEY",

amount:order.amount,

currency:"INR",

name:"QuickCart",

description:"Smart Checkout",

order_id:order.id,

handler:function(response){

alert("Payment successful")

}

}

const rzp = new Razorpay(options)

rzp.open()

}