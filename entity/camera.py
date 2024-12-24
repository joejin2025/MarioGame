

class Camera(object):
    def __init__(self, width, height):
        self.offset_x = 0
        self.offset_y = 0
        self.width = width
        self.height = height

    def apply(self, rect):
        return rect.move(self.offset_x, self.offset_y)

    def update(self, target_rect, level_width, level_height):
        # 计算目标的中心与屏幕中心的偏移量
        self.offset_x = -target_rect.centerx + self.width // 2
        self.offset_y = -target_rect.centery + self.height // 2

        # 限制相机范围
        self.offset_x = max(min(0, self.offset_x), -(level_width - self.width))
        self.offset_y = max(min(0, self.offset_y), -(level_height - self.height))