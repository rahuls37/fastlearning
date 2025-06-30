from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

# ```item-query``` is not a valid Python variable name
# But you can declare an alias, and that alias is what will be used to find the parameter value
@app.get('/items/')
async def read_items(q: Annotated[str | None, Query(alias='item-query')]=None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results