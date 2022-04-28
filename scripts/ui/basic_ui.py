class UI:
    def __init__(self, game):
        self.game = game

        self._buttons = {}

    def init_ui(self):
        return

    @property
    def buttons(self):
        return self._buttons

    def update(self):
        return

    def render(self):
        display = self.game.window.display
        display.fill((255, 255, 255))
