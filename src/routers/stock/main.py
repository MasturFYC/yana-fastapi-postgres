""" Product Router """

from typing import List
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from src.models.base import db_session
from src.schemas.stock import StockIn, StockOut
from src.dals.stock import StockDal


async def __get_current_dal():
    ''' middleware '''
    async with db_session() as session:
        async with session.begin():
            yield StockDal(session)

ROUTER = APIRouter(
    prefix="/stocks",
    tags=["stocks"],
    responses={404: {"stocks": "Not found"}},
)


@ROUTER.get("/", response_model=List[StockOut], status_code=status.HTTP_200_OK)
async def read_stocks(skip: int = 0, take: int = 20,
                      dal: StockDal = Depends(__get_current_dal)):
    """ Get all stocks """
    res = await dal.stock_get_all(skip, take)
    if res is None:
        raise HTTPException(status_code=404, detail="Product is empty")
    return [row.__dict__ for row in res]


@ROUTER.get("/{pid}/", response_model=StockOut, status_code=status.HTTP_200_OK)
async def read_stock(pid: int,
                     dal: StockDal = Depends(__get_current_dal)):
    """ Get all product by id """
    res = await dal.stock_get_one(pid)
    if res is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return res  # .__dict__


@ROUTER.post("/", response_model=StockOut, status_code=status.HTTP_201_CREATED)
async def create_stock(payload: StockIn,
                       dal: StockDal = Depends(__get_current_dal)):
    """ Create product """
    res = dal.stock_insert(payload)
    if res is None:
        raise HTTPException(status_code=500, detail="Product name exist")

    return res.__dict__


@ROUTER.put("/{pid}/", response_model=StockOut, status_code=status.HTTP_200_OK)
async def update_stock(pid: int, payload: StockIn,
                       dal: StockDal = Depends(__get_current_dal)):
    """ Update product by id """
    res = await dal.stock_update(pid, payload)

    if res is None:
        raise HTTPException(status_code=500, detail="Product name exist")

    return res  # //.__dict__


@ROUTER.delete("/{pid}/", status_code=status.HTTP_200_OK)
async def delete_stock(pid: int,
                       dal: StockDal = Depends(__get_current_dal)):
    """ Delete product by id """
    return await dal.stock_delete(pid)
