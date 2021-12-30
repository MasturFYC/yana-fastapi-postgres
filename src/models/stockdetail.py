"""
Tabel Stock Details with model
"""

from sqlalchemy import Sequence, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Numeric
from src.models.base import Base


class StockDetail(Base):
    """ Tabel Stock Detail base model """
    __tablename__ = 'stock_details'

    stock_id = Column(Integer,
                      ForeignKey("stocks.id", ondelete='CASCADE'),
                      index=True, nullable=False)
    id = Column(Integer, Sequence('order_details_id_seq'),
                primary_key=True)
    product_id = Column(Integer,
                        ForeignKey("products.id"),
                        nullable=False, index=True)
    unit_id = Column(Integer,
                     ForeignKey("units.id"),
                     nullable=False, index=True)
    qty = Column(Numeric(10, 2), nullable=False, default=0)
    content = Column(Numeric(8, 2), nullable=False, default=0)
    unit_name = Column(String(6), nullable=False)
    real_qty = Column(Numeric(10, 2), nullable=False, default=0)
    price = Column(Numeric(12, 2), nullable=False, default=0)
    discount = Column(Numeric(12, 2), nullable=False, default=0)
    subtotal = Column(Numeric(12, 2), nullable=False, default=0)

    stock = relationship("src.models.stock.Stock",
                         back_populates='stock_details')
    product = relationship("src.models.product.Product",
                           back_populates='stock_details')
    unit = relationship("src.models.unit.Unit", back_populates='stock_details')

    def __init__(self, **kwargs):
        valid_keys = ["stock_id", "product_id", "unit_id", "qty",
                      "content", "unit_name", "real_qty", "price",
                      "discount", "subtotal"]
        for key in valid_keys:
            setattr(self, key, kwargs.get(key))
