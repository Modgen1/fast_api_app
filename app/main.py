from fastapi import FastAPI
import os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # changing root directory from /app/ to /

from app.users.routers import reg_router

app = FastAPI()  # starting a FatAPI app
app.include_router(reg_router)


@app.get("/")
async def root():
    return {"Hello": "World"}
