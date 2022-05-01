import pygame

from scripts.animation import Animation


class Entity:
    def __init__(self, game):
        self.game = game

        self.image = None
        self.pos = None

    def update(self):
        return

    def render(self):
        if isinstance(self.image, Animation):
            self.image.render(self.game.window.display.blit, self.pos)
        else:
            self.game.window.display.blit(self.image, self.pos)
