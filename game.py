import pygame
import time
from pygame.locals import MOUSEBUTTONDOWN
import pygame.freetype
from pygame import gfxdraw
from math import sqrt
import random
from enum import Enum
import os
from sys import exit
from menu import Menu
from sprites.playerSprite import PlayerSprite
from gamestate import _GameState


def distance(a, b):
    x1, y1 = a
    x2, y2 = b
    x2s = (x2 - x1)**2
    y2s = (y2 - y1)**2

    return sqrt(x2s + y2s)

class WhackAMole:

    # Colors
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    SKY_BLUE = (40,151,255)

    # Consts
    FPS = 27

    def __init__(self):

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.7)

        # Set up display
        self.display = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Whack A Mole")

        #setting constants
        self.scrWidth, self.scrHeight = self.display.get_size()
        self.clock = pygame.time.Clock()

        self.background_color = self.WHITE
        self.menu = None

        pygame.mouse.set_visible(False)

        self.set_state(_GameState.MENU)

    def set_state(self, state):
        # Do stuff
        if state == _GameState.MENU:
            pygame.mixer.music.load(os.path.join( './assets', 'audio', "mixkit-games-worldbeat-466.mp3"))
            pygame.mixer.music.play(-1)
            if self.menu is None:
                self.menu = Menu(self.display)
        elif state == _GameState.LEVEL_SELECT:
            pass
        elif state == _GameState.PLAYING:
            self.player = PlayerSprite(self.display)
            pass
        elif state == _GameState.EXIT:
            pass
        elif state == _GameState.SETTINGS:
            pass

        self.state = state

    def process_game_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.set_state(GameState.EXIT)
                break

            if self.state == _GameState.MENU:
                self.menu.handle_event(self, event)
            elif self.state == _GameState.LEVEL_SELECT:
                pass
            elif self.state == _GameState.PLAYING:
                self.player.handle_event(event)
                pass
            elif self.state == _GameState.EXIT:
                pass
                

    def main(self):

        #run game until exits
        while self.state != _GameState.EXIT:
            dt = self.clock.tick(self.FPS) / 1000
            self.display.fill(self.background_color)
            self.process_game_events()

            if self.state == _GameState.MENU:
                self.menu.update(self, dt)
                self.menu.draw()
            elif self.state == _GameState.LEVEL_SELECT:
                pass
            elif self.state == _GameState.PLAYING:
                self.player.update(dt)
                self.player.draw(100, 100)
                pass
            elif self.state == _GameState.EXIT:
                pass
            elif self.state == _GameState.SETTINGS:
                pass
            else:
                raise ValueError("You passed an invalid state variable to set_state")

            

            pygame.display.update()
            
        pygame.display.quit()
        pygame.quit()
        exit()



# This line allows you to be able to just run this file independent of the virus 'main.py'
demonstration = WhackAMole()
demonstration.main()