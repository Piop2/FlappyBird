import pygame

class Input:
    def __init__(self, game):
        self.game = game
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.game.running = False
