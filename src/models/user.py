"""
Tabel User with model
"""

from sqlalchemy import Sequence, Column, SmallInteger, String
from src.models.base import Base


class User(Base):
    """ Tabel Users base model """
    __tablename__ = 'users'

    id = Column(SmallInteger, Sequence('users_id_seq'), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    role = Column(String(25), nullable=False)
    
    def __init__(self, **kwargs):
        valid_keys = ["name", "email", "password", "role"]
        for key in valid_keys:
            setattr(self, key, kwargs.get(key))

