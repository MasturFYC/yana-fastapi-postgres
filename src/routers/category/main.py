""" Category Router """
from typing import List
from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from src.dals.category import CategoryDal
from src.models.base import db_session
from src.schemas.category import CategoryIn, CategoryOut


async def _get_current_dal():
    ''' middleware '''
    async with db_session() as session:
        async with session.begin():
            yield CategoryDal(session)


ROUTER = APIRouter(
    prefix="/categories",
    tags=["categories"],
    responses={404: {"categories": "Not found"}},
)


@ROUTER.get("/", response_model=List[CategoryOut],
            status_code=status.HTTP_200_OK)
async def read_categories(skip: int = 0, take: int = 20,
                          dal: CategoryDal = Depends(_get_current_dal)):
    """ Get all categories """
    res = await dal.category_get_all(skip, take)
    if res is None:
        raise HTTPException(status_code=404, detail="Category is empty")
    return [row.__dict__ for row in res]


@ROUTER.get("/{pid}/",
            response_model=CategoryOut,
            status_code=status.HTTP_200_OK)
async def read_category(pid: int, dal: CategoryDal = Depends(_get_current_dal)):
    """ Get one category """
    res = await dal.category_get_one(pid)
    if res is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return res.__dict__


@ ROUTER.post("/", response_model=CategoryOut, status_code=status.HTTP_201_CREATED)
async def create_category(payload: CategoryIn,
                          dal: CategoryDal = Depends(_get_current_dal)):
    """ create new category """
    res = await dal.category_insert(payload)

    if res is None:
        raise HTTPException(status_code=500, detail="Category name exist")

    return res.__dict__


@ ROUTER.put("/{pid}/", response_model=CategoryOut, status_code=status.HTTP_200_OK)
async def update_category(pid: int, payload: CategoryIn,
                          dal: CategoryDal = Depends(_get_current_dal)):
    """ Update category by id """

    res = await dal.category_update(pid, payload)

    if res is None:
        raise HTTPException(status_code=500, detail="Category name exist")

    return res  # //.__dict__


@ ROUTER.delete("/{pid}/", status_code=status.HTTP_200_OK)
async def delete_category(pid: int, dal: CategoryDal = Depends(_get_current_dal)):
    """ Delete category by id """
    return await dal.category_delete(pid)
