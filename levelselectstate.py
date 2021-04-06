from enum import Enum

class _LevelSelectState(Enum):
    EARTH_WORLD, ROCK_WORLD, ICE_WORLD, TRANSITION_RIGHT, TRANSITION_LEFT = range(5)