from fastapi import FastAPI
from enum import Enum

# This will help you give dropdown options in the Swagger UI or we can say predefine values
class ModelName(str, Enum):
    apple="Apple"
    banana="Banana"
    orange="Orange"


app = FastAPI()

@app.get('/')
async def main():
    return {'message':'This is a new concept somewhat similar to OOPs'}


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.apple:
        return {'model_name': model_name, 'message': f'Eat a {model_name} daily will keep you healthy!'}

    elif model_name is ModelName.banana:
        return {'model_name': model_name, 'message': f'Eating {model_name} daily will help you gain wiegth!'}

    return {'model_name': model_name, 'message': f'Eating {model_name} daily will help your skin keep hydrated!'}