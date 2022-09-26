from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

from app.api.stock_name import StockName

templates = Jinja2Templates(directory="app/templates")
homepage_router = APIRouter()

@homepage_router.get("/")
async def home(request: Request):
	return templates.TemplateResponse("homepage/homepage.html",context={'request': request, 'choices': [e.value for e in StockName]})
	