# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using FastAPI by creating endpoints for managing a simple book collection and practicing request handling, data validation, and HTTP methods.

## 📝 Tasks

### 🛠️ Create the FastAPI application

#### Description
Create a FastAPI application and define a Pydantic model for a `Book`. Add the first endpoint to return a welcome message and a second endpoint to retrieve all books.

#### Requirements
Completed program should:

- Define a `Book` model using `pydantic.BaseModel` with fields `id`, `title`, `author`, and `year`.
- Create a `FastAPI()` app instance.
- Add a `GET /` endpoint that returns a simple welcome message.
- Add a `GET /books` endpoint that returns a list of books.
- Use an in-memory list or dictionary to store book objects.

### 🛠️ Implement CRUD endpoints

#### Description
Add endpoints to create, read, update, and delete books. Use path parameters, request bodies, and proper HTTP status codes.

#### Requirements
Completed program should:

- Add a `GET /books/{book_id}` endpoint to retrieve a single book by its ID.
- Add a `POST /books` endpoint that accepts a `Book` request body and adds a new book.
- Add a `PUT /books/{book_id}` endpoint that updates an existing book with new fields.
- Add a `DELETE /books/{book_id}` endpoint that removes a book.
- Return `404` if a requested book does not exist.

### 🛠️ Add filtering and validation

#### Description
Enhance the API with optional query parameters and input validation to make the service more robust and user-friendly.

#### Requirements
Completed program should:

- Add an optional query parameter to `GET /books` so users can filter books by author or year.
- Use a Pydantic model or `Field` definitions to validate book data.
- Return a meaningful JSON response for invalid requests.
- Include example usage for filtering and request bodies in the README.
