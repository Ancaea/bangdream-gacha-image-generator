from bangdream_gacha_image_generator.card_draw import draw_10times
from bangdream_gacha_image_generator.image_draw import Card
import asyncio
from PIL import Image


async def test2():
    card_list = await draw_10times(5)
    image = Image.new("RGBA", (900, 360))
    for i in range(10):
        size = (i*180 if i <= 4 else (i-5)*180, 0 if i <= 4 else 180)
        image.alpha_composite(await Card.draw_card_thumb(card_list[i]), size)
    image.save("./saved_pic.png")
    return image

async def test3():
    return (await Card.draw_card_thumb(790))

res = asyncio.run(test2())
res.show()
