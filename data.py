from config import URL_ASTEROIDS, URL_APOD
import requests

def get_data_asteroids():
    respuesta = requests.get(URL_ASTEROIDS)
    datos = respuesta.json()
    asteroides = datos["near_earth_objects"]["2015-09-08"]
    resultado = [
        {"name": ast["name"], "danger": ast["is_potentially_hazardous_asteroid"]}
        for ast in asteroides
    ]

    return resultado


def get_img_day():
    respuesta = requests.get(URL_APOD)
    date = respuesta.json()
    
    title = datos["title"]
    image_url = datos["hdurl"]
    explanation = datos["explanation"]

    return title, image_url, explanation

    
