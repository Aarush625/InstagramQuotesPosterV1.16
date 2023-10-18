from io import BytesIO
from PIL import Image, ImageFont, ImageDraw
import requests
import random
import json
from textwrap import wrap
from instagrapi import Client
import config
import time

cl = Client()

cl.login(config.username, config.password)


while True:
    array = ["age", "alone", "amazing", "anger", "architecture", "art", "attitude",
            "beauty", "best", "birthday", "business", "car", "change", "communications",
            "computers", "cool", "courage", "dad", "dating", "death", "design", "dreams",
            "education", "environmental", "equality", "experience", "failure", "faith",
            "family", "famous", "fear", "fitness", "food", "forgiveness", "freedom",
            "friendship", "funny", "future", "god", "good", "government", "graduation",
            "great", "happiness", "health", "history", "home", "hope", "humor",
            "imagination", "inspirational", "intelligence", "jealousy", "knowledge",
            "leadership", "learning", "legal", "life", "love", "marriage", "medical",
            "men", "mom", "money", "morning", "movies", "success"]

    array2 = ["bb", "ff", "gg", "nn", "nnm", "vv", "qq", "oo"]


    category = random.choice(array)
    image = random.choice(array2)

    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)

    response = requests.get(
        api_url, headers={'X-Api-Key': 'O5hbwotukFWX3vBu9LW5tw==Q8teoWXdFng6bm35'})

    if response.status_code == requests.codes.ok:
        quotes = json.loads(response.text)
        for quote in quotes:
            img = Image.open(f'{image}.jpg')
            W, H = img.size
            msg = str(quote['quote'])
            author = str(quote['author'])
            finalMessage = "\n".join(wrap(msg, 40))
            font = ImageFont.truetype('BebasNeue-Regular.ttf', size=34)
            draw = ImageDraw.Draw(img)
            w, h = draw.textsize(finalMessage)
            draw.multiline_text(((W-w)/3, ((H-h))/2) , finalMessage, align="center", font=font)
            data = BytesIO()
            rgb_im = img.convert('RGB')
            rgb_im.save('bali_new.jpeg')
            media = cl.photo_upload(
                path = 'bali_new.jpeg',
                caption = f"-{author},\n {msg},\nsuch a beatiful quote. This always touches my heart."
            )
    else:
        print("Error:", response.status_code, response.text)
    time.sleep(21600)