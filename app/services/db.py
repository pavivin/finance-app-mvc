from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
from settings import DB_CONNECTION_STRING

async def init_db():
    await Tortoise.generate_schemas()


async def connect_db(app: FastAPI):
    await Tortoise.init(db_url=DB_CONNECTION_STRING, modules={'models': ['models']})
    register_tortoise(
        app,
        db_url=DB_CONNECTION_STRING,
        modules={"models": ["models.users"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )
