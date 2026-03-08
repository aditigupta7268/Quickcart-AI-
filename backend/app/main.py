import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.models import user  # noqa: F401 — ensures User table is created
from app.models import cart  # noqa: F401 — ensures Cart table is created
from app.models import order  # noqa: F401 — ensures Order table is created

from app.routers import product_router, cart_router, order_router, auth_router, payment_router, dashboard_router

# Create all tables (User, Cart) if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="QuickCart AI API", version="2.0")

# ── CORS ──────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── ROUTERS ───────────────────────────────────────────────────────────────────
app.include_router(product_router.router) if hasattr(product_router, 'router') else app.include_router(product_router)
app.include_router(cart_router.router) if hasattr(cart_router, 'router') else app.include_router(cart_router)
app.include_router(order_router.router) if hasattr(order_router, 'router') else app.include_router(order_router)
app.include_router(auth_router.router) if hasattr(auth_router, 'router') else app.include_router(auth_router)
app.include_router(payment_router.router) if hasattr(payment_router, 'router') else app.include_router(payment_router)
app.include_router(dashboard_router.router)

# ── FRONTEND PAGES ────────────────────────────────────────────────────────────
FRONTEND = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "frontend")

@app.get("/")
def serve_index():
    return FileResponse(os.path.join(FRONTEND, "index.html"))

@app.get("/signin")
def serve_signin():
    return FileResponse(os.path.join(FRONTEND, "signin.html"))

@app.get("/checkout")
def serve_checkout():
    return FileResponse(os.path.join(FRONTEND, "checkout.html"))

@app.get("/payment")
def serve_payment():
    return FileResponse(os.path.join(FRONTEND, "payment.html"))

@app.get("/receipt")
def serve_receipt():
    return FileResponse(os.path.join(FRONTEND, "receipt.html"))

@app.get("/scanner")
def serve_scanner():
    return FileResponse(os.path.join(FRONTEND, "scanner.html"))

@app.get("/dashboard")
def serve_dashboard():
    return FileResponse(os.path.join(FRONTEND, "dashboard.html"))

@app.get("/billing")
def serve_billing():
    return FileResponse(os.path.join(FRONTEND, "billing.html"))

from fastapi.responses import RedirectResponse

@app.get("/shop.html")
def redirect_shop():
    return RedirectResponse(url="/signin", status_code=302)

@app.get("/favicon.ico")
def favicon():
    return JSONResponse(content={}, status_code=204)

# ── STATIC ASSETS (JS, CSS, images) ──────────────────────────────────────────
app.mount("/static", StaticFiles(directory=FRONTEND), name="static")