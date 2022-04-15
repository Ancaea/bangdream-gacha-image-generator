from typing import List, Optional
from random import choice
from loguru import logger
from .bestdori import get_gacha_content


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
