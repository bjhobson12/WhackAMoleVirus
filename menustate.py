# File: menustate.py
# Created: Tue Apr 06 2021
#
# Copyright © 2021 Foxbat

from enum import Enum

class _MenuState(Enum):
    TRANSITION_IN, TRANSITION_OUT, STATIC = range(3)