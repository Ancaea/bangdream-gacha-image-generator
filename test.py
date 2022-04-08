from bangdream_gacha_image_generator.image_draw import open_img, Card, draw_card

a = Card(image=open_img("./custom.jpg").resize((180, 180)),
         rarity=4,
         attribute="powerful")
b = draw_card(a)
b.show()
b.save("./me.png")