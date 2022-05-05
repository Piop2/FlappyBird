from scripts.ui.basic_ui import UI

from scripts.effect.vfx import FadeIn

class GameUI(UI):
    def __init__(self, game):
        super().__init__(game)

        self.background = game.assets.images.background
        self.ground = game.assets.images.ground
        self.ground_x = 0
        self.ground_speed = game.assets.configs.bird_speed

        self.bird = self.game.world.bird

        self._buttons = {}

        self.fade = FadeIn((255, 255, 255), game.assets.configs.gameover_fadeout_s)

    def init_ui(self):
        self.ground_x = 0
        self.fade.init_alpha()

    def update(self):
        dt = self.game.renderer.dt

        if self.game.world.gameover:
            is_faded = self.fade.update(dt)
        else:
            self.bird.update()

            self.ground_x -= self.ground_speed * dt
            if self.ground_x <= - self.ground.get_width():
                self.ground_x = 0

    def render(self):
        display = self.game.window.display
        display_size = self.game.window.DISPLAY_SIZE

        # BACKGROUND #
        display.blit(self.background, (0, 0))
        display.blit(self.ground, (self.ground_x,
                                   display_size[1] - self.ground.get_height()))
        display.blit(self.ground, (self.ground_x + self.ground.get_width(),
                                   display_size[1] - self.ground.get_height()))

        self.bird.render()

        if self.game.world.gameover:
            self.fade.render(display)
