import pygame


def clip(surf, x, y, w, h):
    handle_surf = surf.copy()
    clip_rect = pygame.Rect(x, y, w, h)
    handle_surf.set_clip(clip_rect)
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()
