from scripts.entity.basic_entity import Entity


class Pipe(Entity):
    def __init__(self, game, image, pos):
        super().__init__(game)

        self.image = image
        self.pos = pos

class Pipes:
    def __init__(self, game, pos):
        self.top = Pipe(game, game.assets.images.top_pipe, [0, 0])
        self.bottom = Pipe(game, game.assets.images.bottom_pipe, [0, 0])

    def render(self):
        self.top.render()
        self.bottom.render()
