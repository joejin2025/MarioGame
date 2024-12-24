import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        pass

    def draw(self, surface, camera):
        surface.blit(self.image, camera.apply(self.rect))


class Ground(Background):
    pass


class Sky(Background):
    pass
