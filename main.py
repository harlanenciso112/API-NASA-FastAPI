from fastapi import FastAPI, Request
from config import *
import data as n

app = FastAPI()

@app.get("/")
def main(request : Request):
    return templates.TemplateResponse("index.html",{"request": request})

@app.get("/asteroides")
def asteroids():
    resultado = n.get_data_asteroids()
    return {"asteroides": resultado}

@app.get("/APOD")
def apod(request: Request):
    title, image_url, explanation = n.get_img_day()
    return templates.TemplateResponse("apod.html", {"request": request, "title": title, "image_url": image_url, "description": explanation})