from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import index


app = FastAPI()


app.mount(
    path="/static",
    app=StaticFiles(directory="./static"),
    name="static"
)


app.include_router(index.router)
