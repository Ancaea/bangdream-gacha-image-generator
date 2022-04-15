from typing import List, Dict
from httpx import AsyncClient, Response
from loguru import logger
from time import time as now


async def quick_get(url: str) -> Response:
    async with AsyncClient() as client:
        resp = await client.get(url, timeout=None)
    return resp


async def get_card_info(situationId: int) -> Dict:
    url = f"https://bestdori.com/api/cards/{situationId}.json"
    resp = await quick_get(url)
    return resp.json()


async def get_char_info(characterId: int):
    url = "https://bestdori.com/api/characters/all.2.json"
    resp = await quick_get(url)
    char_info = resp.json()[str(characterId)]
    return char_info


async def card_img_url(situationId: int) -> str:
    groupId = str(int(situationId / 50))
    groupId = "card" + "0" * (5 - len(groupId)) + groupId
    resourceSetName = (await get_card_info(situationId))["resourceSetName"]
    img_url = f"https://bestdori.com/assets/jp/thumb/chara/{groupId}_rip/{resourceSetName}_normal.png"
    return img_url


async def get_gacha_content(gachaId: int) -> List[str]:
    """
    说明：
        获取选定池子中所有的卡片ID
    参数：
        :param gachaId: 卡池ID
    """
    try:
        url = f"https://bestdori.com/api/gacha/{gachaId}.json"
        resp = await quick_get(url)
        gachaId_content = list(resp.json()["details"][0].keys())
    except Exception as e:
        logger.error(e)
        gachaId_content = []
    return gachaId_content


async def get_all_gacha() -> Dict:
    try:
        url = "https://bestdori.com/api/gacha/all.5.json"
        resp = await quick_get(url)
        return resp.json()
    except Exception as e:
        logger.error(e)
        return {}


def is_upping(value) -> bool:
    try:
        if value["publishedAt"][3] < str(now()*1000) < value["closedAt"][3]:
            return True
        else:
            return False
    except Exception:
        return False


async def get_upping_gacha() -> Dict:
    all_gacha = await get_all_gacha()
    upping_gacha = {k: v for k, v in all_gacha.items() if is_upping(v)}
    return upping_gacha
