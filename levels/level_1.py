from levels.abstractlevel import AbstractLevel
import pygame
import os
from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP
from components.button import Button
from gamestate import _GameState
from menustate import _MenuState
from utility import easeInBounce, easeOutBound
import math
from components.mole import Mole
from random import randrange as rand

class LevelOne(AbstractLevel):

    def __init__(self, display):
        super().__init__(display)
        self.index = 1
        pygame.mixer.music.load(os.path.join( 'assets', 'audio', "mixkit-playground-fun-12.mp3"))
        pygame.mixer.music.play(-1, fade_ms=AbstractLevel.TRANSITION_DELAY*1000)

        self.kill_count_win_bound = 10

        self.background = pygame.transform.scale(self.load_img('11_background.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        self.trees = pygame.transform.scale(self.load_img('02_trees_and_bushes.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        self.ground = pygame.transform.scale(self.load_img('01_ground.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        self.clouds = pygame.transform.scale(self.load_img('10_distant_clouds.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        self.huge_clouds = pygame.transform.scale(self.load_img('07_huge_clouds.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 

        self.timer_text = self.font.render(str(math.ceil(self.timer)), True, (255, 255, 255))
        self.timer_text_pos = self.timer_text.get_rect()
        self.timer_text_pos.y = 50
        self.timer_text_pos.x = (self.display.get_width() - self.timer_text.get_width()) / 2

        self.kill_count_text = self.font_small.render("0/{}".format(self.kill_count_win_bound), True, (255, 255, 255))
        self.kill_count_text_pos = self.kill_count_text.get_rect()
        self.kill_count_text_pos.y = 25
        self.kill_count_text_pos.x = 25

        

        self.mole_entities = [Mole(pos=(rand(self.display.get_width()/2),500)), Mole(pos=(rand(self.display.get_width()/2),500))]

    def update(self, game, dt):
        cur_pos = pygame.mouse.get_pos()
        self.cursor_img_rect = (cur_pos[0] - 13, cur_pos[1] - 51)

        
        self.timer_text = self.font.render(str(math.ceil(self.timer)), True, (255, 255, 255))
        self.timer_text_pos.x = (self.display.get_width() - self.timer_text.get_width()) / 2

        self.kill_count_text = self.font_small.render("{}/{}".format(self.kill_count, self.kill_count_win_bound), True, (255, 255, 255))

        if self.timer is not 0:
            self.timer -= dt
        elif not pygame.mixer.music.get_busy():
            game.set_state(_GameState.LEVEL_SELECT)

        if (self.timer < 0):
            self.timer = 0
            pygame.mixer.music.pause()
            if self.kill_count >= self.kill_count_win_bound:
                self.win_sound.play()
                game.level_select.unlocked_level[self.index] = True
            else:
                self.lose_sound.play()
        elif rand(30) == 0 and self.timer is not 0:
            self.mole_entities.append(Mole(pos=(rand(100, self.display.get_width()-100),rand(50, self.display.get_height() - 50))))


    def draw(self):
        self.display.blit(self.background, self.background.get_rect())
        self.display.blit(self.huge_clouds, self.huge_clouds.get_rect())
        self.display.blit(self.trees, self.trees.get_rect())
        self.display.blit(self.ground, self.ground.get_rect())
        self.display.blit(self.clouds, self.clouds.get_rect())

        self.display.blit(self.timer_text, self.timer_text_pos)
        self.display.blit(self.kill_count_text, self.kill_count_text_pos)

        for mole in [(m.sprite, m.position) for m in self.mole_entities]:
            self.display.blit(mole[0], mole[1])

        # Nothing comes after this
        self.display.blit(pygame.transform.flip(self.cursor_img, True, False), self.cursor_img_rect)

    
    def handle_event(self, game, event):
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            i = len(self.mole_entities) -1

            if (self.timer > 0):
                while i > -1:
                    mole = self.mole_entities[i]

                    if mole.contains(pos) and not mole.is_dead:
                        self.hit_sound.play()
                        self.kill_count += 1
                        mole.die()
                        #self.mol
                    
                    i -= 1


