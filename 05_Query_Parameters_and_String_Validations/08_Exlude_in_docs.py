from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()


@app.get('/items/')
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50, include_in_schema=False)]=None):
    results = {'items': [{'item_id':'Foo'}, {'item_id':'Bar'}]}
    if q:
        results.update({'q':q})
    return results