from scripts.ui.basic_ui import UI

from scripts.effect.vfx import FadeIn


class GameUI(UI):
    def __init__(self, game):
        super().__init__(game)

        self.background = game.assets.images.background
        self.ground = game.assets.images.ground
        self.ground_x = 0
        self.ground_speed = game.assets.configs.bird_speed

        self.tap = game.assets.images.tap
        self.tap_y = 85
        self.tap_alpha = 0
        self.tap_breath_direction = 1
        self.tap_breath_speed = 4

        self.bird = self.game.world.bird

        self.buttons = {}

        self.fade = FadeIn((255, 255, 255), game.assets.configs.gameover_fadeout_s)

    def init_ui(self):
        self.ground_x = 0
        self.fade.init_alpha()
        self.bird.image.speed = self.game.assets.configs.game_ready_ani_speed
        self.bird.image.play()

        self.game.world.init_world()

    def update(self):
        dt = self.game.renderer.dt
        world = self.game.world

        if world.mode == "ready":
            if self.game.input.jump:
                self.bird.image.speed = self.game.assets.configs.game_start_ani_speed

            self.tap_alpha += self.tap_breath_direction * self.tap_breath_speed
            if self.tap_alpha <= 0 or self.tap_alpha >= 255:
                self.tap_breath_direction *= -1

        if self.game.world.gameover:
            is_faded = self.fade.update(dt)
            self.bird.image.pause()
        else:
            self.ground_x -= self.ground_speed * dt
            if self.ground_x <= - self.ground.get_width():
                self.ground_x = 0

        self.bird.update()

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

        if self.game.world.mode == "ready":
            self.tap.set_alpha(self.tap_alpha)
            display.blit(self.tap, ((display_size[0] / 2) - (self.tap.get_width() / 2), self.tap_y))

        if self.game.world.gameover:
            self.fade.render(display)
