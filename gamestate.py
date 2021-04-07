# File: gamestate.py
# Created: Tue Apr 06 2021
#
# Copyright © 2021 Foxbat

from enum import Enum

class _GameState(Enum):
    MENU, LEVEL_SELECT, PLAYING, WIN, LOSE, SETTINGS, EXIT = range(7)