from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    prize: float

item_info = [
    {'name': 'Rahul', 'description': 'He is a good boy!', 'prize': '10000'}
]

def load_data(item_info):
    return item_info

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    data = load_data(item_info)
    data.append(item)
    return data