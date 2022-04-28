from scripts.core.load_f import load_json, load_image
from scripts.animation import Animation


class Configs:
    def __init__(self):
        configs = load_json("assets/config.json")
        game = configs["Game"]
        window = configs["Window"]
        render = configs["Render"]
        vfx = configs["Vfx"]
        debug = configs["Debug"]

        # Game #
        self.bird_speed = game["BirdSpeed"]

        # Window #
        self.caption = window["Caption"]
        self.window_size = window["WindowSize"]
        self.fullscreen = window["FullScreen"]

        # Render #
        self.fps = render["Fps"]
        image_animation = render["ImageAnimation"]
        menu_title = image_animation["MenuUiTitle"]
        self.t_menu_movement = menu_title["MovementRange"]
        self.t_menu_speed = menu_title["Speed"]
        self.t_menu_cool = menu_title["CoolTime"]

        # vfx #
        self.ui_fadeout_s = vfx["UiFadeOutSpeed"]

        # Settings #
        self.screen_modes = window["WindowModes"]
        self.fps_modes = render["FpsModes"]

        # Debugs #
        self.show_fps = debug["ShowFps"]


class Images:
    def __init__(self):
        self.icon = load_image("assets/images/icon/icon_50.png")

        self.bird_ani = Animation.load("assets/images/bird")

        self.background = load_image("assets/images/background.png")
        self.ground = load_image("assets/images/ground.png")

        # MenuUI #
        self.t_flappy_bird = load_image("assets/images/titles/flappy_bird.png")
        self.copyright = load_image("assets/images/copyright.png")
        self.b_start = load_image("assets/images/buttons/start.png")
        self.b_score = load_image("assets/images/buttons/score.png")


class Sounds:
    def __init__(self):
        pass


class Fonts:
    def __init__(self):
        pass


class Assets:
    def __init__(self):
        self.configs = Configs()
        self.images = Images()
        self.sounds = Sounds()
        self.fonts = Fonts()
