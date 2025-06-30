from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/items/')
async def read_items(q: Annotated[list[str] | None, Query(min_length=1, max_length=50)]=None):
    query_items ={'q':q}
    return query_items

# You can also use list directly instead of list[str]
# async def read_items(q: Annotated[list | None, Query(min_length=1, max_length=50)]=None):
#     query_items ={'q':q}
#     return query_items
# Keep in mind that in this case, FastAPI won't check the contents of the list.