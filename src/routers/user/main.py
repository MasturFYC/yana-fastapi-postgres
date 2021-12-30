""" User Router """

from typing import List
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from src.models.base import db_session
from src.schemas.user import UserIn, UserOut, UserLogin, UserGet
from src.dals.user import user_dal


async def __get_current_dal():
    ''' middleware '''
    async with db_session() as session:
        async with session.begin():
            yield user_dal(session)

ROUTER = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"User": "Not found"}},
)

"""
@ROUTER.get("/", response_model=List[UserOut], status_code=status.HTTP_200_OK)
async def read_users(dal: user_dal = Depends(__get_current_dal)):
    "" Get all users ""
    res = await dal.user_get_all()
    if res is None:
        raise HTTPException(status_code=404, detail="User is empty")
    
    return [row.__dict__ for row in res]

@ROUTER.get("/{pid}/", response_model=UserOut, status_code=status.HTTP_200_OK)
async def read_user(pid: int, dal: user_dal = Depends(__get_current_dal)):
    "" Get all user by id ""
    res = await dal.user_get_one(pid)
    print(res)
    if res is None:
        raise HTTPException(status_code=404, detail="User not found")

    return res.__dict__

"""

@ROUTER.post("/me/", response_model=UserGet, status_code=status.HTTP_200_OK)
async def read_user(payload: UserLogin, dal: user_dal = Depends(__get_current_dal)):
    """ Get all user by id """
    print(payload)
    res = await dal.user_get_user(payload)
    if res is None:
        raise HTTPException(status_code=404, detail="User not found")

    return res.__dict__



@ROUTER.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_users(payload: UserIn, dal: user_dal = Depends(__get_current_dal)):
    """ Create user """
    res = dal.user_insert(payload)
    if res is None:
        raise HTTPException(status_code=500, detail="User name exist")

    return res.__dict__


@ROUTER.put("/{pid}/", response_model=UserOut, status_code=status.HTTP_200_OK)
async def update_user(pid: int, payload: UserIn, dal: user_dal = Depends(__get_current_dal)):
    """ Update user by id """
    res = await dal.user_update(pid, payload)

    if res is None:
        raise HTTPException(status_code=500, detail="User name exist")

    return res.__dict__

"""
@ROUTER.delete("/{pid}/", status_code=status.HTTP_200_OK)
async def delete_user(pid: int, dal: user_dal = Depends(__get_current_dal)):
    "" Delete user by id ""
    
    return await dal.user_delete(pid)
"""
