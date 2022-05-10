import pygame


class Button:
    def __init__(self, image, pos):
        self.image = image
        self.pushed = False

        self.pos = pos

    @property
    def rect(self):
        return pygame.Rect(*self.pos, *self.image.get_size())

    def push_down(self):
        self.pushed = True

    def push_up(self):
        self.pushed = False

    def is_mouse_touched(self, mouse_pos):
        return self.rect.collidepoint(*mouse_pos)

    def render(self, surf):
        if self.pushed:
            surf.blit(self.image, (self.pos[0], self.pos[1] + 2))
        else:
            surf.blit(self.image, self.pos)
