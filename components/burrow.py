import pygame
import os


class Burrow:

    RELATIVE_PATH_LIST = ["assets"]

    def __init__(self, parent_list, hole_num, lifespan=2):
        self.hole_num = hole_num
        self.sprite = pygame.transform.scale(self.load_sprite('door.png'), (100, 115))
        self.counter = 0
        self.lifespan = lifespan
        self.parent_list = parent_list

    def load_sprite(self, file_name, add_sub_dir=[], alpha=True):
        ret = pygame.image.load(os.path.join('./', *Burrow.RELATIVE_PATH_LIST, 'sprites', *add_sub_dir, file_name))
        if alpha:
            return ret.convert_alpha()
        return ret

    def update(self, game, dt):
        self.counter += dt

        if self.counter >= self.lifespan:
            self.parent_list.remove(self)

    def contains(self, p):
        x, y = p
        return x > self.position.x and x < self.position.x + self.sprite.get_width() and y > self.position.y and y < self.position.y + self.sprite.get_height()