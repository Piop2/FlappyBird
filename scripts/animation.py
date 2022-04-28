from scripts.core.load_f import load_image, load_json
from scripts.core.clip import clip


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

        animation_data.append({"image": image, "d": int(d)})
    return tuple(animation_data)


class Animation:

    @staticmethod
    def load(path):
        return Animation(load_animation(path))

    def __init__(self, ani_data):
        self.ani_data = ani_data
        self.layer = 0
        self._speed = 1
        self.frame = 0
        self.pause = False

    @property
    def image(self):
        return self.ani_data[self.layer]["image"]

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        self._speed = new_speed

    def play(self):
        self.pause = False

    def stop(self):
        self.pause = True

    def update(self, dt):
        if not self.pause:
            self.frame += dt / 10 * self.speed
            if self.frame >= self.ani_data[self.layer]["d"]:
                self.frame = 0
                if self.layer >= len(self.ani_data):
                    self.layer = 0
                else:
                    self.layer += 1

    def render(self, surf, pos):
        surf.blit(self.image, pos)
