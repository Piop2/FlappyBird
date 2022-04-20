class UI:
    def __init__(self, game):
        self.game = game

        self.buttons = {}
    
    def get_buttons(self):
        return self.buttons
    
    def update(self, dt):
        return
    
    def render(self):
        display = self.game.window.display
        display.fill((255, 255, 255))
        return