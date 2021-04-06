

class AbstractLevel:

    def __init__(self, display):
        self.display = display

    def reset(self):
        pass

    def update(self, game, dt):
        pass

    def draw(self):
        self.display.fill((255, 100, 100))

    def handle_event(self, game, event):
        pass