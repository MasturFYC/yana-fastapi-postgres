""" Stock Detail Schema """

from src.models.base import CamelModel


class StockDetailIn(CamelModel):
    """ router parameter in """
    stock_id: int
    product_id: int
    unit_id: int
    qty: float
    content: float
    unit_name: str
    price: float
    discount: float


class StockDetailOut(StockDetailIn):
    """ router parameter out """
    id: int
    real_qty: float
    subtotal: float
