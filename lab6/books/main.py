from fastapi import FastAPI
from .database import Base, engine
from .routers import authors, publishers, bookstores, books

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library API")

app.include_router(authors.router)
app.include_router(publishers.router)
app.include_router(bookstores.router)
app.include_router(books.router)