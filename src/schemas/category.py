""" Category Schema """

from typing import List
from src.models.base import CamelModel
from src.schemas.product import ProductOut

class CategoryIn(CamelModel):
    """ Category Camel Model """
    name: str


class CategoryOut(CategoryIn):
    """ Category Camel Model """
    id: int
    products: List[ProductOut] = []
