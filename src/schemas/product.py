""" Product Schema """

from typing import Optional
from src.models.base import CamelModel

class ProductIn(CamelModel):
    """ product Camel Model """
    name: str
    spec: Optional[str] = None  # pylint: disable=unsubscriptable-object
    price: float = 0
    stock: float = 0
    first_stock: float = 0
    unit: str
    update_notif: bool = False
    category_id: int


class ProductOut(ProductIn):
    """ product Camel Model """
    id: int
