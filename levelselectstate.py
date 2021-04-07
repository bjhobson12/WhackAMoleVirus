# File: levelselectstate.py
# Created: Tue Apr 06 2021
#
# Copyright © 2021 Foxbat

from enum import Enum

class _LevelSelectState(Enum):
    EARTH_WORLD, ROCK_WORLD, ICE_WORLD, TRANSITION_RIGHT, TRANSITION_LEFT = range(5)