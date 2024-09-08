import uvicorn
from fastapi import FastAPI
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # changing root directory from /app/ to /

app = FastAPI()  # starting a FatAPI app


@app.get("/")
async def root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
