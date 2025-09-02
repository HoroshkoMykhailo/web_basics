from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ...database import Base

class Publisher(Base):
    __tablename__ = "publishers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)

    books = relationship("Book", back_populates="publisher")
