import pygame
import json

COLORKEY = (100, 100, 200)


def load_image(path):
    img = pygame.image.load(path)
    img.set_colorkey(COLORKEY)
    return img


def load_json(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return data


class Configs:
    def __init__(self):
        game = load_json("assets/configs/game.json")
        self.bird_speed = game["BirdSpeed"]

        window = load_json("assets/configs/window.json")
        self.window_size = window["WindowSize"]
        self.fullscreen = window["Settings"]["FullScreen"]

        render = load_json("assets/configs/render.json")
        self.fps = render["FPS"]


class Images:
    def __init__(self):
        self.icon = load_image("assets/images/icon/icon_50.png")

        self.background = load_image("assets/images/background.png")
        self.ground = load_image("assets/images/ground.png")

        # MenuUI #
        self.t_flappy_bird = load_image("assets/images/titles/flappy_bird.png")
        self.copyright = load_image("assets/images/copyright.png")
        self.b_start = load_image("assets/images/buttons/start.png")
        self.b_score = load_image("assets/images/buttons/score.png")


class Sounds:
    def __init__(self):
        pass


class Fonts:
    def __init__(self):
        pass


class Assets:
    def __init__(self):
        self.configs = Configs()
        self.images = Images()
        self.sounds = Sounds()
        self.fonts = Fonts()
