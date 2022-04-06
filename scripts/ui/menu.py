import pygame


class MenuUI:
    def __init__(self, game):
        self.game = game

        self.ground = game.assets.images.ground
        self.ground_x = 0
        self.ground_speed = 0.07

        self.copyright = game.assets.images.copyright
    
    def update(self, dt):
        self.ground_x -= self.ground_speed * dt
        if self.ground_x <= - self.ground.get_width():
            self.ground_x = 0
    
    def render(self):
        display = self.game.window.display

        display.blit(self.ground, (self.ground_x, self.game.window.DISPLAY_SIZE[1] - self.ground.get_height()))
        display.blit(self.ground, (self.ground_x + self.ground.get_width(), self.game.window.DISPLAY_SIZE[1] - self.ground.get_height()))
