from scripts.entity.basic_entity import Entity


class Bird(Entity):
    def __init__(self, game):
        super().__init__(game)

        self.image = game.assets.images.game_bird_ani
        self.pos = [0, 0]
        self.bird_speed = game.assets.configs.bird_speed

    def render(self):
        image = self.image.get()

        rotated_image = None

        self.game.window.display.blit(image, self.pos)
