from scripts.button import Button


class MenuUI:
    def __init__(self, game):
        self.game = game

        self.background = game.assets.images.background
        self.ground = game.assets.images.ground
        self.ground_x = 0
        self.ground_speed = game.assets.configs.bird_speed

        self.copyright = game.assets.images.copyright

        self.buttons = {
            "start": Button(game.assets.images.b_start, (20, 160)),
            "share": Button(game.assets.images.b_score, (84, 160))
        }

    def update(self):
        dt = self.game.renderer.dt
        self.ground_x -= self.ground_speed * dt
        if self.ground_x <= - self.ground.get_width():
            self.ground_x = 0

    def render(self):
        display = self.game.window.display

        # BACKGROUND #
        display.blit(self.background, (0, 0))
        display.blit(self.ground, (self.ground_x,
                                   self.game.window.DISPLAY_SIZE[1] - self.ground.get_height()))
        display.blit(self.ground, (self.ground_x + self.ground.get_width(),
                                   self.game.window.DISPLAY_SIZE[1] - self.ground.get_height()))
        display.blit(self.copyright, ((self.game.window.DISPLAY_SIZE[0] / 2) - (self.copyright.get_width() / 2),
                                      215))

        # buttons #
        for button in list(self.buttons.values()):
            button.render(display)
