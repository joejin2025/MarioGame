import pygame

class JumpComponent(object):
    def __init__(self, jump_height, gravity, entity):
        self.entity = entity
        self.jump_height = jump_height
        self.gravity = gravity
        self.on_ground = True
        self.is_jumping = False
        self.velocity = 0
        self.entity = entity

    def jump(self):
        if self.on_ground:
            self.is_jumping = True
            self.velocity = -self.jump_height
            self.on_ground = False

    def update(self):
        if not self.on_ground:
            self.velocity += self.gravity
            self.entity.rect.y += self.velocity
            if self.entity.rect.y >= 300:
                self.entity.rect.y = 300
                self.velocity = 0
                self.on_ground = True
                self.is_jumping = False