from levels.abstractlevel import AbstractLevel
class LevelThree(AbstractLevel):

    def __init__(self, display):
        super().__init__(display)
        self.index = 3