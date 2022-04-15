from bangdream_gacha_image_generator import Card, draw_10times
from bangdream_gacha_image_generator.bestdori import get_all_gacha, get_gacha_content, get_upping_gacha
import asyncio
from PIL import Image
import ujson as json
from datetime import datetime
from time import time

async def test2():
    card_list = await draw_10times(5)
    image = Image.new("RGBA", (900, 360))
    for i in range(10):
        size = (i*180 if i <= 4 else (i-5)*180, 0 if i <= 4 else 180)
        image.alpha_composite(await Card.draw_card_thumb(card_list[i]), size)
    return image

async def test3():
    return (await Card.draw_card_thumb(790))

res = asyncio.run(get_upping_gacha())
print(res)