from scripts.utils.load_f import load_image, load_json
from scripts.utils.clip import clip


def load_animation(path):
    cfg = load_json(f"{path}/config.json")
    img = load_image(f"{path}/images.png")

    animation_data = []
    for data in cfg.values():
        x = data["x"]
        y = data["y"]
        w = data["w"]
        h = data["h"]
        d = data["d"]

        image = clip(img, x, y, w, h)

        animation_data.append({"image": image, "d": d})
    return tuple(animation_data)


class Animation:

    @staticmethod
    def load(path):
        return Animation(load_animation(path))

    def __init__(self, ani_data):
        self.ani_data = ani_data
        self._pause = False
        self.layer = 0
        self._speed = 1
        self.frame = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        self._speed = float(new_speed)

    def get(self):
        return self.ani_data[self.layer]["image"]

    def pause(self):
        self._pause = True

    def play(self):
        self._pause = False

    def update(self, dt):
        if not self._pause:
            self.frame += dt / 1000 * self.speed
            if self.frame >= self.ani_data[self.layer]["d"]:
                self.frame = 0
                if self.layer >= len(self.ani_data) - 1:
                    self.layer = 0
                else:
                    self.layer += 1

    def render(self, surf, pos):
        surf.blit(self.get(), pos)