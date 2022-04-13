import pygame


class Window:
    def __init__(self, game):
        pygame.init()

        self.WINDOW_SIZE = game.assets.configs.window_size
        self.DISPLAY_SIZE = (144, 256)
        self.MONITOR_SIZE = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.fullscreen = game.assets.configs.fullscreen

        self.window = pygame.display.set_mode(self.WINDOW_SIZE)
        self.display = pygame.Surface(self.DISPLAY_SIZE)
        pygame.display.set_caption("Flappy Bird")
        pygame.display.set_icon(game.assets.images.icon)

        if self.fullscreen:
            self.set_fullscreen()

    def set_fullscreen(self):
        self.fullscreen = True
        pygame.display.set_mode(self.MONITOR_SIZE, pygame.FULLSCREEN)

    def set_window(self):
        self.fullscreen = False
        pygame.display.set_mode(self.WINDOW_SIZE)

