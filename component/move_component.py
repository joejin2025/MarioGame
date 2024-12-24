import pygame

class MoveComponent(object):
    def __init__(self, speed, entity):
        self.speed = speed # 速度，只有大小
        self.velocity = 0 #速度，包含大小和方向
        self.entity = entity

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.velocity = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.velocity = self.speed
        else:
            self.velocity = 0

    def update(self, level_width):
        new_x = self.entity.rect.x + self.velocity
        if new_x < 0:
            new_x = 0
        elif new_x + self.entity.rect.width >= level_width:
            new_x = level_width - self.entity.rect.width
        self.entity.rect.x = new_x