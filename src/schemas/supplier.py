""" Supplier Schema """

from typing import Optional
from src.models.base import CamelModel

class SupplierIn(CamelModel):
    """ router parameter in """
    name: str
    sales_name: Optional[str] # = None  # pylint: disable=unsubscriptable-object
    street: Optional[str] # = None  # pylint: disable=unsubscriptable-object
    city: Optional[str] # = None  # pylint: disable=unsubscriptable-object
    phone: Optional[str] # = None  # pylint: disable=unsubscriptable-object
    cell: Optional[str] # = None  # pylint: disable=unsubscriptable-object
    email: Optional[str] # = None  # pylint: disable=unsubscriptable-object


class SupplierOut(SupplierIn):
    """ router parameter out """
    id: int
