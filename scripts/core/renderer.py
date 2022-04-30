import pygame

from scripts.ui.menu import MenuUI
from scripts.ui.game import GameUI

from scripts.effects.vfx import FadeOut


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

        self.FPS = game.assets.configs.fps
        self.clock = pygame.time.Clock()
        self.dt = 0

        self._ui = UI(game)
        self.fade = FadeOut((0, 0, 0), game.assets.configs.ui_fadeout_s)
    
    def get_dt(self):
        return self.dt

    @property
    def ui(self):
        return self._ui.ui

    @ui.setter
    def ui(self, new_mode):
        is_faded = self.fade.update(self.get_dt())

        if is_faded:
            self._ui.set_mode(new_mode)
            self.fade.init_alpha()
            self.ui.init_ui()

    def update(self):
        self.dt = self.clock.tick(self.FPS)
        display = self.game.window.display
        window = self.game.window.window
        monitor_size = self.game.window.MONITOR_SIZE
        window_size = self.game.window.WINDOW_SIZE
        fullscreen = self.game.window.fullscreen

        display.fill((255, 255, 255))

        self.ui.update()
        self.ui.render()

        if fullscreen:
            window.blit(pygame.transform.scale(display, monitor_size), (0, 0))
        else:
            window.blit(pygame.transform.scale(display, window_size), (0, 0))

        self.fade.render(window)

        pygame.display.update()
