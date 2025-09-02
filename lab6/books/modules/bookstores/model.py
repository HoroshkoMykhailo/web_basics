from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ...database import Base

class Bookstore(Base):
    __tablename__ = "bookstores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)

    books = relationship("Book", back_populates="bookstore")
