""" User Schema """

from pydantic import BaseModel
from typing import Optional

class UserIn(BaseModel):
    """ router parameter in """
    name: str
    email: str
    password: str
    role: str


class UserOut(UserIn):
    """ router parameter out """
    id: int

class UserLogin(BaseModel):
    email: str
    password: str

class UserGet(BaseModel):
    id: int
    name: str
    email: str
    role: str
    token: Optional[str] = None
