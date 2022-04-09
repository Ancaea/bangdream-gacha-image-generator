from os import path

ASSETS = path.abspath(path.join(path.dirname(__file__), "assets"))

class StaticPath:
    # thumb_frame
    thumb_frame_silver = path.join(ASSETS, "img", "thumb_frame_silver.png")
    thumb_frame_gold = path.join(ASSETS, "img", "thumb_frame_gold.png")
    thumb_frame_rainbow = path.join(ASSETS, "img", "thumb_frame_rainbow.png")
    # star
    star_untrained = path.join(ASSETS, "img", "star_untrained.png")
    star_after_training = path.join(ASSETS, "img", "star_after_training.png")
