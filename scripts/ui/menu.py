from scripts.ui.basic_ui import UI

from scripts.button import Button


class MenuUI(UI):
    def __init__(self, game):
        super().__init__(game)

        self.background = game.assets.images.background
        self.ground = game.assets.images.ground
        self.ground_x = 0
        self.ground_speed = game.assets.configs.bird_speed

        self.bird = game.assets.images.menu_bird_ani  # animation
        self.bird.speed = game.assets.configs.menu_bird_ani_speed

        self.title = game.assets.images.t_flappy_bird
        self.title_direction = -1
        self.title_go = True
        self.title_cool_timer = 0
        self.title_movement = self.game.assets.configs.t_menu_movement
        self.title_speed = self.game.assets.configs.t_menu_speed
        self.title_origin_y = 40
        self.title_y = self.title_origin_y + self.title_movement

        self.copyright = game.assets.images.copyright

        self.buttons = {
            "start": Button(game.assets.images.b_start, (20, 160)),
            "score": Button(game.assets.images.b_score, (84, 160))
        }
        self.select = ""

    def init_ui(self):
        self.ground_x = 0

        self.title_y = self.title_origin_y + self.title_movement
        self.title_direction = -1
        self.title_go = True
        self.title_cool_timer = 0

        self.select = ""

    def update(self):
        dt = self.game.renderer.dt

        self.bird.update(dt)

        self.ground_x -= self.ground_speed * dt
        if self.ground_x <= - self.ground.get_width():
            self.ground_x = 0

        if self.title_go:
            self.title_y += self.title_direction * self.title_speed
            if abs(self.title_y - self.title_origin_y) >= self.title_movement:
                if self.title_direction == -1:
                    self.title_go = False

                self.title_y = self.title_origin_y + (self.title_direction * self.title_movement)
                self.title_direction *= -1
        else:
            self.title_cool_timer += dt / 1000
            if self.title_cool_timer >= self.game.assets.configs.t_menu_cool:
                self.title_cool_timer = 0
                self.title_go = True

        # button #
        if self.select == "start":
            self.game.renderer.set_ui("game")
        elif self.select == "score":
            self.select = ""

    def render(self):
        display = self.game.window.display
        display_size = self.game.window.DISPLAY_SIZE

        # BACKGROUND #
        display.blit(self.background, (0, 0))
        display.blit(self.ground, (self.ground_x,
                                   display_size[1] - self.ground.get_height()))
        display.blit(self.ground, (self.ground_x + self.ground.get_width(),
                                   display_size[1] - self.ground.get_height()))
        display.blit(self.copyright, ((display_size[0] / 2) - (self.copyright.get_width() / 2),
                                      215))

        # buttons #
        self._render_buttons()

        display.blit(self.title, (15, self.title_y))

        self.bird.render(display, (116, self.title_y + 5))
