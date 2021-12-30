""" Stock Schema """

from datetime import datetime
from pydantic import validator
from src.models.base import CamelModel

class StockIn(CamelModel):
    """ router parameter in """
    supplier_id: int
    stock_num: str
    cash: float
    payments: float
    remain_payment: float
    stock_date: datetime = None

    @classmethod
    @validator("stock_date", pre=True)
    def stock_date_validate(cls, value) -> None:
        ''' DOC STRING '''
        return datetime.fromtimestamp(value)


class StockOut(StockIn):
    """ router parameter out """
    id: int
    # updated_at: datetime = None

    # @classmethod
    # @validator("updated_at", pre=True)
    # def updated_at_validate(cls, value) -> None:
    #    ''' DOC STRING '''
    #    return datetime.fromtimestamp(value)
