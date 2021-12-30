''' Supplier Dal '''
from typing import List
from sqlalchemy import select, update, delete
from sqlalchemy.orm import  Session
from src.models.supplier import Supplier
from src.schemas.supplier import SupplierIn


class SupplierDal():
    ''' load Supplier dal '''

    def __init__(self, session: Session):
        self.session = session

    async def supplier_get_all(self, skip: int = 0, take: int = 20) -> List[Supplier]:
        ''' load all Suppliers '''
        query = await self.session\
            .execute(select(Supplier)
                     .offset(skip).limit(take).order_by(Supplier.name))
        return query.scalars().fetchall()

    async def supplier_get_one(self, pid: int) -> Supplier:
        ''' load one Supplier by id '''
        query = await self.session.execute(select(Supplier)
                                           .where(Supplier.id == pid))
        return query.scalars().first()

    async def supplier_insert(self, payload: SupplierIn) -> Supplier:
        ''' insert new Supplier '''
        new_supplier = Supplier(name=payload.name, sales_name=payload.sales_name,
                                street=payload.street, city=payload.city, phone=payload.phone,
                                cell=payload.cell, zip=payload.zip, email=payload.email)
        self.session.add(new_supplier)
        await self.session.flush()
        return new_supplier

    async def supplier_update(self, pid: int, payload: SupplierIn) -> Supplier:
        ''' update one Supplier by id '''
        query = update(Supplier).where(Supplier.id == pid)\
            .values(name=payload.name, sales_name=payload.sales_name,
                    street=payload.street, city=payload.city, phone=payload.phone,
                    cell=payload.cell, zip=payload.zip, email=payload.email).returning(Supplier)
        query.execution_options(synchronize_session="fetch")
        res = await self.session.execute(query)
        tup = res.fetchone()
        await self.session.commit()
        return tup

    async def supplier_delete(self, pid: int) -> int:
        ''' delete Supplier by id '''
        query = delete(Supplier).where(
            Supplier.id == pid).returning(Supplier.id)
        res = await self.session.execute(query)
        tup = res.fetchone()
        await self.session.commit()
        return {'id': tup.id}
