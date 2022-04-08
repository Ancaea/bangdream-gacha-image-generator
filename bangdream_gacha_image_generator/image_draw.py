from PIL import Image
from .assets import StaticPath


def open_img(image_path: str) -> Image.Image:
    with open(image_path, "rb") as f:
        image = Image.open(f).convert("RGBA")
    return image


class Card:
    def __init__(self, image: Image.Image, rarity, attribute) -> Image.Image:
        self.image = image
        self.rarity = rarity
        self.attribute = attribute

        
def draw_card(card: Card):
    image = card.image
    rarity = card.rarity
    frame = open_img(StaticPath.thumb_frame_rainbow)
    star = open_img(StaticPath.star_after_training)
    attribute = open_img(StaticPath.icon_powerful)
    band_icon = open_img(StaticPath.band_icon_7)
    image = image
    image.alpha_composite(frame)
    image.alpha_composite(band_icon, (3, 3))
    image.alpha_composite(attribute, (130, 0))
    for i in range(rarity):
        image.alpha_composite(star, (5, 140-30*i))
    return image