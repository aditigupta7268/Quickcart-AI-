from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.services.auth_service import signup_user, signin_user, signout_user

router = APIRouter(prefix="/api/auth", tags=["auth"])


class SignUpRequest(BaseModel):
    name: str
    email: str
    password: str


class SignInRequest(BaseModel):
    email: str
    password: str


class SignOutRequest(BaseModel):
    token: str


@router.post("/signup")
def signup(body: SignUpRequest, db: Session = Depends(get_db)):
    return signup_user(db, body.name, body.email, body.password)


@router.post("/signin")
def signin(body: SignInRequest, db: Session = Depends(get_db)):
    return signin_user(db, body.email, body.password)


@router.post("/signout")
def signout(body: SignOutRequest):
    return signout_user(body.token)
