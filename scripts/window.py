import pygame

class Window:
    def __init__(self):
        self.WINDOW_SIZE = (288, 512)
        self.DISPLAY_SIZE = (144, 256)

        pygame.init()
        self.window =  pygame.display.set_mode(self.WINDOW_SIZE)
        self.display = pygame.Surface(self.DISPLAY_SIZE)
        pygame.display.set_caption("Flappy Bird")
