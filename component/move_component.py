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

    def update(self):
        self.entity.rect.x += self.velocity