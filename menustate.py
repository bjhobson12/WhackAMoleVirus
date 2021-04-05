from enum import Enum

class _MenuState(Enum):
    TRANSITION_IN, TRANSITION_OUT, STATIC = range(3)