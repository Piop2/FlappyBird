import pygame


class Input:
    def __init__(self, game):
        self.game = game

        self.mouse_pos = [0, 0]
        self.click = False

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.game.running = False
