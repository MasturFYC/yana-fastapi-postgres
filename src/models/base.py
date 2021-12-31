""" base model """

import os
import urllib
import databases
from env_loader import load_env
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
import humps

env = load_env(dir_path='./', auto_parse=True)

PORT = str(os.environ.get('DB_PORT'))
HOST_SERVER = os.environ.get('HOST_SERVER')
DB_SERVER_PORT = urllib.parse.quote_plus(str(PORT))
DB_NAME = os.environ.get('DB_NAME')
DB_USER_NAME = urllib.parse.quote_plus(
    str(os.environ.get('DB_USERNAME')))
DB_PASSWORD = urllib.parse.quote_plus(
    str(os.environ.get('DB_PASSWORD')))
SSL_MODEL = urllib.parse.quote_plus(str(os.environ.get('SSL_MODE')))

# DATABASE_URL = 'postgresql+asyncpg://{}:{}@{}:{}/{}?
# sslmode={}&prepared_statement_cache_size=500'.format(
DATABASE_URL = "postgresql+asyncpg://{}:{}@{}:{}/{}?prepared_statement_cache_size=500".format(
    DB_USER_NAME, DB_PASSWORD, HOST_SERVER, DB_SERVER_PORT, DB_NAME)

engine = create_async_engine(
    DATABASE_URL, pool_size=3, max_overflow=0, echo=True,)

Base = declarative_base()

db_session = sessionmaker(engine, class_=AsyncSession,
                          expire_on_commit=False, autocommit=False)
database = databases.Database(DATABASE_URL)


def to_camel(string):
    """ convert field to camel case """
    return humps.camelize(string)


class CamelModel(BaseModel):
    """ convert field to camel case """
    class Config:
        """ convert field to camel case """
        alias_generator = to_camel
        allow_population_by_field_name = True
        orm_mode = True
