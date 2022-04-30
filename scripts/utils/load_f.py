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
