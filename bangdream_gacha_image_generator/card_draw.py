from typing import List, Dict, Optional
from httpx import AsyncClient, Response
from random import choice
from loguru import logger


async def quick_get(url: str) -> Response:
    async with AsyncClient() as client:
        resp = await client.get(url)
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
    groupId = str(int(situationId/50))
    groupId = "card"+"0"*(5-len(groupId))+groupId
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


# 随机进行一个卡池的抽
async def draw_once(gachaId: int) -> Optional[int]:
    """
    说明：
        在指定卡池中随机抽一发
    参数：
        :param gachaId: 卡池ID
    """
    try:
        situationId: int = int(choice(await get_gacha_content(gachaId)))
    except Exception as e:
        logger.error(e)
        situationId = None
    return situationId


# 我要抽十发
async def draw_10times(gachaId: int) -> List[int]:
    """
    说明：
        顾名思义抽十发
    参数：
        :param gachaId: 卡池ID
    """
    result_list = []
    gacha_content = await get_gacha_content(gachaId)
    try:
        for i in range(10):
            situationId = int(choice(gacha_content))
            result_list.append(situationId)
        return result_list
    except Exception as e:
        logger.error(e)
        return []
