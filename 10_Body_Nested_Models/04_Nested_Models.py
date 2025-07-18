from typing import Annotated

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None

@app.put('items/{item_id}')
async def udpate_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results