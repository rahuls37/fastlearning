from typing import Annotated

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None

@app.put('/items/{item_id}')
async def update_item(
    item_id: int, item: Item, user: User, importance: Annotated[str, Body()]
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results

"""
Example of what this might look like:
Instead of the data being split like:

Body: {item: {...}, user: {...}}
URL: ?importance=5

You get everything together in the body:

Body: {item: {...}, user: {...}, importance: 5}
"""