#route_homepage.py

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()


@general_pages_router.get("/")
async def home(request: Request):
	return templates.TemplateResponse("general_pages/homepage.html",{"request":request})

@general_pages_router.get("/ourservices")
async def home(request: Request):
	return templates.TemplateResponse("general_pages/ourservices.html",{"request":request})
	
@general_pages_router.get("/contactus")
async def home(request: Request):
	return templates.TemplateResponse("general_pages/contactus.html",{"request":request})
@general_pages_router.get("/contactus/done")
async def home(request: Request):
	return templates.TemplateResponse("general_pages/contactusdoe.html",{"request":request})
	