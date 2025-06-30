from fastapi import FastAPI
from pathlib import Path

# folder_path=Path('data')
# if folder_path.exists():
#     print(f"Folder '{folder_path}' already existed.")
# else:
#     try:
#         folder_path.mkdir(parents=True)
#         print(f"Folder '{folder_path}' created successfully.")
#     except Exception as e:
#         print(f'Error creating folder: {e}')
# with open('data/example.txt','w') as f:
#     f.write('Hello my Guys!')

app=FastAPI()

@app.get('/file/{file_path:path}') # Using 'path' to accept slashes in the path
def read_file(file_path: str):
    return {'file_path': file_path, 'content': Path(file_path).read_text()}