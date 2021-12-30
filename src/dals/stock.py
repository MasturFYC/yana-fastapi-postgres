''' Stock Dal '''
from typing import List
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from src.models.stock import Stock
from src.schemas.stock import StockIn


class StockDal():
    ''' load Stock dal '''

    def __init__(self, session: Session):
        self.session = session

    async def stock_get_all(self, skip: int = 0, take: int = 20) -> List[Stock]:
        ''' load all Stocks '''
        query = await self.session\
            .execute(select(Stock)
                     .offset(skip).limit(take).order_by(Stock.stock_num))
        return query.scalars().fetchall()

    async def stock_get_one(self, pid: int) -> Stock:
        ''' load one Stock by id '''
        query = await self.session.execute(select(Stock)
                                           .where(Stock.id == pid))
        return query.scalars().first()

    async def stock_insert(self, payload: StockIn) -> Stock:
        ''' insert new Stock '''
        new_stock = Stock(supplier_id=payload.supplier_id,
                          stock_num=payload.stock_num,
                          cash=payload.cash,
                          payments=payload.payments,
                          remain_payment=payload.remain_payment,
                          created_at=payload.stock_date)
        self.session.add(new_stock)
        await self.session.flush()
        return new_stock

    async def stock_update(self, pid: int, payload: StockIn) -> Stock:
        ''' update one Stock by id '''
        query = update(Stock).where(Stock.id == pid)\
            .values(supplier_id=payload.supplier_id,
                    stock_num=payload.stock_num,
                    cash=payload.cash,
                    payments=payload.payments,
                    remain_payment=payload.remain_payment,
                    created_at=payload.stock_date)
        res = await self.session.execute(query)
        tup = res.fetchone()
        await self.session.commit()
        return tup

    async def stock_delete(self, pid: int) -> int:
        ''' delete Stock by id '''
        query = delete(Stock).where(
            Stock.id == pid).returning(Stock.id)
        res = await self.session.execute(query)
        tup = res.fetchone()
        await self.session.commit()
        return {'id': tup.id}
