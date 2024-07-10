from fastapi import FastAPI

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "World"}
