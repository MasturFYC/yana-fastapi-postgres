''' Category Dal '''
from typing import List
from sqlalchemy import select, update, delete
from sqlalchemy.orm import joinedload, Session
from src.models.category import Category
from src.schemas.category import CategoryIn


class CategoryDal():
    ''' load category dal '''

    def __init__(self, session: Session):
        self.session = session

    async def category_get_all(self, skip: int = 0, take: int = 20) -> List[Category]:
        ''' load all categories '''
        query = await self.session\
            .execute(select(Category)
                     .offset(skip).limit(take).order_by(Category.name))
        return query.scalars().fetchall()

    async def category_get_one(self, pid: int) -> Category:
        ''' load one category by id '''
        query = await self.session.execute(select(Category)
                                           .options(joinedload(Category.products))
                                           .where(Category.id == pid))
        return query.scalars().first()

    async def category_insert(self, payload: CategoryIn) -> Category:
        ''' insert new category '''
        new_category = Category(name=payload.name)
        self.session.add(new_category)
        await self.session.flush()
        return new_category

    async def category_update(self, pid: int, payload: CategoryIn) -> Category:
        ''' update one category by id '''
        query = update(Category).where(Category.id == pid)\
            .values(name=payload.name).returning(Category)
        query.execution_options(synchronize_session="fetch")
        res = await self.session.execute(query)
        tup = res.fetchone()
        await self.session.commit()
        return tup

    async def category_delete(self, pid: int) -> int:
        ''' delete category by id '''
        query = delete(Category).where(
            Category.id == pid).returning(Category.id)
        res = await self.session.execute(query)
        tup = res.fetchone()
        await self.session.commit()
        return {'id': tup.id}
