""" StockDetail Router """

from typing import List
from fastapi import APIRouter, status
from sqlalchemy import select, update, insert, delete
from src.models.base import database
from src.models.stockdetail import StockDetail
from src.schemas.stockdetail import StockDetailIn, StockDetailOut


ROUTER = APIRouter(
    prefix="/stockdetails",
    tags=["stockdetails"],
    responses={404: {"Stock Detail": "Not found"}},
)


@ROUTER.get("/stocks/{stock_id}", response_model=List[StockDetailOut],
            status_code=status.HTTP_200_OK)
async def read_stock_details(stock_id: int):
    """ Get stock details by stock """
    query = select(StockDetail).where(StockDetail.stock_id == stock_id)
    return await database.fetch_all(query)


@ROUTER.get("/{det_id}/", response_model=StockDetailOut, status_code=status.HTTP_200_OK)
async def read_stock_detail(det_id: int):
    """ Get stock detail by id """
    query = select(StockDetail).where(StockDetail.id == det_id)
    return await database.fetch_one(query)


@ROUTER.post("/", response_model=StockDetailOut, status_code=status.HTTP_201_CREATED)
async def create_stock_detail(detail: StockDetailIn):
    """ Create stock detail """
    query = insert(StockDetail) \
        .values(stock_id=detail.stock_id, product_id=detail.product_id,
                unit_id=detail.unit_id, qty=detail.qty, content=detail.content,
                unit_name=detail.unit_name, price=detail.price, discount=detail.discount)
    last_record_id = await database.execute(query)
    return {**detail.dict(), "id": last_record_id}


@ROUTER.put("/{det_id}/", response_model=StockDetailOut, status_code=status.HTTP_200_OK)
async def update_stock_detail(det_id: int, detail: StockDetailIn):
    """ Update stock detail by id """
    query = update(StockDetail).where(StockDetail.id == det_id) \
        .values(stock_id=detail.stock_id, product_id=detail.product_id,
                unit_id=detail.unit_id, qty=detail.qty, content=detail.content,
                unit_name=detail.unit_name, price=detail.price, discount=detail.discount)
    await database.execute(query)
    return {**detail.dict(), "id": det_id}


@ROUTER.delete("/{det_id}/", status_code=status.HTTP_200_OK)
async def delete_stock_detail(det_id: int):
    """ Delete stock detail by id """
    query = delete(StockDetail).where(StockDetail.id == det_id)
    await database.execute(query)
    return {"message": "Note with id: {} deleted successfully!".format(det_id)}
