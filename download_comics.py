import os
import requests
import random
from urllib.parse import urlparse


def save_img(img_url, filename):
    response = requests.get(img_url)
    response.raise_for_status()
    with open(f'images/{filename}', 'wb') as file:
        file.write(response.content)


def get_file_name(img_url):
    parsed_url = urlparse(img_url)
    filename = os.path.split(parsed_url.path)[1]
    return filename


def download_random_comic():
    total_number_comics = 2771
    number = random.randint(1, total_number_comics)
    url = f'https://xkcd.com/{number}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
