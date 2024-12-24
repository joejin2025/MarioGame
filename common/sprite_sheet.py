import pygame

class SpriteSheet(object):
    def __init__(self, sheet_path):
        self.sprite_sheet = pygame.image.load(sheet_path).convert_alpha()

    def get_frame(self, x, y, scale_factor, ignore_tilesize=False, width=16, height=16):
        if ignore_tilesize:
            rect = pygame.Rect(x, y, width, height)
        else:
            rect = pygame.Rect(x * width, y * height, width, height)
        frame = self.sprite_sheet.subsurface(rect)
        # return frame
        return pygame.transform.scale(frame, (width * scale_factor, height * scale_factor))