const API = 'http://localhost:8000/api';

// ── AUTH ──────────────────────────────────────────────────────────────────────
async function signIn(email, password) {
  const res = await fetch(`${API}/auth/signin`, {
    method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({email, password})
  });
  if (!res.ok) throw new Error((await res.json()).detail || 'Sign in failed');
  return await res.json();
}

async function signUp(name, email, password) {
  const res = await fetch(`${API}/auth/signup`, {
    method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({name, email, password})
  });
  if (!res.ok) throw new Error((await res.json()).detail || 'Sign up failed');
  return await res.json();
}

async function signOut(token) {
  await fetch(`${API}/auth/signout`, {
    method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({token})
  });
}

// ── PRODUCTS ──────────────────────────────────────────────────────────────────
async function getProduct(id) {
  const res = await fetch(`${API}/products/${id}`);
  return await res.json();
}

// ── CART ──────────────────────────────────────────────────────────────────────
async function addToCart(productId) {
  const res = await fetch(`${API}/cart/add?product_id=${productId}`, {method: 'POST'});
  return await res.json();
}

async function getCart() {
  const res = await fetch(`${API}/cart/`);
  return await res.json();
}

async function removeCartItem(itemId) {
  const res = await fetch(`${API}/cart/${itemId}`, {method: 'DELETE'});
  return await res.json();
}

async function updateCartQty(itemId, quantity) {
  const res = await fetch(`${API}/cart/${itemId}`, {
    method: 'PUT', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({quantity})
  });
  return await res.json();
}

// ── ORDER ─────────────────────────────────────────────────────────────────────
async function placeOrder(items, total) {
  const res = await fetch(`${API}/order/checkout`, {
    method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({items, total})
  });
  if (!res.ok) throw new Error('Order placement failed');
  return await res.json();
}

// ── PAYMENT ───────────────────────────────────────────────────────────────────
async function payOrder(orderId, method, amount) {
  const res = await fetch(`${API}/payment/pay`, {
    method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({order_id: orderId, method, amount})
  });
  if (!res.ok) throw new Error('Payment failed');
  return await res.json();
}