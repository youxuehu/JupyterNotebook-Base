# -*- coding:utf-8 -*-
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """
    http://127.0.0.1:8000/
    :return:
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    """
    http://127.0.0.1:8000/items/1?q=jack
    :param item_id:
    :param q:
    :return:
    """
    return {"item_id": item_id, "q": q}


"""
http://127.0.0.1:8000/docs#/
http://127.0.0.1:8000/redoc
"""