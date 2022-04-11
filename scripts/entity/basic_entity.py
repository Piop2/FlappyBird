import pygame


class BasicEntity:
    def __init__(self, game, image, pos, hitbox_size):
        self.game = game

        self.image = image
        self.pos = pos
        self.hitbox_size = hitbox_size

    @property
    def hitbox(self):
        return pygame.Rect(*self.pos, *self.hitbox_size)

    def render(self):
        self.game.window.display.blit(self.image, self.pos)
