"""
Tabel Stock with model
"""

from datetime import datetime
from sqlalchemy import Sequence, DateTime, Column, Integer, SmallInteger, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Numeric
from src.models.base import Base


class Stock(Base):
    """ Tabel Stock base model """
    __tablename__ = 'stocks'

    id = Column(Integer, Sequence('orders_id_seq'), primary_key=True)
    supplier_id = Column(SmallInteger, ForeignKey(
        "suppliers.id"), index=True, nullable=False)
    stock_num = Column(String(50), nullable=False, unique=True)
    stock_date = Column(DateTime(timezone=True),
                        nullable=False, default=datetime.utcnow())
    total = Column(Numeric(12, 2), nullable=False, default=0)
    cash = Column(Numeric(12, 2), nullable=False, default=0)
    payments = Column(Numeric(12, 2), nullable=False, default=0)
    remain_payment = Column(Numeric(12, 2), nullable=False, default=0)
    descriptions = Column(String(128), nullable=True)

    supplier = relationship(
        "src.models.supplier.Supplier", back_populates='stocks')

    stock_details = relationship("src.models.stockdetail.StockDetail",
                                 back_populates="stock")

    def __init__(self, **kwargs):
        valid_keys = ["supplier_id", "stock_num", "stock_date", "total", "cash",
                      "payments", "remain_payment", "descriptions"]
        for key in valid_keys:
            setattr(self, key, kwargs.get(key))
