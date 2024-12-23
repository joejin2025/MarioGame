import pygame
import sys
import json

from entity.mario import Mario
from common.sprite_sheet import SpriteSheet
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

characters_sprite_sheet = SpriteSheet("./assets/image/characters.gif")
sprites_manager = SpriteManager()
print(sprites_manager.get_sprite_dict())
mario = Mario(screen, characters_sprite_sheet, sprites_manager, 100, 300)

# 游戏主循环
while True:
    # 处理事件（比如关闭窗口）
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 填充背景色
    screen.fill(tuple(config["bg_color"]))

    keys = pygame.key.get_pressed()

    mario.update(keys)

    mario.draw()

    # 更新显示
    pygame.display.update()

    # 设置游戏的帧率（从配置文件中获取）
    clock.tick(config["frame_rate"])