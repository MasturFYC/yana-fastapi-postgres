""" base model """

import os
import urllib
import databases
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
import humps

HOST_SERVER = os.environ.get('host_server', 'localhost')
DB_SERVER_PORT = urllib.parse.quote_plus(
    str(os.environ.get('db_server_port', '5432')))
DB_NAME = os.environ.get('database_name', 'sip')
DB_USER_NAME = urllib.parse.quote_plus(
    str(os.environ.get('db_username', 'postgres')))
DB_PASSWORD = urllib.parse.quote_plus(
    str(os.environ.get('db_password', 't2z00a8y')))
SSL_MODEL = urllib.parse.quote_plus(str(os.environ.get('ssl_mode', 'prefer')))

# DATABASE_URL = 'postgresql+asyncpg://{}:{}@{}:{}/{}?
# sslmode={}&prepared_statement_cache_size=500'.format(
DATABASE_URL = 'postgresql+asyncpg://{}:{}@{}:{}/{}?prepared_statement_cache_size=500'.format(
    DB_USER_NAME, DB_PASSWORD, HOST_SERVER, DB_SERVER_PORT, DB_NAME)

engine = create_async_engine(
    DATABASE_URL, pool_size=3, max_overflow=0, echo=True,)

Base = declarative_base()

db_session = sessionmaker(engine, class_=AsyncSession,
                          expire_on_commit=False, autocommit=False)
database = databases.Database(DATABASE_URL)


def to_camel(string):
    return humps.camelize(string)


class CamelModel(BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
        orm_mode = True
