import pygame

class AnimationComponent(object):
    def __init__(self, sprite_dict, state, animations, entity, frame_rate):
        self.current_state = state
        self.all_frames = {
            state: [sprite_dict[name] for name in animations[state]] for state in animations.keys()
        }
        self.entity = entity
        self.current_frame_index = 0
        self.current_frame = self.all_frames[self.current_state][self.current_frame_index]
        self.time_since_last_frame = 0
        self.frame_rate = frame_rate

    def set_state(self, state):
        if self.current_state != state:
            self.current_state = state
            self.current_frame_index = self.time_since_last_frame = 0
            self.current_frame = self.all_frames[self.current_state][self.current_frame_index]

    def update(self, dt):
        self.time_since_last_frame += dt
        if self.time_since_last_frame >= 1 / self.frame_rate:
            self.time_since_last_frame = 0
            self.current_frame_index = (self.current_frame_index + 1) % len(self.all_frames[self.current_state])
            self.current_frame = self.all_frames[self.current_state][self.current_frame_index]
        self.entity.set_image(self.current_frame)