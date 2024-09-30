import sys, os
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.templating import Jinja2Templates
import uvicorn
# Add the root directory to the syspath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Create FastAPI app object
app = FastAPI()

# Get the absolute path to the templates directory
templates_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "templates"))
# Get the absolute path to the static directory
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "static"))
# Serve static files
app.mount("/static", StaticFiles(directory=static_dir))
# Set up Jinja2 template for rendering HTML files
templates = Jinja2Templates(directory=templates_dir)

# In-memory user storage for login
users = {"admin": "password"}

# Define routes
@app.get("/")
async def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})




if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001, workers=1)