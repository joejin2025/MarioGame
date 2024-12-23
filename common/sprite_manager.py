import json
import os
import util.path
from common.sprite_sheet import SpriteSheet
from common.sprite_image import SpriteImage

class SpriteManager(object):
    def __init__(self):
        self.sprite_dict = self._load_spirtes([
            os.path.join(util.path.get_root_path(), "assets/sprites/mario.json"),
        ])

    def _load_spirtes(self, paths):
        res = {}
        for path in paths:
            with open(path, "r") as sprite_f:
                sprite_json = json.load(sprite_f)
                sprite_sheet = SpriteSheet(sprite_json["sprite_sheet_path"])
                frame_width, frame_height = sprite_json["frame_size"]
                for sprite_data in sprite_json["sprites"]:
                    img = sprite_sheet.get_frame(
                        sprite_data["x"],
                        sprite_data["y"],
                        frame_width,
                        frame_height,
                    )
                    res[sprite_data["name"]] = SpriteImage(img, frame_width, frame_height)
        return res

    def get_sprite_dict(self):
        return self.sprite_dict