from sqlalchemy.orm import Session
from schemas.book_schema import BookCreate,BookUpdate,Book
from repositories import book_repository

def list_books(db: Session):
    return book_repository.get_all_books(db)

def retrieve_book(db: Session, book_id: int):
    return book_repository.get_book_by_id(db, book_id)

def add_book(db: Session, book_data: BookCreate):
    return book_repository.create_book(db, book_data)

def delete_book (db: Session, book_id: int):
    return book_repository.delete_book(db,book_id)

def update_book (db:Session,book_id:int,updated_book_data: BookUpdate):
    updated_book = book_repository.update_book(db, book_id, updated_book_data.dict())
    return updated_book