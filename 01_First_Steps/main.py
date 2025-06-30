from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def main():
    return {'message':'This is learning for me'}

# @app.get('/greet/{name}')
# async def greeting(name):
#     return {f'Hello {name}! how are your let"s start learning.'}