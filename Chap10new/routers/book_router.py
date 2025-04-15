from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services import book_service
from schemas.book_schema import Book, BookCreate, BookUpdate
from typing import List

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=List[Book])
def get_books(db: Session = Depends(get_db)):
    return book_service.list_books(db)

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = book_service.retrieve_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return book_service.add_book(db, book)

@router.delete("/{book_id}", response_model=Book)
def delete_book( book_id:int,db:Session= Depends(get_db)):
    return book_service.delete_book(db,book_id)

@router.put("/{book_id}", response_model=Book) 
def update_book(book_id: int, updated_book_data: BookUpdate, db: Session = Depends(get_db)):
    updated_book = book_service.update_book(db, book_id, updated_book_data)
    return updated_book