from io import BytesIO
from PIL import Image
from .assets import StaticPath, root
from .card_draw import card_img_url, get_card_info, get_char_info
from typing import Optional
from loguru import logger
from httpx import AsyncClient


def open_img(image_path: str) -> Image.Image:
    with open(image_path, "rb") as f:
        image = Image.open(f).convert("RGBA")
    return image


async def open_img_from_url(url: str) -> Optional[Image.Image]:
    try:
        async with AsyncClient() as client:
            resp = await client.get(url)
        return Image.open(BytesIO(resp.read())).convert("RGBA")
    except Exception as e:
        logger.error(e)
        return None


def frame_selector(rarity: int):
    if rarity == 4:
        return StaticPath.thumb_frame_rainbow
    elif rarity == 3:
        return StaticPath.thumb_frame_gold
    else:
        return StaticPath.thumb_frame_silver


class Card:
    def __init__(self, situationId) -> Image.Image:
        self.situationId = situationId

    async def get_necessary_info(self):
        situationId = self.situationId
        img_url = await card_img_url(situationId)
        self.image = await open_img_from_url(img_url)
        card_info = await get_card_info(situationId)
        self.rarity = card_info["rarity"]
        self.attribute = card_info["attribute"]
        characterId = card_info["characterId"]
        char_info = await get_char_info(characterId)
        self.bandID = char_info["bandId"]


def draw_card_thumb(card: Card):
    image = card.image
    rarity = card.rarity
    attribute = card.attribute
    bandID = card.bandID
    frame = open_img(frame_selector(rarity))
    star = open_img(StaticPath.star_untrained)
    attribute = open_img(root.img(f"icon_{attribute}.png"))
    band_icon = open_img(root.img(f"band_icon_{bandID}.png"))
    image = image
    image.alpha_composite(frame)
    image.alpha_composite(band_icon, (3, 3))
    image.alpha_composite(attribute, (130, 0))
    for i in range(rarity):
        image.alpha_composite(star, (5, 140-30*i))
    return image
