import pygame
from pygame import K_SPACE


class InputController(object):
    def __init__(self, entity):
        self.entity = entity

    def check_input(self):
        self.check_keyboard_input()

    def check_keyboard_input(self):
        pressed_keys = pygame.key.get_pressed()

        is_jumping = pressed_keys[K_SPACE]
        self.entity.jump(is_jumping)