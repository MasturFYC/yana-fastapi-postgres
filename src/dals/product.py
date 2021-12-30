''' Product Dal '''
from typing import List
from sqlalchemy import select, update, delete
from sqlalchemy.orm import joinedload, Session
from src.models.product import Product
from src.schemas.product import ProductIn


class ProductDal():
    ''' load product dal '''

    def __init__(self, session: Session):
        self.session = session

    async def product_get_all(self, skip: int = 0, take: int = 20) -> List[Product]:
        ''' load all products '''
        query = await self.session\
            .execute(select(Product)
                     .offset(skip).limit(take).order_by(Product.name))
        return query.scalars().fetchall()

    async def product_get_one(self, pid: int) -> Product:
        ''' load one Product by id '''
        query = await self.session.execute(select(Product)
                                           .options(joinedload(Product.units))
                                           .where(Product.id == pid))
        return query.scalars().first()

    async def product_insert(self, payload: ProductIn) -> Product:
        ''' insert new Product '''
        new_product = Product(name=payload.name,
                              spec=payload.spec,
                              price=payload.price,
                              stock=payload.stock,
                              first_stock=payload.first_stock,
                              unit=payload.unit,
                              update_notif=payload.update_notif,
                              category_id=payload.category_id)
        self.session.add(new_product)
        await self.session.flush()
        return new_product

    async def product_update(self, pid: int, payload: ProductIn) -> Product:
        ''' update one Product by id '''
        query = update(Product).where(Product.id == pid)\
            .values(name=payload.name,
                    spec=payload.spec,
                    price=payload.price,
                    stock=payload.stock,
                    first_stock=payload.first_stock,
                    unit=payload.unit,
                    update_notif=payload.update_notif,
                    category_id=payload.category_id).returning(Product)
        query.execution_options(synchronize_session="fetch")
        res = await self.session.execute(query)
        tup = res.fetchone()
        await self.session.commit()
        return tup

    async def product_delete(self, pid: int) -> int:
        ''' delete Product by id '''
        query = delete(Product).where(
            Product.id == pid).returning(Product.id)
        res = await self.session.execute(query)
        tup = res.fetchone()
        await self.session.commit()
        return {'id': tup.id}
