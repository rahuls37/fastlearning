from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(q: str | None = None):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'bar'}]}
    if q:
        results.update({'q':q})
    return results