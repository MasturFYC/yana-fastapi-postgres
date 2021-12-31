""" Main App """
import os
import multiprocessing
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.models.base import Base, database, engine
from src.routers.category import main as category_router
from src.routers.product import main as product_router
from src.routers.unit import main as unit_router
from src.routers.supplier import main as supplier_router
from src.routers.stock import main as stock_router
from src.routers.stockdetail import main as stockdetail_router
from src.routers.user import main as user_router

app = FastAPI(title=os.environ.get("APP_TITLE"))
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    """ Start endpoint """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    """ Shutdown endpoint """
    await database.disconnect()


@app.get("/")
async def root():
    """ Goto root """
    return {"message": "Welcome to Yoga Fastapi Postgresql"}

app.include_router(category_router.ROUTER)
app.include_router(product_router.ROUTER)
app.include_router(unit_router.ROUTER)
app.include_router(supplier_router.ROUTER)
app.include_router(stock_router.ROUTER)
app.include_router(stockdetail_router.ROUTER)
app.include_router(user_router.ROUTER)

if __name__ == "__main__":
    multiprocessing.freeze_support()
    uvicorn.run("app:app", host="127.0.0.1", port=8000,
                reload=True, workers=1, debug=True)
