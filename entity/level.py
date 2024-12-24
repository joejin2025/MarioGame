import json

import pygame

from entity.background import Ground, Sky


class Level(object):
    def __init__(self, screen, sprite_manager, tile_size):
        self.screen = screen
        self.sprite_data_dict = sprite_manager.get_sprite_dict()

        self.tile_size = tile_size
        self.backgrounds = pygame.sprite.Group()

        self.level_width = self.level_height = 0

    def load(self, level_file):
        with open(level_file, 'r') as f:
            level_data = json.load(f)
            self.level_width = len(level_data[0]) * self.tile_size
            self.level_height = len(level_data) * self.tile_size
            for row_idx, row in enumerate(level_data):
                for col_idx, tile in enumerate(row):
                    x = col_idx * self.tile_size
                    y = row_idx * self.tile_size
                    if tile == '#':
                        bg_ground = Ground(self.sprite_data_dict["ground"], x, y)
                        self.backgrounds.add(bg_ground)
                    elif tile == ' ':
                        bg_sky = Sky(self.sprite_data_dict["sky"], x, y)
                        self.backgrounds.add(bg_sky)

    def draw(self, camera):
        for bg in self.backgrounds.sprites():
            bg.draw(self.screen, camera)

    def update(self):
        self.backgrounds.update()
