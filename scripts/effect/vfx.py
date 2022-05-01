import pygame


class FadeOut:
    def __init__(self, color, speed):
        self.color = color
        self.alpha = 0
        self.speed = speed

    def init_alpha(self):
        self.alpha = 0

    def update(self, dt):
        self.alpha += self.speed * dt
        if self.alpha >= 255:
            self.alpha = 255
            return True
        return False
    
    def render(self, surf):
        fade_surf = pygame.Surface(surf.get_size())
        fade_surf.fill(self.color)
        fade_surf.set_alpha(self.alpha)

        surf.blit(fade_surf, (0, 0))
    
    
