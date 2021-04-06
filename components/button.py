from gamestate import _GameState


class Button:

    def __init__(self, display, button, pos, font=None, text=None, text_color=(255, 255, 255)):
        self.display = display
        self.button = button
        self.button_rect = self.button.get_rect()
        self.button_rect.center = pos
        self.font = font
        self.disabled = False
        self.text = None

        if self.font:
            self.text = self.font.render(text, True, text_color)

    def update(self, game, dt):
        pass

    def draw(self):
        self.display.blit(self.button, self.button_rect)
        
        if self.text is not None:
            self.display.blit(self.text, (self.button_rect.x + int((self.button.get_width() - self.text.get_width())/2), self.button_rect.y + int((self.button.get_height() - self.text.get_height())/2)))

    def contains(self, pos):
        x, y = pos
        return x > self.button_rect.x and x < self.button_rect.x + self.button_rect.width and y > self.button_rect.y and y < self.button_rect.y + self.button_rect.height