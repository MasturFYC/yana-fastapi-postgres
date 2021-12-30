
"""
Tabel unit with model
"""

from sqlalchemy import Sequence, Column, Integer, String, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import UniqueConstraint
from src.models.base import Base

# from sqlalchemy.sql.schema import PrimaryKeyConstraint


class Unit(Base):
    """ Tabel units base model """
    __tablename__ = 'units'
    __table_args__ = (
        UniqueConstraint(
            'product_id',
            'name',
            name='uq_unit_name'
        ),
    )

    product_id = Column(Integer, ForeignKey(
        "products.id", ondelete='CASCADE'), index=True, nullable=False)
    id = Column(Integer, Sequence('units_id_seq'), primary_key=True)
    name = Column(String(6), nullable=False, index=True)
    content = Column(Numeric(8, 2), nullable=False, default=0)
    buy_price = Column(Numeric(12, 2), nullable=False, default=0)
    margin = Column(Numeric(5, 4), nullable=False, default=0)
    price = Column(Numeric(12, 2), nullable=False, default=0)
    is_default = Column(Boolean, nullable=False, default=False)
    product = relationship("src.models.product.Product",
                           back_populates="units")
    stock_details = relationship("src.models.stockdetail.StockDetail",
                                 back_populates="unit")

    def __init__(self, **kwargs):
        valid_keys = ["product_id", "name", "content",
                      "price", "buy_price", "margin", "is_default"]
        for key in valid_keys:
            setattr(self, key, kwargs.get(key))
