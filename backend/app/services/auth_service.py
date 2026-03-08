import uuid
import bcrypt as _bcrypt
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.user import User

# In-memory session store: token -> user_id
# In production replace with Redis / DB-backed sessions
_sessions: dict[str, int] = {}


def _hash_password(password: str) -> str:
    return _bcrypt.hashpw(password.encode("utf-8"), _bcrypt.gensalt()).decode("utf-8")


def _verify_password(plain: str, hashed: str) -> bool:
    try:
        return _bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))
    except Exception:
        return False



def signup_user(db: Session, name: str, email: str, password: str) -> dict:
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    user = User(
        name=name,
        email=email,
        hashed_password=_hash_password(password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = str(uuid.uuid4())
    _sessions[token] = user.id
    return {"token": token, "user_id": user.id, "name": user.name, "email": user.email}


def signin_user(db: Session, email: str, password: str) -> dict:
    user = db.query(User).filter(User.email == email).first()
    if not user or not _verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    token = str(uuid.uuid4())
    _sessions[token] = user.id
    return {"token": token, "user_id": user.id, "name": user.name, "email": user.email}


def signout_user(token: str) -> dict:
    _sessions.pop(token, None)
    return {"message": "Signed out successfully"}


def get_current_user_id(token: Optional[str]) -> Optional[int]:
    if not token:
        return None
    return _sessions.get(token)
