from sqlalchemy.orm import Session
from models.book_model import Book
from schemas.book_schema import BookCreate,BookUpdate
from fastapi import HTTPException

def get_all_books(db: Session):
    return db.query(Book).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, book: BookCreate):
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
def delete_book (db: Session, book_id: int):
    book=db.query(Book).filter(Book.id == book_id).first()
    if not book:
         raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return book

def update_book(db: Session, book_id: int, updated_book_data: dict):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Not found book")
    for key, value in updated_book_data.items():
        if value:
            setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book

