from .RHelper import RHelper

root = RHelper()
root = root.assets


class StaticPath:
    # thumb_frame
    thumb_frame_silver = root.img("thumb_frame_silver.png")
    thumb_frame_gold = root.img("thumb_frame_gold.png")
    thumb_frame_rainbow = root.img("thumb_frame_rainbow.png")
    # star
    star_untrained = root.img("star_untrained.png")
    star_after_training = root.img("star_after_training.png")
