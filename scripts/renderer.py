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

    def update(self):
        self.ui.update()

    def render(self):
        self.ui.render()


class Renderer:
    def __init__(self, game):
        self.game = game

        self.fps = 60
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.ui = UI(game)
    
    def get_ui(self):
        return self.ui.ui

    def update(self):
        self.dt = self.clock.tick(self.fps)
        display = self.game.window.display
        window = self.game.window.window
        monitor_size = self.game.window.MONITOR_SIZE
        window_size = self.game.window.WINDOW_SIZE
        fullscreen = self.game.window.fullscreen

        self.ui.update()
        self.ui.render()

        if fullscreen:
            window.blit(pygame.transform.scale(display, monitor_size), (0, 0))
        else:
            window.blit(pygame.transform.scale(display, window_size), (0, 0))

        pygame.display.update()
