from enum import Enum

import pygame

from assets.component.animation_component import AnimationComponent
from assets.component.jump_component import JumpComponent
from assets.component.move_component import MoveComponent


class MarioState(Enum):
    IDLE = 0
    MOVE = 1
    JUMP = 2


mario_animations = {
    MarioState.IDLE: ["mario_idle"],
    MarioState.MOVE: ["mario_run_1", "mario_run_2", "mario_run_3"],
    MarioState.JUMP: ["mario_jump"],
}


class Mario(pygame.sprite.Sprite):
    def __init__(self, screen, sprite_sheet, sprite_manager, x, y, frame_rate):
        self.screen = screen
        self.sprite_sheet = sprite_sheet
        self.sprite_data_dict = sprite_manager.get_sprite_dict()

        self.rect = pygame.Rect(x, y, 0, 0)

        self.current_state = MarioState.IDLE
        # 设置components
        self.move_component = MoveComponent(6, self)
        self.jump_component = JumpComponent(12, 0.8, self)
        self.animation_component = AnimationComponent(
            self.sprite_data_dict,
            self.current_state,
            mario_animations,
            self,
            frame_rate
        )

    def set_image(self, image):
        self.current_image = image
        self.rect.width = self.current_image.frame_width
        self.rect.height = self.current_image.frame_height

    def handle_input(self, keys):
        self.move_component.move(keys)
        if keys[pygame.K_SPACE]:
            self.jump_component.jump()

    def update(self, keys, dt):
        self.handle_input(keys)

        self.move_component.update()
        self.jump_component.update()

        if not self.jump_component.on_ground:
            self.animation_component.set_state(MarioState.JUMP)
        elif self.move_component.velocity != 0:
            self.animation_component.set_state(MarioState.MOVE)
        else:
            self.animation_component.set_state(MarioState.IDLE)

        self.animation_component.update(dt)

    def draw(self):
        self.screen.blit(self.current_image.image, self.rect)
