import pygame

COLORKEY = (100, 100, 200)


def load_image(path):
    img = pygame.image.load(path)
    img.set_colorkey(COLORKEY)
    return img


class Images:
    def __init__(self):
        self.background = load_image("assets/images/background.png")
        self.ground = load_image("assets/images/ground.png")
        self.copyright = load_image("assets/images/copyright.png")


class Sounds:
    def __init__(self):
        pass


class Font:
    def __init__(self):
        pass


class Assets:
    def __init__(self):
        self.images = Images()
        self.sounds = Sounds()
        self.font = Font()
