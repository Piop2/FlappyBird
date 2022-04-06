import pygame

from .ui.game import GameUI


class Renderer:
    def __init__(self, game):
        self.game = game

        self.fps = 60
        self.clock = pygame.time.Clock()

        self.ui = {
            "game": GameUI(game)
        }
        self.ui_mode = "game"
    
    def get_ui(self):
        return self.ui[self.ui_mode]
    
    def set_ui(self, new_mode):
        self.ui_mode = new_mode
        return

    def update(self):
        dt = self.clock.tick(self.fps)
        display = self.game.window.display

        display.blit(self.game.assets.images.background, (0, 0))

        ui = self.get_ui()
        ui.update(dt)
        ui.render()

        self.game.window.window.blit(pygame.transform.scale(display, self.game.window.WINDOW_SIZE), (0, 0))
        pygame.display.update()
