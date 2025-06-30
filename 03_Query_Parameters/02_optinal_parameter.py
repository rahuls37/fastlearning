from fastapi import FastAPI


app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(item_id: str, q: str | None = None):
    """
    Read items with an optional query parameter `q`.
    
    :param item_id: The ID of the item to read.
    :param q: An optional query parameter.
    :return: A dictionary containing the item ID and the query parameter.
    """
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}