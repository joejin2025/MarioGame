import pygame
import sys
import os
import json

import util.path
from entity.camera import Camera
from entity.level import Level
from entity.mario import Mario
from common.sprite_manager import SpriteManager

# 读取配置文件
with open("config.json", "r") as f:
    config = json.load(f)

# 初始化 pygame
pygame.init()

# 设置游戏窗口的大小
screen = pygame.display.set_mode((config["screen_width"], config["screen_height"]))

# 设置窗口标题
pygame.display.set_caption(config["title"])

# 设置游戏的帧率
clock = pygame.time.Clock()

sprites_manager = SpriteManager()

camera = Camera(config["screen_width"], config["screen_height"])

mario = Mario(screen, sprites_manager, 100, 480 - 96, config["frame_rate"])

level = Level(screen, sprites_manager, 32)
level.load(os.path.join(util.path.get_root_path(), "assets/level/level1-1.json"))
# 游戏主循环
while True:
    dt = clock.tick(config["frame_rate"]) / 1000.0

    # 处理事件（比如关闭窗口）
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 填充背景色
    screen.fill(tuple(config["bg_color"]))

    keys = pygame.key.get_pressed()

    mario.update(keys, dt, level.level_width, level.level_height)
    camera.update(mario.rect, level.level_width, level.level_height)
    level.update()

    level.draw(camera)
    mario.draw(camera)


    # 更新显示
    pygame.display.update()

    # 设置游戏的帧率（从配置文件中获取）
    clock.tick(config["frame_rate"])