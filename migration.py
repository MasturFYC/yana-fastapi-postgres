import asyncio

from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.orm.session import sessionmaker

from src.models.base import engine, Base, db_session
from src.models.category import Category
from src.models.product import Product
from src.models.unit import Unit
from src.models.firststock import FirstStock
from src.models.supplier import Supplier
from src.models.stock import Stock
from src.models.stockdetail import StockDetail


async def async_main(AsyncronEngine: AsyncEngine, AsyncronSession: sessionmaker):

    async with AsyncronEngine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncronSession() as session:

        async with session.begin():
            await conn.run_sync(Category.__table__.create(bind=engine, checkfirst=True))
            await AsyncronSession.commit()
            await conn.run_sync(Product.__table__.create(bind=engine, checkfirst=True))
            await AsyncronSession.commit()
            await conn.run_sync(Unit.__table__.create(bind=engine, checkfirst=True))
            await AsyncronSession.commit()
            await conn.run_sync(FirstStock.__table__.create(bind=engine, checkfirst=True))
            await AsyncronSession.commit()
            await conn.run_sync(Supplier.__table__.create(bind=engine, checkfirst=True))
            await AsyncronSession.commit()
            await conn.run_sync(Stock.__table__.create(bind=engine, checkfirst=True))
            await AsyncronSession.commit()
            await conn.run_sync(StockDetail.__table__.create(bind=engine, checkfirst=True))
            await AsyncronSession.commit()

    await AsyncronEngine.dispose()

asyncio.run(async_main(engine, db_session))
