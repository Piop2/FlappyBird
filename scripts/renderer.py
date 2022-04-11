import pygame

from scripts.ui.menu import MenuUI
from scripts.ui.game import GameUI


class UI:
    def __init__(self, game):
        self._ui = {
            "menu": MenuUI(game),
            "game": GameUI(game)
        }
        self._mode = "menu"

    @property
    def ui(self):
        return self._ui[self._mode]

    def set_mode(self, new_mode):
        self._mode = new_mode

    def update(self, dt):
        self.ui.update(dt)

    def render(self):
        self.ui.render()


class Renderer:
    def __init__(self, game):
        self.game = game

        self.fps = 60
        self.clock = pygame.time.Clock()

        self.ui = UI(game)

    def update(self):
        dt = self.clock.tick(self.fps)
        display = self.game.window.display

        self.ui.update(dt)
        self.ui.render()

        self.game.window.window.blit(pygame.transform.scale(display, self.game.window.WINDOW_SIZE), (0, 0))
        pygame.display.update()
