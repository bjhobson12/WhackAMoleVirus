# File: mole.py
# Created: Tue Apr 06 2021
#
# Copyright © 2021 Foxbat

import pygame
import os


class Mole:

    RELATIVE_PATH_LIST = ["assets"]

    def __init__(self, parent_list, lifespan=2, pos=(0,0)):
        self.sprite = self.load_sprite('mole.png')
        self.position = self.sprite.get_rect()
        self.position.center = pos
        self.is_dead = False
        self.counter = 0
        self.lifespan = lifespan
        self.parent_list = parent_list

    def load_sprite(self, file_name, add_sub_dir=[], alpha=True):
        ret = pygame.image.load(os.path.join('./', *Mole.RELATIVE_PATH_LIST, 'sprites', *add_sub_dir, file_name))
        if alpha:
            return ret.convert_alpha()
        return ret

    def update(self, game, dt):
        self.counter += dt

        if self.counter >= self.lifespan or self.counter > 1 and self.is_dead:
            self.parent_list.remove(self)

    def contains(self, p):
        x, y = p
        return x > self.position.x and x < self.position.x + self.sprite.get_width() and y > self.position.y and y < self.position.y + self.sprite.get_height()

    def die(self):
        self.is_dead = True
        self.counter = 0
        self.sprite = self.load_sprite('whacked_mole.png')