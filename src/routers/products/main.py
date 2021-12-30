""" Product Router """

from typing import List
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from src.models.base import db_session
from src.schemas.product import ProductIn, ProductOut
from src.dals.product import ProductDal


async def __get_current_dal():
    ''' middleware '''
    async with db_session() as session:
        async with session.begin():
            yield ProductDal(session)

ROUTER = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"products": "Not found"}},
)


@ROUTER.get("/", response_model=List[ProductOut], status_code=status.HTTP_200_OK)
async def read_products(skip: int = 0, take: int = 20,
                        dal: ProductDal = Depends(__get_current_dal)):
    """ Get all products """
    res = await dal.product_get_all(skip, take)
    if res is None:
        raise HTTPException(status_code=404, detail="Product is empty")
    return [row.__dict__ for row in res]


@ROUTER.get("/{pid}/", response_model=ProductOut, status_code=status.HTTP_200_OK)
async def read_product(pid: int,
                       dal: ProductDal = Depends(__get_current_dal)):
    """ Get all product by id """
    res = await dal.product_get_one(pid)
    if res is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return res # .__dict__


@ROUTER.post("/", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
async def create_products(payload: ProductIn,
                          dal: ProductDal = Depends(__get_current_dal)):
    """ Create product """
    res = dal.product_insert(payload)
    if res is None:
        raise HTTPException(status_code=500, detail="Product name exist")

    return res.__dict__


@ROUTER.put("/{pid}/", response_model=ProductOut, status_code=status.HTTP_200_OK)
async def update_product(pid: int, payload: ProductIn,
                         dal: ProductDal = Depends(__get_current_dal)):
    """ Update product by id """
    res = await dal.product_update(pid, payload)

    if res is None:
        raise HTTPException(status_code=500, detail="Product name exist")

    return res  # //.__dict__


@ROUTER.delete("/{pid}/", status_code=status.HTTP_200_OK)
async def delete_product(pid: int,
                         dal: ProductDal = Depends(__get_current_dal)):
    """ Delete product by id """
    return await dal.product_delete(pid)
