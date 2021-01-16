from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.app import api_v1

app = FastAPI()
app.include_router(api_v1)

HTML = """
<center>
<h1>Hello🖐️ there</h1>
<h3>Try : <a href='https://ytmeta.tk/api/v1/BalvzyKg_4k'>https://ytmeta.tk/api/v1/BalvzyKg_4k</a></h3>
</center>
"""


@app.get("/")
def read_home():
    return HTMLResponse(content=HTML, status_code=200)