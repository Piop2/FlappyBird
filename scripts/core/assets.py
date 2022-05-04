from scripts.utils.load_f import load_json, load_image
from scripts.animation import Animation

from scripts.font import Font

class Configs:
    def __init__(self):
        configs = load_json("assets/config.json")

        # Game #
        game = configs["Game"]

        self.bird_speed = game["BirdSpeed"]

        # Window #
        window = configs["Window"]

        self.caption = window["Caption"]
        self.window_size = window["WindowSize"]
        self.fullscreen = window["FullScreen"]

        # Render #
        render = configs["Render"]

        self.fps = render["Fps"]
        
        font = render["Font"]
        
        self.big_score_font_space = font["BigScoreFont"]["Space"]
        self.small_score_font_space = font["SmallScoreFont"]["Space"]

        ui = render["UI"]

        menu_ui = ui["MenuUI"]
        
        menu_title = menu_ui["Title"]

        self.t_menu_movement = menu_title["MovementRange"]
        self.t_menu_speed = menu_title["Speed"]
        self.t_menu_cool = menu_title["CoolTime"]

        self.menu_bird_speed = menu_ui["Bird"]["Speed"]

        # vfx #
        vfx = configs["Vfx"]
        
        self.ui_fadeout_s = vfx["UiFadeOutSpeed"]

        # Settings #
        self.screen_modes = window["WindowModes"]
        self.fps_modes = render["FpsModes"]

        # Debugs #
        debug = configs["Debug"]

        self.show_fps = debug["ShowFps"]


class Images:
    def __init__(self):
        self.icon = load_image("assets/images/icon/icon_50.png")

        self.bird_ani = Animation.load("assets/images/bird")

        self.menu_bird_ani = Animation.load("assets/images/bird")

        self.top_pipe = load_image("assets/images/pipes/top.png")
        self.ground_pipe = load_image("assets/images/pipes/ground.png")

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
    def __init__(self, assets):
        self.big_score_font = Font.load("assets/fonts/big_score_font.png", assets.configs.big_score_font_space)
        self.small_score_font = Font.load("assets/fonts/small_score_font.png", assets.configs.small_score_font_space)

class Assets:
    def __init__(self):
        self.configs = Configs()
        self.images = Images()
        self.sounds = Sounds()
        self.fonts = Fonts(self)