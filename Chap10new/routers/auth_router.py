from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services import book_service
from schemas.book_schema import Book, BookCreate, BookUpdate
from typing import List
from schemas.user_schema import UserLogin, Token
from services.auth_service import authenticate_user,register_user,get_user
from schemas.user_schema import UserRegister,UsernameRequest
from schemas.user_schema import UserRegister, UserOut  # Import model mới

router = router = APIRouter()

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return authenticate_user(db, user.username, user.password)

@router.post("/register", response_model=UserOut)
def register(user: UserRegister, db: Session = Depends(get_db)):
    return register_user(db, user.username, user.password)

@router.post("/get-user", response_model=UserOut)
def register(username: UsernameRequest, db: Session = Depends(get_db)):
    return get_user(db=db,username=username.username)