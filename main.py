from scripts.assets import Assets
from scripts.window import Window
from scripts.renderer import Renderer
from scripts.input import Input

class Game:
    def __init__(self):
        self.running = True

        self.assets = Assets()
        self.window = Window()
        self.renderer = Renderer(self)
        self.input = Input(self)
    
    def update(self):
        self.renderer.update()
        self.input.update()
    
    def run(self):
        while self.running:
            self.update()

if __name__=='__main__':
    Game().run()
