"""
Tabel category with model
"""

from datetime import datetime, timezone
from sqlalchemy import Sequence, Column, SmallInteger, String, DateTime
from sqlalchemy.orm import relationship
from src.models.base import Base


class Category(Base): # pylint: disable = too-few-public-methods
    """ Tabel categories base model """

    __tablename__ = 'categories'

    id = Column(SmallInteger, Sequence("categories_id_seq"), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.now(timezone.utc))

    products = relationship("src.models.product.Product",
                            back_populates="category")

    def __init__(self, **kwargs):
        valid_keys = ["name", "created_at", "updated_at"]
        for key in valid_keys:
            setattr(self, key, kwargs.get(key))
