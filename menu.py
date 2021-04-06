import pygame
import os

class Menu:

    RELATIVE_PATH_LIST = ['assets', 'fonts']

    def __init__(self, display):
        self.display = display
        self.font = self.load_font("LuckiestGuy-Regular.ttf", 100)
        self.menu_text = self.font.render('Whack A\nMole', True, (0, 0, 0))
        self.menu_text_offset = (self.display.get_width() - self.menu_text.get_width()) / 2.0
        

    def draw(self):
        self.display.blit(self.menu_text, (int(self.menu_text_offset), 20))

    def update(self, dt):
        pass

    def load_font(self, file_name, size):
        return pygame.font.Font(os.path.join(os.getcwd(), *Menu.RELATIVE_PATH_LIST, file_name), size)