class UI:
    def __init__(self, game):
        self.game = game

        self.buttons = {}

        self.select = ""

    def init_ui(self):
        self.select = ""
        return

    def get_buttons(self):
        return self.buttons

    def _render_buttons(self):
        display = self.game.window.display
        for button in list(self.buttons.values()):
            button.render(display)

    def update(self):
        return

    def render(self):
        display = self.game.window.display
        display.fill((255, 255, 255))
