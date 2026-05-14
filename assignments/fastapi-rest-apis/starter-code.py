from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    year: int = Field(..., ge=0)

books = {
    1: Book(id=1, title="Python Basics", author="A. Student", year=2025),
    2: Book(id=2, title="FastAPI Fundamentals", author="B. Developer", year=2026),
}

# TODO: Return a welcome message
# @app.get("/")
# def read_root():
#     ...

# TODO: Return all books with optional filtering
# @app.get("/books")
# def read_books(author: Optional[str] = Query(None), year: Optional[int] = Query(None)):
#     ...

# TODO: Return a single book by ID
# @app.get("/books/{book_id}")
# def read_book(book_id: int):
#     ...

# TODO: Create a new book
# @app.post("/books")
# def create_book(book: Book):
#     ...

# TODO: Update an existing book
# @app.put("/books/{book_id}")
# def update_book(book_id: int, book: Book):
#     ...

# TODO: Delete a book
# @app.delete("/books/{book_id}")
# def delete_book(book_id: int):
#     ...
