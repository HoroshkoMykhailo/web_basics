from fastapi import FastAPI
from .database import Base, engine
from .modules.authors import routers as authors
from .modules.publishers import routers as publishers
from .modules.bookstores import routers as bookstores
from .modules.books import routers as books
from .modules.author_book import routers as author_book

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library API")

app.include_router(authors.router)
app.include_router(publishers.router)
app.include_router(bookstores.router)
app.include_router(books.router)
app.include_router(author_book.router)