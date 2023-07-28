from flet import *
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json


def get_image(url: str):
    try:
        url = url
        page = urlopen(url)
        page_soup = BeautifulSoup(page, 'html.parser')
        img_item = page_soup.find('img', {'class':'_396cs4 _2amPTt _3qGmMb'})
        img_src = img_item.get('src') # type: ignore
        return img_src
    except AttributeError:
        return "https://rukminim2.flixcart.com/image/416/416/l0vbukw0/computer/2/c/9/-original-imagckcfhgpfbdme.jpeg?q=70"


if __name__ == "__main__":
    data = []
    converted_data = []
    with open("package/data/laptops.json", "r") as file:
        data = json.load(file)

    for laptop in data:
        img_src = get_image(laptop['link'])
        laptop['link'] = img_src
        converted_data.append(laptop)
        print(laptop['index'])

    with open("package/data/laptop_converted.json", "w") as file:
        file.write(json.dumps(converted_data))
