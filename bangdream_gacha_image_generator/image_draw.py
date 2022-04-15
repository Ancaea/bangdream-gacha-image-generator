from io import BytesIO
from PIL import Image
from .assets import StaticPath, root
from .bestdori import card_img_url, get_card_info, get_char_info
from typing import Dict
from loguru import logger
from httpx import AsyncClient
from .config import Config

region_code = Config.region_code


def open_img(image_path: str) -> Image.Image:
    with open(image_path, "rb") as f:
        image = Image.open(f).convert("RGBA")
    return image


async def open_img_from_url(url: str) -> Image.Image:
    try:
        async with AsyncClient() as client:
            resp = await client.get(url)
        return Image.open(BytesIO(resp.read())).convert("RGBA")
    except Exception as e:
        logger.error(e)
        return Image.new("RGBA", (0, 0))


def frame_selector(rarity: int):
    if rarity == 4:
        return StaticPath.thumb_frame_rainbow
    elif rarity == 3:
        return StaticPath.thumb_frame_gold
    else:
        return StaticPath.thumb_frame_silver


class Card:
    def __init__(self, situationId):
        self.situationId = situationId

    async def _get_necessary_info(self):
        situationId = self.situationId
        img_data = await card_img_url(situationId)
        self.img_url = img_data["img_url"]
        self.thumb_url = img_data["thumb_url"]
        card_info = await get_card_info(situationId)
        self.rarity = card_info["rarity"]
        self.attribute = card_info["attribute"]
        characterId = card_info["characterId"]
        char_info = await get_char_info(characterId)
        self.bandID = char_info["bandId"]

    @staticmethod
    async def draw_card_thumb(situationId: int) -> Image.Image:
        card = Card(situationId)
        await card._get_necessary_info()
        thumb_url = card.thumb_url
        image = await open_img_from_url(thumb_url)
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
            image.alpha_composite(star, (5, 140 - 30 * i))
        return image

    @staticmethod
    async def draw_card(situationId: int) -> Image.Image:
        card = Card(situationId)
        await card._get_necessary_info()
        img_url = card.img_url
        image = await open_img_from_url(img_url)
        return image


class Gacha:
    @staticmethod
    async def draw_banner(gacha_content: Dict) -> Image.Image:
        try:
            bannerAssetBundleName = gacha_content["bannerAssetBundleName"]
            banner_url = f"https://bestdori.com/assets/jp/homebanner_rip/{bannerAssetBundleName}.png"
            banner_image = await open_img_from_url(banner_url)
            return banner_image
        except Exception:
            return Image.new("RGBA", (0, 0))