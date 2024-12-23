import pygame

# Mario 类
class Mario:
    def __init__(self, x, y, image_path):
        # 加载玛丽的图像
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x  # 设置玛丽的初始x坐标
        self.rect.y = y  # 设置玛丽的初始y坐标
        self.speed = 5  # 设置移动速度

    def move(self, keys):
        # 控制玛丽的左右移动
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def draw(self, screen):
        # 在屏幕上绘制玛丽
        screen.blit(self.image, self.rect)