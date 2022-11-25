"""
Basic App to test if your pod connects to DB and Redis
"""
__version__ = "0.1"

import os
from fastapi import FastAPI
import sqlalchemy as db
import redis

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/db-connect")
async def db_connect():
    engine = db.create_engine(os.environ.get("DB_URI"))
    engine.connect()
    return {"message": "Connected to DB"}

@app.get("/redis-connect")
async def redist_connect():
    instance= redis.StrictRedis(host=os.environ.get("REDIS_HOST"), port=6379, db=0, password="devpass")
    instance.set("hello","world")
    return {"message": "Connected to Redis"}


