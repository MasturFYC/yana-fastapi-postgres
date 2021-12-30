"""
Tabel Supplier with model
"""

from sqlalchemy import Sequence, Column, SmallInteger, String
from sqlalchemy.orm import relationship
from src.models.base import Base


class Supplier(Base):
    """ Tabel Supplier base model """
    __tablename__ = 'suppliers'

    id = Column(SmallInteger, Sequence('suppliers_id_seq'), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    sales_name = Column(String(50), nullable=True)
    street = Column(String(128), nullable=True)
    city = Column(String(50), nullable=True)
    phone = Column(String(25), nullable=True)
    cell = Column(String(25), nullable=True)
    # zip = Column(String(8), nullable=True)
    email = Column(String(128), nullable=True)
    
    stocks = relationship("src.models.stock.Stock", back_populates="supplier")

    def __init__(self, **kwargs):
        valid_keys = ["name", "sales_name", "street", "city",
                      "phone", "cell", "email"]
        for key in valid_keys:
            setattr(self, key, kwargs.get(key))
