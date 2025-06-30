from fastapi import FastAPI

data = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
    {"item_name": "Qux"},
    {"item_name": "Quux"},
    {"item_name": "Corge"},
    {"item_name": "Grault"},
    {"item_name": "Garply"},
    {"item_name": "Waldo"},
    {"item_name": "Fred"},
    {"item_name": "Plugh"},
    {"item_name": "Xyzzy"},
    {"item_name": "Thud"},
    {"item_name": "Waldo"},
    {"item_name": "Fred"},
    {"item_name": "Plugh"},
    {"item_name": "Xyzzy"},
    {"item_name": "Thud"}
]

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    """
    Read items with optional query parameters for pagination.
    
    :param skip: Number of items to skip (default is 0)
    :param limit: Maximum number of items to return (default is 10)
    :return: List of items
    """
    return {'items': data[skip : skip + limit], 'length of items': len(data[skip : skip + limit])}
