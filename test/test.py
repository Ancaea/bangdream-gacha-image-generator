from bangdream_gacha_image_generator.card_draw import draw_10times, draw_once
from bangdream_gacha_image_generator.image_draw import Card, draw_card_thumb
import asyncio

async def test1():
    cardID = await draw_once(790)
    card = Card(situationId=cardID)
    await card.get_necessary_info()
    card_img = draw_card_thumb(card)
    card_img.show()

async def test2():
    card_list = await draw_10times(790)
    print(card_list)

asyncio.run(test1())