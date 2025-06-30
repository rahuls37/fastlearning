"""
You can also declare a body as a dict with keys of some type and values of some other type.
This way, you don't have to know beforehand what the valid field/attribute names are (as would be the case with Pydantic models).
This would be useful if you want to receive keys that you don't already know.
Another useful case is when you want to have keys of another type (e.g., int).
That's what we are going to see here.

In this case, you would accept any dict as long as it has int keys with float values:
"""
from fastapi import FastAPI

app = FastAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights