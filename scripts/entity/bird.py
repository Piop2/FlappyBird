import pygame

from scripts.entity.basic_entity import BasicEntity


class Bird(BasicEntity):
    def __init__(self, game):
        super().__init__(game=game,
                         image=None,
                         pos=None,
                         hitbox_size=None)

        self.bird_speed = 0.07


