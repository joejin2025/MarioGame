import pygame

class Mario(pygame.sprite.Sprite):
    def __init__(self, screen, sprite_sheet, sprite_manager, x, y):
        self.screen = screen
        self.sprite_sheet = sprite_sheet
        self.sprite_data_dict = sprite_manager.get_sprite_dict()

        self.rect = pygame.Rect(x, y, 0, 0)

        self.run_index = 0
        # 设置images
        self.current_image = None
        self.run_images = None
        self.idle_image = None
        self.init_images()

        self.timer = 0
        self.delta_time = 7

        self.idle()

    def init_images(self):
        self.idle_image = self.sprite_data_dict["mario_idle"]
        self.run_images = [
            self.sprite_data_dict["mario_run_1"],
            self.sprite_data_dict["mario_run_2"],
            self.sprite_data_dict["mario_run_3"],
        ]

    def idle(self):
        self.current_image = self.idle_image
        self.update_rect()

    def update_rect(self):
        self.rect.width = self.current_image.frame_width
        self.rect.height = self.current_image.frame_height

    def run(self):
        self.timer += 1
        if self.timer % self.delta_time == 0:
            self.run_index = (self.run_index + 1) % len(self.run_images)
            self.current_image = self.run_images[self.run_index]
            self.update_rect()

    def draw(self):
        self.screen.blit(self.current_image.image, self.rect)