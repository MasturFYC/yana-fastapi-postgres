"""
Tabel product with model
"""

from sqlalchemy import Sequence, Column, SmallInteger, Integer, String, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base import Base


class Product(Base):  # pylint: disable=too-few-public-methods
    """ Tabel product base model """
    __tablename__ = 'products'

    id = Column(Integer, Sequence('products_id_seq'),
                primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    spec = Column(String(128), nullable=True)
    price = Column(Numeric(12, 2), nullable=False, default=0)
    stock = Column(Numeric(10, 2), nullable=False, default=0)
    first_stock = Column(Numeric(10, 2), nullable=False, default=0)
    unit = Column(String(6), nullable=False)
    update_notif = Column(Boolean, nullable=False, default=False)
    # is_active = Column(Boolean, nullable=False, default=False)
    category_id = Column(SmallInteger, ForeignKey("categories.id"))

    category = relationship(
        "src.models.category.Category", back_populates="products")
    units = relationship("src.models.unit.Unit",
                         back_populates="product")
    stock_details = relationship("src.models.stockdetail.StockDetail",
                                 back_populates="product")

    def __init__(self, **kwargs):
        valid_keys = ["name", "spec", "price", "stock",
                      "first_stock", "unit", "category_id"]
        for key in valid_keys:
            setattr(self, key, kwargs.get(key))
