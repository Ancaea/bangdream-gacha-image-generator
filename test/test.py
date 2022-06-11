from bangdream_gacha_image_generator import Card, draw_10times, Gacha
import asyncio
from PIL import Image
import ujson as json
from time import time as now
from loguru import logger
from bangdream_gacha_image_generator.bestdori import get_gacha_content, get_upping_gacha




async def image_10times():
    card_list = await draw_10times(5)
    image = Image.new("RGBA", (900, 360))
    for i in range(10):
        size = (i * 180 if i <= 4 else (i - 5) * 180, 0 if i <= 4 else 180)
        image.alpha_composite(await Card.draw_card_thumb(card_list[i]), size)
    return image


async def test():
    card = Card(situationId=980)
    res = await Card.draw_card_thumb(situationId=980)
    return res


res = asyncio.run(test())
res.show()