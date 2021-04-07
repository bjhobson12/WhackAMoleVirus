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
from components.burrow import Burrow
from components.trapdoor import TrapDoor
from random import randrange as rand

class LevelFive(AbstractLevel):

    def __init__(self, display):
        super().__init__(display)
        self.index = 5
        self.timer = 30
        pygame.mixer.music.load(os.path.join( 'assets', 'audio', "mixkit-playground-fun-12.mp3"))
        pygame.mixer.music.play(-1, fade_ms=AbstractLevel.TRANSITION_DELAY*1000)

        self.kill_count_win_bound = 30

        self.background = pygame.transform.scale(self.load_img('12_background.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        self.trees = pygame.transform.scale(self.load_img('02_trees_and_bushes.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        self.ground = pygame.transform.scale(self.load_img('03_ground.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
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

        self.explode_button = Button(self.display, pygame.transform.scale(self.load_img('b_3.png', add_sub_dir=['ui_gold']), (int(803/5), int(305/6))), (85, self.display.get_height()/2), text="Explode Moles", font=self.font_small)
        self.slow_down_button = Button(self.display, pygame.transform.scale(self.load_img('b_3.png', add_sub_dir=['ui_gold']), (int(803/5), int(305/6))), (85, self.display.get_height()/2 + 50), text="Slow Down", font=self.font_small)
        self.trap_door_button = Button(self.display, pygame.transform.scale(self.load_img('b_3.png', add_sub_dir=['ui_gold']), (int(803/5), int(305/6))), (85, self.display.get_height()/2+100), text="Trap Door", font=self.font_small)
        self.burrow_cover_button = Button(self.display, pygame.transform.scale(self.load_img('b_3.png', add_sub_dir=['ui_gold']), (int(803/5), int(305/6))), (85, self.display.get_height()/2 + 150), text="Burrow Cover", font=self.font_small)
        
        self.mole_entities.append(Mole(self.mole_entities, pos=self.mole_hole_locs[rand(9)]))
        self.mole_entities.append(Mole(self.mole_entities, pos=self.mole_hole_locs[rand(9)]))

        #self.burrow_cover_list.append(Burrow(self.burrow_cover_list, 0, lifespan=4))

        #self.trap_door_list.append(TrapDoor(self.trap_door_list, 1, lifespan=10))

    def update(self, game, dt):
        cur_pos = pygame.mouse.get_pos()
        self.cursor_img_rect = (cur_pos[0] - 13, cur_pos[1] - 51)

        self.explode_button.update(game, dt)
        self.slow_down_button.update(game, dt)
        self.trap_door_button.update(game, dt)
        self.burrow_cover_button.update(game, dt)

        self.money_text = self.font_small.render('{}'.format(game.coins), True, (255, 255, 255))

        for mole in self.mole_entities:
            mole.update(game, dt)

        for burrow_cover in self.burrow_cover_list:
            burrow_cover.update(game, dt)

        for trap_door in self.trap_door_list:
            trap_door.update(game, dt)
        
        self.timer_text = self.font.render(str(math.ceil(self.timer)), True, (255, 255, 255))
        self.timer_text_pos.x = (self.display.get_width() - self.timer_text.get_width()) / 2

        self.kill_count_text = self.font_small.render("{}/{}".format(self.kill_count, self.kill_count_win_bound), True, (255, 255, 255))

        if self.timer is not 0:
            self.timer -= dt
        else:
            self.timer_to_leave += dt
            

        if self.timer_to_leave > 2:
            self.reset()
            game.set_state(_GameState.LEVEL_SELECT)

        if (self.timer < 0):
            self.timer = 0
            pygame.mixer.music.pause()
            if self.kill_count >= self.kill_count_win_bound:
                self.win_sound.play()
                game.coins += 10
                game.level_select.unlocked_level[self.index] = True
            else:
                self.lose_sound.play()
        elif rand(15) == 0 and self.timer is not 0:
            loc = rand(0, 9)

            if not any(cover_door.hole_num == loc for cover_door in self.burrow_cover_list):
                #self.mole_entities.append(Mole(self.mole_entities, pos=self.mole_hole_locs[loc]))
                
                # There's not any trapdoor
                if not any(trap_door.hole_num == loc for trap_door in self.trap_door_list):
                    # Add the mole
                    self.mole_entities.append(Mole(self.mole_entities, pos=self.mole_hole_locs[loc]))
                # There is a trap door at loc
                else:
                    print("trap door caught mole!")
                    mole = Mole(self.mole_entities, pos=self.mole_hole_locs[loc])
                    self.mole_entities.append(mole)
                    mole.die()
                    self.kill_count += 1



    def draw(self):
        self.display.blit(self.background, self.background.get_rect())
        self.display.blit(self.huge_clouds, self.huge_clouds.get_rect())
        self.display.blit(self.trees, self.trees.get_rect())
        self.display.blit(self.ground, self.ground.get_rect())
        self.display.blit(self.clouds, self.clouds.get_rect())

        self.draw_mole_holes()

        self.explode_button.draw()
        self.slow_down_button.draw()
        self.trap_door_button.draw()
        self.burrow_cover_button.draw()


        for burrow_cover in [(m.sprite, m.hole_num) for m in self.burrow_cover_list]:
            x, y = self.mole_hole_locs[burrow_cover[1]]
            self.display.blit(burrow_cover[0], (x-burrow_cover[0].get_width()/2, y-burrow_cover[0].get_height()/2))

        for trap_door in [(t.sprite, t.hole_num) for t in self.trap_door_list]:
            x, y = self.mole_hole_locs[trap_door[1]]
            self.display.blit(trap_door[0], (x-trap_door[0].get_width()/2, y-trap_door[0].get_height()/2))

        for mole in [(m.sprite, m.position) for m in self.mole_entities]:
            self.display.blit(mole[0], mole[1])

        self.display.blit(self.money_icon, self.money_icon_pos)
        self.display.blit(self.money_text, (self.money_icon_pos[0] + 50, self.money_icon_pos[1] + 10))
           
        self.display.blit(self.timer_text, self.timer_text_pos)
        self.display.blit(self.kill_count_text, self.kill_count_text_pos)
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

            if (self.explode_button.contains(pos)) and game.coins >= 5:
                self.explode()
                game.coins -= 5
            elif (self.slow_down_button.contains(pos)) and game.coins >= 2:
                if len(self.mole_entities) > 0:
                    self.slow_down_moles(self.mole_entities[0].lifespan*2.0)
                game.coins -= 2
            elif self.burrow_cover_button.contains(pos) and game.coins >= 2:
                
                options = list(set(range(9)) - set([cover_door.hole_num for cover_door in self.burrow_cover_list] + [trap_door.hole_num for trap_door in self.trap_door_list]))
                if len(options) == 0:
                    return
                game.coins -= 2
                loc = rand(0, len(options))
                self.burrow_cover_list.append(Burrow(self.burrow_cover_list, options[loc], lifespan=10))
            
            elif self.trap_door_button.contains(pos) and game.coins >= 3:
                options = list(set(range(9)) - set([cover_door.hole_num for cover_door in self.burrow_cover_list] + [trap_door.hole_num for trap_door in self.trap_door_list]))
                if len(options) == 0:
                    return
                game.coins -= 3
                loc = rand(0, len(options))
                self.trap_door_list.append(TrapDoor(self.trap_door_list, options[loc], lifespan=10))


