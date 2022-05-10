from scripts.entity.bird import Bird
from scripts.entity.pipe import Pipes


class World:
    def __init__(self, game):
        self.game = game

        self.bird = Bird(game)
        self.bird.pos = game.assets.configs.bird_start_pos
        self.bird_jump_power = game.assets.configs.bird_jump_power
        self.bird_acc = 0

        self.gravity = game.assets.configs.gravity

        self.pipes = []

        self.mode = "start"
        self.gameover = False

    def init_world(self):
        self.mode = "ready"
        self.gameover = False
        self.bird.pos = self.game.assets.configs.bird_start_pos
        self.bird_acc = 0

    def update(self):
        if self.game.renderer.ui_mode == "game":
            dt = self.game.renderer.dt
            jump = self.game.input.jump

            match self.mode:
                case "ready":
                    if jump:
                        self.mode = "start"
                case "start":
                    self.bird_acc += self.gravity
                    if jump:
                        self.bird_acc = -self.bird_jump_power
                        self.game.input.jump = False

                    self.bird.move(0, dt * self.bird_acc)

                    display_size = self.game.window.DISPLAY_SIZE
                    max_height = self.game.assets.configs.bird_max_height
                    ground_size = self.game.assets.images.ground.get_size()
                    bird_size = self.game.assets.images.bird.get_size()
                    # 바닥 충돌
                    if self.bird.pos[1] >= (ground_y := display_size[1] - ground_size[1] - bird_size[1]):
                        self.bird.pos = (self.bird.pos[0], ground_y)
                        self.bird_acc = 0
                        self.gameover = True
                    # 천장 충돌
                    elif self.bird.pos[1] <= max_height:
                        self.bird.pos = [self.bird.pos[0], max_height]

                case _:
                    pass
