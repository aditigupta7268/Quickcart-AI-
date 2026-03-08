# 🛒 QuickCart AI — Smart Retail Checkout System

QuickCart AI is a smart retail checkout system that allows customers to **scan products, add them to a cart, and complete checkout without standing in queues**.
The system integrates a **FastAPI backend, MySQL database, QR-based product scanning, and AI-powered insights using Gemini**.

This project demonstrates a **full-stack architecture similar to modern self-checkout systems used in smart retail stores.**

---

## 🚀 Features

* 📱 **QR Code Product Scanning**
* 🛍 **Real-time Cart Management**
* 💳 **UPI Payment Simulation**
* 🧾 **Digital Receipt Generation**
* 🤖 **AI-powered cart analysis using Gemini**
* ⚡ **FastAPI backend with REST APIs**
* 🗄 **MySQL database for product & order storage**
* ⚡ **Redis caching for faster product lookup**
* 🌐 **Nginx reverse proxy for unified frontend & backend routing**

---

## 🧱 System Architecture

```
Customer (Browser)
        │
        ▼
Frontend (HTML + JS)
        │
        ▼
Nginx Reverse Proxy
        │
        ├── /          → Frontend UI
        └── /api       → FastAPI Backend
                            │
                            ├── MySQL Database
                            ├── Redis Cache
                            └── Gemini AI API
```

---

## 🖥 Project Structure

```
quickcart-ai/
│
├── frontend/
│   ├── index.html
│   ├── signup.html
│   ├── signin.html
│   ├── scan.html
│   ├── cart.html
│   ├── payment.html
│   ├── receipt.html
│   │
│   ├── css/
│   │   └── styles.css
│   │
│   └── js/
│       ├── api.js
│       ├── auth.js
│       ├── scanner.js
│       ├── cart.js
│       └── payment.js
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   │
│   │   ├── models/
│   │   ├── routers/
│   │   ├── services/
│   │   ├── cache/
│   │   └── ai/
│   │
│   ├── requirements.txt
│   └── .env
│
└── docker-compose.yml
```

---

## 🛠 Tech Stack

### Frontend

* HTML5
* CSS3
* Vanilla JavaScript
* HTML5 QR Scanner

### Backend

* FastAPI
* Python
* SQLAlchemy

### Database

* MySQL

### Cache

* Redis

### AI

* Google Gemini API

### Infrastructure

* Nginx Reverse Proxy
* Docker (optional)

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/quickcart-ai.git
cd quickcart-ai
```

---

### 2️⃣ Backend Setup

```
cd backend
pip install -r requirements.txt
```

Create `.env` file:

```
DATABASE_URL=mysql+pymysql://root:yourpassword@localhost:3306/quickcart
REDIS_HOST=localhost
REDIS_PORT=6379
GEMINI_API_KEY=your_gemini_api_key
```

Run backend:

```
uvicorn app.main:app --reload
```

Backend will start at:

```
http://localhost:8000
```

Swagger API docs:

```
http://localhost:8000/docs
```

---

### 3️⃣ Frontend Setup

Open frontend using Live Server or any static server:

```
frontend/index.html
```

Default development URL:

```
http://localhost:5500
```

---

## 🔍 Example API Endpoints

### Get Product

```
GET /api/products/{product_id}
```

Example:

```
GET /api/products/MILK001
```

---

### Add Item to Cart

```
POST /api/cart/add
```

---

### Checkout Order

```
POST /api/order/checkout
```

---

## 🤖 AI Integration

The system integrates **Gemini AI** for:

* Smart cart analysis
* Purchase insights
* Recommendation suggestions

Example usage:

```
Analyze this shopping cart and provide insights.
```

---

## 📸 Screens

Typical flow:

```
Sign Up
   ↓
Sign In
   ↓
Scan Product
   ↓
Cart
   ↓
Payment
   ↓
Receipt
```

---

## 🔮 Future Improvements

* Real UPI payment integration
* Smart inventory prediction
* Admin dashboard
* Multi-store support
* Cloud deployment

---

---

## 👩‍💻 Author

**Aditi Gupta**

B.Tech Electronics & Communication Engineering
The LNM Institute of Information Technology

---

⭐ If you found this project useful, please consider giving it a star!
