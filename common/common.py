from enum import Enum

class Direction(Enum):
    LEFT = 0
    RIGHT = 1

class MarioState(Enum):
    IDLE = 0
    MOVE = 1
    JUMP = 2