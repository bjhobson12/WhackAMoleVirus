from enum import Enum

class _GameState(Enum):
    MENU, LEVEL_SELECT, PLAYING, WIN, LOSE, SETTINGS, EXIT = range(7)