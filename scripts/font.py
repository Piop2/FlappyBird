from scripts.utils.load_f import load_image
from scripts.utils.clip import clip

FONT_SEP_COLOR = 255 # R


def load_font_image(path):
    font_img = load_image(path)
    font_h = font_img.get_height()

    font_images = []
    font_w = 0

    start_x = 0
    for end_x in range(font_img.get_width()):
        if font_img.get_at((end_x, 0))[0] == FONT_SEP_COLOR:
            if font_w == 0:
                font_w = end_x - start_x
            
            font_images.append(clip(font_img, start_x, 0, end_x - start_x, font_h))
            start_x = end_x + 1
    return font_images, font_w, font_h

class Font:
    @staticmethod
    def load(path, font_space):
        return Font(*load_font_image(path), font_space)

    def __init__(self, images, w, h, space):
        self.images = images
        self.w = w
        self.h = h
        self.space = space
    
    def get_width(self, texts):
        return self.w * len(texts) + self.space * (len(texts) - 1)

    def render(self, surf, pos, texts):
        offset_x = 0
        for text in texts:
            surf.blit(self.images[int(text)], (pos[0] + offset_x, pos[1]))
            offset_x += self.w + self.space
