from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode
import requests

api_key = 'eWG1Gts8IZHKKynVLgQeMlOgYLqbYmK04ScZTuUJ'


def Combertir_a_URL(**kwargs):
	url = kwargs.get("url")
	params = kwargs.get("params")
	response = redirect(url)
	if params:
		query_string = urlencode(params)
		response['Location'] += '?' + query_string
	return response


class APIMixin:
    def __init__(self, **kwargs):
        self.cat = kwargs.get("cat")
        self.date = kwargs.get("date")

    def get_data(self):
        if self.cat == "mars":
            url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=eWG1Gts8IZHKKynVLgQeMlOgYLqbYmK04ScZTuUJ'
            r = requests.get(url)
            return {"image": r.json()['photos'][0]["img_src"], "text": "Image data gathered by NASA's Curiosity, Opportunity, and Spirit rovers on Mars."}
        
        elif self.cat == "apod":
            url = f'https://api.nasa.gov/planetary/apod?api_key=eWG1Gts8IZHKKynVLgQeMlOgYLqbYmK04ScZTuUJ&date={self.date}'
            r = requests.get(url)
            return {"image": r.json()["url"], "text": r.json()["explanation"]}

        return None
