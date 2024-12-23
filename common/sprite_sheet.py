import pygame

class SpriteSheet(object):
    def __init__(self, sheet_path):
        self.sprite_sheet = pygame.image.load(sheet_path).convert_alpha()

    def get_frame(self, x, y, width, height):
        frame = self.sprite_sheet.subsurface(pygame.Rect(x, y, width, height))
        return frame