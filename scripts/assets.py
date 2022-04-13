import pygame

COLORKEY = (100, 100, 200)


def load_image(path):
    img = pygame.image.load(path)
    img.set_colorkey(COLORKEY)
    return img


class Image:
    def __init__(self):
        self.background = load_image("assets/image/background.png")
        self.ground = load_image("assets/image/ground.png")
        self.copyright = load_image("assets/image/copyright.png")

        self.b_start = load_image("assets/image/button/start.png")
        self.b_score = load_image("assets/image/button/score.png")


class Sound:
    def __init__(self):
        pass


class Font:
    def __init__(self):
        pass


class Assets:
    def __init__(self):
        self.image = Image()
        self.sound = Sound()
        self.font = Font()
