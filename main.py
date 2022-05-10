from scripts.core.assets import Assets
from scripts.core.window import Window
from scripts.core.renderer import Renderer
from scripts.core.input import Input
from scripts.core.world import World


class Game:
    def __init__(self):
        self.running = True

        self.assets = Assets()
        self.window = Window(self)
        self.world = World(self)
        self.renderer = Renderer(self)
        self.renderer.get_ui().init_ui()
        self.input = Input(self)

    def update(self):
        self.input.update()
        self.renderer.update()
        self.world.update()

    def run(self):
        while self.running:
            self.update()


if __name__ == '__main__':
    Game().run()
