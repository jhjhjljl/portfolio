from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix="",
    tags=["index"]
)


templates = Jinja2Templates(directory="./templates")


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )
