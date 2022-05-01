from scripts.entity.basic_entity import Entity


class Pipe(Entity):
    def __init__(self, game, image, pos):
        super().__init__(game)

        self.image = image
        self.pos = pos

class Pipes:
    def __init__(self, game, pos_x):
        self.top_pipe = Pipe(game, )
