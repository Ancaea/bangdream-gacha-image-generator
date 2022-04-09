from bangdream_gacha_image_generator.card_draw import draw_10times, draw_once
from bangdream_gacha_image_generator.image_draw import Card, draw_card_thumb
import asyncio
from PIL import Image

async def test1(id):
    cardID = id
    card = Card(situationId=cardID)
    await card.get_necessary_info()
    card_img = draw_card_thumb(card)
    return card_img

async def test2():
    card_list = await draw_10times(5)
    image = Image.new("RGBA", (900, 360))
    for i in range(10):
        size = (i*180 if i<=4 else (i-5)*180, 0 if i<=4 else 180)
        image.alpha_composite(await test1(card_list[i]), size)
    image.show()

asyncio.run(test2())