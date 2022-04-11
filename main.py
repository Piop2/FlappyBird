from scripts.assets import Assets
from scripts.window import Window
from scripts.renderer import Renderer
from scripts.input import Input
from scripts.world import World


class Game:
    def __init__(self):
        self.running = True

        self.assets = Assets()
        self.window = Window(self)
        self.renderer = Renderer(self)
        self.input = Input(self)
        self.world = World(self)

    def update(self):
        self.renderer.update()
        self.input.update()
        self.world.update()

    def run(self):
        while self.running:
            self.update()


if __name__ == '__main__':
    Game().run()
