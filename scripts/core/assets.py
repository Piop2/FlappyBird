from scripts.utils.load_f import load_json, load_image
from scripts.animation import Animation

from scripts.font import Font


class Data:
    def __init__(self):
        self.player_name = "Ploppy"
        self.best_score = 0


class Configs:
    def __init__(self):
        configs = load_json("assets/config.json")

        # Game #
        game = configs["Game"]

        bird = game["Bird"]
        self.bird_start_pos = bird["StartPos"]
        self.bird_speed = bird["Speed"]
        self.bird_jump_power = bird["JumpPower"]
        self.bird_max_height = bird["MaxHeight"]

        self.gravity = game["Gravity"]

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

        self.menu_bird_ani_speed = menu_ui["Bird"]["AnimationSpeed"]

        game_ui = ui["GameUI"]

        self.game_ready_ani_speed = game_ui["Ready"]["AnimationSpeed"]

        self.game_start_ani_speed = game_ui["Start"]["AnimationSpeed"]

        tap = game_ui["Tap"]
        self.tap_breath_speed = tap["BreathSpeed"]

        # vfx #
        vfx = configs["Vfx"]

        self.ui_fadeout_s = vfx["UIFadeOutSpeed"]
        self.gameover_fadeout_s = vfx["GameOverFadeOutSpeed"]

        # Settings #
        self.screen_modes = window["WindowModes"]
        self.fps_modes = render["FpsModes"]

        # Debugs #
        debug = configs["Debug"]

        self.show_fps = debug["ShowFps"]


class Images:
    def __init__(self):
        self.icon = load_image("assets/images/icon/icon_50.png")

        self.bird = load_image("assets/images/bird.png")

        self.game_bird_ani = Animation.load("assets/images/bird")

        self.menu_bird_ani = Animation.load("assets/images/bird")

        self.top_pipe = load_image("assets/images/pipes/top.png")
        self.bottom_pipe = load_image("assets/images/pipes/bottom.png")

        self.background = load_image("assets/images/background.png")
        self.ground = load_image("assets/images/ground.png")

        # MenuUI #
        self.t_flappy_bird = load_image("assets/images/titles/flappy_bird.png")
        self.copyright = load_image("assets/images/copyright.png")
        self.b_start = load_image("assets/images/buttons/start.png")
        self.b_score = load_image("assets/images/buttons/score.png")

        # GameUI #
        self.tap = load_image("assets/images/tap.png")

class Sounds:
    def __init__(self):
        pass


class Fonts:
    def __init__(self, assets):
        self.big_score_font = Font.load("assets/fonts/big_score_font.png", assets.configs.big_score_font_space)
        self.small_score_font = Font.load("assets/fonts/small_score_font.png", assets.configs.small_score_font_space)


class Assets:
    def __init__(self):
        self.data = Data()
        self.configs = Configs()
        self.images = Images()
        self.sounds = Sounds()
        self.fonts = Fonts(self)

    def save_all(self):
        return
