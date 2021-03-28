import pygame
import os

class Frame:

    def __init__(self, sprite, duration):
        self.sprite = sprite
        self.duration = duration

class AbstractSprite(pygame.sprite.Sprite):

    RELATIVE_PATH_LIST = ['assets', 'sprites']

    def __init__(self, display):
        super().__init__()
        self.display = display
        self.frames = []

    def reset(self):
        self.frame_index = 0
        self.timer = 0
        self.animating = True

    def load_sprite(self, file_name):
        return pygame.image.load(os.path.join(os.getcwd(), *AbstractSprite.RELATIVE_PATH_LIST, file_name)).convert_alpha()
    

