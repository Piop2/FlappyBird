from scripts.animation import Animation


class Entity:
    def __init__(self, game):
        self.game = game

        self.image = None
        self.pos = None

    def move(self, to_x, to_y):
        self.pos = self.pos[0] + to_x, self.pos[1] + to_y

    def update(self):
        if isinstance(self.image, Animation):
            self.image.update(self.game.renderer.dt)

    def render(self):
        self.game.window.display.blit(self.image, self.pos)
