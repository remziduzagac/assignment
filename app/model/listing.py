from sqlalchemy import Column, Integer, String, Float

from app.core.db.base import Base


class Listing(Base):
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    address = Column(String(512), nullable=True)
    price = Column(Float(), nullable=True)
