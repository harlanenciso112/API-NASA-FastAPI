import os
from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates

load_dotenv()
api_password = os.getenv("DEMO_KEY")
URL_ASTEROIDS = f"https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key={api_password}"
URL_APOD = f"https://api.nasa.gov/planetary/apod?api_key={api_password}"
templates = Jinja2Templates(directory="templates")