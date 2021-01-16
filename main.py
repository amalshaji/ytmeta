from fastapi import FastAPI

from app.app import api_v1

app = FastAPI()
app.include_router(api_v1)


@app.get("/")
def read_home():
    return "Hello🖐️ there"