import datetime
currentDT = datetime.datetime.now()

# d = str(currentDT.strftime("%Y-%m-%d %H:%M:%S"))


card = {"img_url": "Image-Here.png",
        "is_new": True,
        "is_featured": True,
        "is_super": True,
        "title": "Giveaways",
        "text": "Something here..",
        "uploaded": currentDT.strftime("%Y-%m-%d %H:%M:%S"),
        "views": "Can't be counted yet."}

cards = [card, card, card, card, card, card, card]
