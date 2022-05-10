class UI:
    def __init__(self, game):
        self.game = game

        self._buttons = {}

        self.select = ""

    def init_ui(self):
        self.select = ""
        return

    @property
    def buttons(self):
        return self._buttons

    def _render_buttons(self):
        display = self.game.window.display
        for button in list(self.buttons.values()):
            button.render(display)

    def update(self):
        return

    def render(self):
        display = self.game.window.display
        display.fill((255, 255, 255))
