import requests
from fastapi import APIRouter
from .utils import metadata, ENDPOINT


api_v1 = APIRouter(prefix="/api/v1")


@api_v1.get("/")
def read_home():
    return "Hello🖐️ there"


@api_v1.get("/{id}")
async def get_video_metadata(id: str):
    result = requests.get(ENDPOINT(id)).content
    meta = metadata(result)
    return meta