# File: playersprite.py
# Created: Tue Apr 06 2021
#
# Copyright © 2021 Foxbat

import os
from .abstractSprite import AbstractSprite, Frame

class PlayerSprite(AbstractSprite):

    def __init__(self, display):
        super().__init__(display)
        self.frames.append(Frame(self.load_sprite("run-1.png"), 0.2))
        self.frames.append(Frame(self.load_sprite("run-2.png"), 0.2))
        self.frames.append(Frame(self.load_sprite("run-3.png"), 0.2))
        self.frames.append(Frame(self.load_sprite("run-4.png"), 0.2))
        self.frames.append(Frame(self.load_sprite("run-5.png"), 0.2))
        self.frames.append(Frame(self.load_sprite("run-6.png"), 0.2))
        self.frames.append(Frame(self.load_sprite("run-7.png"), 0.2))
        self.frames.append(Frame(self.load_sprite("run-8.png"), 0.2))
        self.reset()

    def draw(self, x, y):
        self.display.blit(self.frames[self.frame_index].sprite, (x, y))
    
    def update(self, dt):
        if self.animating:
            self.timer += dt
            print(self.timer)
            if self.timer >= self.frames[self.frame_index].duration:
                self.timer = 0
                self.frame_index = (self.frame_index + 1) % len(self.frames)
