import pygame

class SpriteImage(object):
    def __init__(self, image, frame_width, frame_height):
        self.image = image
        self.frame_width = frame_width
        self.frame_height = frame_height

    def copy(self):
        return SpriteImage(self.image.copy(), self.frame_width, self.frame_height)