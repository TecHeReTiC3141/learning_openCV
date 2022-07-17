import requests
from bs4 import BeautifulSoup
from pprint import pprint
from pathlib import Path
from PIL import Image
from io import BytesIO

req = requests.get('https://minecraft.fandom.com/wiki/List_of_block_textures')

soup = BeautifulSoup(req.text, 'lxml')

# print(soup.prettify())

blocks_text = [i.p.text.strip() for i in
               soup.select('ul.gallery > li.gallerybox div.gallerytext') if i.p]

last_block = 'Warped Planks'
blocks_text = blocks_text[:blocks_text.index(last_block)]

blocks_img_url = [i.get('href') for i in
                  soup.select('ul.gallery > li.gallerybox div.thumb a.image')][:len(blocks_text)]

for block_url, block_text in zip(blocks_img_url, blocks_text):
    try:
        img = Image.open(BytesIO(requests.get(block_url).content)).resize((128, 128))
        img.save(f'../minecraft_blocks/{block_text.replace("/", ".")}.png', 'PNG')
    except Exception as e:
        print(e, block_text)