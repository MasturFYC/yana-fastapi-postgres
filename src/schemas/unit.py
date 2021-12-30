""" Unit Schema """

from src.models.base import CamelModel


class UnitIn(CamelModel):
    """ unit Camel Model """
    product_id: int
    name: str
    content: float
    buy_price: float
    margin: float
    price: str
    is_default: bool


class UnitOut(UnitIn):
    """ unit camel Model """
    id: int
