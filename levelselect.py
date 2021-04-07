import pygame
from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP
from components.button import Button
import os
from gamestate import _GameState
from menustate import _MenuState
from levelselectstate import _LevelSelectState
from utility import easeInBounce, easeOutBound
import math
from levels.level_1 import LevelOne
from levels.level_2 import LevelTwo
from levels.level_3 import LevelThree
from levels.level_4 import LevelFour
from levels.level_5 import LevelFive
from levels.level_6 import LevelSix
from levels.level_7 import LevelSeven
from levels.level_8 import LevelEight
from levels.level_9 import LevelNine


class LevelSelect:

    TRANSITION_DELAY = 1
    RELATIVE_PATH_LIST = ['assets']

    def __init__(self, display):
        self.display = display
        self.state = None
        self.prev_state = None
        self.counter = 0
        self.font = self.load_font("LuckiestGuy-Regular.ttf", 100)
        self.font_small = self.load_font("LuckiestGuy-Regular.ttf", 18)
        self.select_sound = pygame.mixer.Sound(os.path.join('./', *LevelSelect.RELATIVE_PATH_LIST, 'audio', 'mixkit-winning-a-coin-video-game-2069.wav'))
        self.select_sound.set_volume(0.05)
        self.locked_sound = pygame.mixer.Sound(os.path.join('./', *LevelSelect.RELATIVE_PATH_LIST, 'audio', 'mixkit-quick-lock-sound-2854.wav'))
        self.locked_sound.set_volume(0.05)
        self.unlock_sound = pygame.mixer.Sound(os.path.join('./', *LevelSelect.RELATIVE_PATH_LIST, 'audio', 'mixkit-unlock-new-item-game-notification-254.wav'))
        self.unlock_sound.set_volume(0.05)


        self.cursor_img = self.load_img("hammer.png")

        self.cursor_img_rect = self.cursor_img.get_rect()

        self.money_icon = pygame.transform.scale(self.load_img('c.png', add_sub_dir=['ui_gold']), (30,30))
        self.money_icon_pos = self.money_icon.get_rect()
        self.money_icon_pos.x = self.display.get_width()*0.90
        self.money_icon_pos.y = 10
        self.money_text = self.font_small.render('{}'.format(0), True, (255, 255, 255))
        self.forward_button = Button(self.display, pygame.transform.scale(self.load_img('b_7.png', add_sub_dir=['ui_gold']), (50,50)), ((self.display.get_width() + 50)/2+25, self.display.get_height()*0.85))
        self.backward_button = Button(self.display, pygame.transform.scale(self.load_img('b_6.png', add_sub_dir=['ui_gold']), (50,50)), ((self.display.get_width() + 50)/2-75, self.display.get_height()*0.85))

        self.backward_button.disabled = True

        """self.forward_button = pygame.transform.scale(self.load_img('b_7.png', add_sub_dir=['ui_gold']), (50,50))
        self.forward_button_pos = self.forward_button.get_rect()
        self.forward_button_pos.x, self.forward_button_pos.y = (self.display.get_width() + 50)/2, self.display.get_height()*0.85
        self.backward_button = pygame.transform.scale(self.load_img('b_6.png', add_sub_dir=['ui_gold']), (50, 50))
        self.backward_button_pos = self.backward_button.get_rect()
        self.backward_button_pos.x, self.backward_button_pos.y = (self.display.get_width() + 50)/2-100, self.display.get_height()*0.85"""

        self.background = pygame.transform.scale(self.load_img('11_background.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        self.background_rock = pygame.transform.scale(self.load_img('12_background.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        self.background_ice = pygame.transform.scale(self.load_img('13_background.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        #self.trees = pygame.transform.scale(self.load_img('02_trees_and_bushes.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        self.ground = pygame.transform.scale(self.load_img('01_ground.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        self.ground_two = pygame.transform.scale(self.load_img('03_ground.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        self.ground_ice = pygame.transform.scale(self.load_img('02_ground.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        self.clouds = pygame.transform.scale(self.load_img('10_distant_clouds.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        self.clouds_pos = self.clouds.get_rect()
        self.cloud_speed = 1
        self.huge_clouds = pygame.transform.scale(self.load_img('07_huge_clouds.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        
        self.small_shroom = self.load_img('mushroom06.png', add_sub_dir=['flowers_and_plants'])
        self.shroom = self.load_img('mushroom01.png', add_sub_dir=['flowers_and_plants'])
        self.red_shroom = self.load_img('mushroom02.png', add_sub_dir=['flowers_and_plants'])

        self.small_stone = self.load_img('stone03.png', add_sub_dir=['nature', '_rocks'])
        self.stone = self.load_img('stone02.png', add_sub_dir=['nature', '_rocks'])
        self.large_stone = self.load_img('stone06.png', add_sub_dir=['nature', '_rocks'])

        self.small_ice = self.load_img('ice_2.png', add_sub_dir=['nature', '_ice'])
        self.ice = self.load_img('ice_4.png', add_sub_dir=['nature', '_ice'])
        self.large_ice = self.load_img('ice_6.png', add_sub_dir=['nature', '_ice'])

        self.level_spacing = self.display.get_width()/5

        self.background_pos = self.background.get_rect()
        self.background_rock_pos = self.background_rock.get_rect()
        self.background_rock_pos.x = self.display.get_width()
        self.background_ice_pos = self.background_rock.get_rect()
        self.background_ice_pos.x = self.display.get_width()*2
        self.huge_clouds_pos = self.huge_clouds.get_rect()

        self.ground_pos = self.ground.get_rect()
        self.ground_two_pos = self.ground_two.get_rect()
        self.ground_two_pos.x = self.display.get_width()
        self.ground_ice_pos = self.ground_ice.get_rect()
        self.ground_ice_pos.x = self.display.get_width()*2



        
        self.small_shroom_pos = self.small_shroom.get_rect() 
        self.small_shroom_pos.x, self.small_shroom_pos.y = (self.level_spacing*(1)-self.level_spacing/2 + self.small_shroom.get_width()/4, 340)

        self.shroom_pos = self.shroom.get_rect() 
        self.shroom_pos.x, self.shroom_pos.y = (self.level_spacing*(2) + self.shroom.get_width()/4, 340)

        self.red_shroom_pos = self.red_shroom.get_rect() 
        self.red_shroom_pos.x, self.red_shroom_pos.y = (self.level_spacing*(3)+self.level_spacing/2 , 340)



        self.small_stone_pos = self.small_stone.get_rect() 
        self.small_stone_pos.x, self.small_stone_pos.y = (self.level_spacing*(1)-self.level_spacing/2 + self.small_shroom.get_width()/4 + self.display.get_width(), 340)

        self.stone_pos = self.stone.get_rect() 
        self.stone_pos.x, self.stone_pos.y = (self.level_spacing*(2) + self.shroom.get_width()/4 + self.display.get_width(), 340)

        self.large_stone_pos = self.large_stone.get_rect() 
        self.large_stone_pos.x, self.large_stone_pos.y = (self.level_spacing*(3)+self.level_spacing/2 + self.display.get_width(), 340)



        self.small_ice_pos = self.small_ice.get_rect() 
        self.small_ice_pos.x, self.small_ice_pos.y = (self.level_spacing*(1)-self.level_spacing/2 + self.small_shroom.get_width()/4 + self.display.get_width()*2, 340)

        self.ice_pos = self.ice.get_rect() 
        self.ice_pos.x, self.ice_pos.y = (self.level_spacing*(2) + self.shroom.get_width()/4 + self.display.get_width()*2, 340)

        self.large_ice_pos = self.large_ice.get_rect() 
        self.large_ice_pos.x, self.large_ice_pos.y = (self.level_spacing*(3)+self.level_spacing/2 + self.display.get_width()*2, 340)



        # must add to begining not end 
        self.slidables = [
            self.background_pos, 
            self.background_rock_pos, 
            self.background_ice_pos,
            self.huge_clouds_pos, 
            self.ground_pos,
            self.ground_two_pos,
            self.ground_ice_pos,
            self.small_shroom_pos, 
            self.shroom_pos, 
            self.red_shroom_pos,
            self.small_stone_pos,
            self.stone_pos,
            self.large_stone_pos,
            self.small_ice_pos,
            self.ice_pos,
            self.large_ice_pos
        ]

        self.levels = [
            LevelOne,
            LevelTwo,
            LevelThree,
            LevelFour,
            LevelFive,
            LevelSix,
            LevelSeven,
            LevelEight,
            LevelNine
        ]

        self.hover_level = None

        self.unlocked_level = [True] + [False]*8

        self.num_unlocked_levels = 1
        
        self.current_level = self.levels[0]
        
        self.title_text = self.font.render('Select Level', True, (110, 60, 19))
        self.title_text_pos = self.title_text.get_rect()
        self.title_text_pos.x = int((self.display.get_width() - self.title_text.get_width()) / 2.0)
        self.title_text_pos.y = int(self.display.get_height()*0.15)

        self.set_state(_LevelSelectState.EARTH_WORLD)
        

    def update(self, game, dt):
        cur_pos = pygame.mouse.get_pos()
        self.cursor_img_rect = (cur_pos[0] - 13, cur_pos[1] - 51)
        self.clouds_pos = self.clouds_pos.move(-self.cloud_speed,0)
        if self.clouds_pos.width+self.clouds_pos.x <= 0:
            self.clouds_pos.x = self.display.get_width()*1.2
        
        if self.num_unlocked_levels != sum(self.unlocked_level):
            self.num_unlocked_levels = sum(self.unlocked_level)
            self.unlock_sound.play()

        self.money_text = self.font_small.render('{}'.format(game.coins), True, (255, 255, 255))

        if self.state == _LevelSelectState.TRANSITION_RIGHT or self.state == _LevelSelectState.TRANSITION_LEFT:
            self.counter += dt
            if self.counter >= LevelSelect.TRANSITION_DELAY:
                self.counter -= dt
                dt = LevelSelect.TRANSITION_DELAY - self.counter
                self.counter = LevelSelect.TRANSITION_DELAY
            
            x = dt/LevelSelect.TRANSITION_DELAY

            

            if self.counter >= 1:
                realign_offset = round(self.background_ice_pos.x / self.display.get_width()) * self.display.get_width() - self.background_ice_pos.x
                for item in self.slidables:
                    item.x = item.x + realign_offset
                
                if (self.prev_state == _LevelSelectState.EARTH_WORLD and self.state == _LevelSelectState.TRANSITION_RIGHT):
                    self.set_state(_LevelSelectState.ROCK_WORLD)
                elif self.prev_state == _LevelSelectState.ROCK_WORLD and self.state == _LevelSelectState.TRANSITION_RIGHT:
                    self.set_state(_LevelSelectState.ICE_WORLD)
                elif self.prev_state == _LevelSelectState.ICE_WORLD and self.state == _LevelSelectState.TRANSITION_LEFT:
                    self.set_state(_LevelSelectState.ROCK_WORLD)
                elif self.prev_state == _LevelSelectState.ROCK_WORLD and self.state == _LevelSelectState.TRANSITION_LEFT:
                    self.set_state(_LevelSelectState.EARTH_WORLD)
                
                return

            for item in self.slidables:
                item.x = item.x + (-1 if self.state == _LevelSelectState.TRANSITION_RIGHT else 1)*self.display.get_width()*x

        else:
            level_rects = self.slidables[-9:]
            for i in range(0, len(level_rects)):
                if level_rects[i].contains(pygame.Rect(*cur_pos, 1, 1)) and level_rects[i] == self.hover_level:
                    self.hover_level = level_rects[i]
                    self.play_counter += dt
                    break
            else:
                self.play_counter = 0

            if self.play_counter >= 3:
                self.play_counter = 0
                game.set_state(_GameState.PLAYING)

    def select_level_index(self, i):
        if self.unlocked_level[i]:
            self.current_level = self.levels[i]
            self.select_sound.play()
            self.hover_level = self.slidables[-9:][i]
        else:
            self.locked_sound.play()

    def handle_event(self, game, event):
        if event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if self.state == _LevelSelectState.TRANSITION_RIGHT or self.state == _LevelSelectState.TRANSITION_LEFT:
                return
            if self.forward_button.contains(pos):
                if self.forward_button.disabled:
                    self.locked_sound.play()
                elif self.state == _LevelSelectState.EARTH_WORLD or self.state == _LevelSelectState.ROCK_WORLD:
                    self.select_sound.play()
                    self.set_state(_LevelSelectState.TRANSITION_RIGHT)
            elif self.backward_button.contains(pos):
                if self.backward_button.disabled:
                    self.locked_sound.play()
                elif self.state == _LevelSelectState.ICE_WORLD or self.state == _LevelSelectState.ROCK_WORLD:
                    self.select_sound.play()
                    self.set_state(_LevelSelectState.TRANSITION_LEFT)
            elif self.small_shroom_pos.contains(pygame.Rect(pos[0], pos[1], 1, 1)):
                self.select_level_index(0)
            elif self.shroom_pos.contains(pygame.Rect(pos[0], pos[1], 1, 1)):
                self.select_level_index(1)
            elif self.red_shroom_pos.contains(pygame.Rect(pos[0], pos[1], 1, 1)):
               self.select_level_index(2)
            elif self.small_stone_pos.contains(pygame.Rect(pos[0], pos[1], 1, 1)):
                self.select_level_index(3)
            elif self.stone_pos.contains(pygame.Rect(pos[0], pos[1], 1, 1)):
                self.select_level_index(4)
            elif self.large_stone_pos.contains(pygame.Rect(pos[0], pos[1], 1, 1)):
                self.select_level_index(5)
            elif self.small_ice_pos.contains(pygame.Rect(pos[0], pos[1], 1, 1)):
                self.select_level_index(6)
            elif self.ice_pos.contains(pygame.Rect(pos[0], pos[1], 1, 1)):
                self.select_level_index(7)
            elif self.large_ice_pos.contains(pygame.Rect(pos[0], pos[1], 1, 1)):
                self.select_level_index(8)
            

    def draw(self):
        self.display.blit(self.background, self.background_pos)
        self.display.blit(self.background_rock, self.background_rock_pos)
        self.display.blit(self.background_ice, self.background_ice_pos)
        self.display.blit(self.huge_clouds, self.huge_clouds_pos)
        #self.display.blit(self.trees, self.trees.get_rect())
        self.display.blit(self.ground, self.ground_pos)
        self.display.blit(self.ground_two, self.ground_two_pos)
        self.display.blit(self.ground_ice, self.ground_ice_pos)
        self.display.blit(self.clouds, self.clouds_pos)
        self.display.blit(self.title_text, self.title_text_pos)
        
        self.display.blit(self.small_shroom, self.small_shroom_pos)
        self.display.blit(self.shroom, self.shroom_pos)
        self.display.blit(self.red_shroom, self.red_shroom_pos)

        self.display.blit(self.small_stone, self.small_stone_pos)
        self.display.blit(self.stone, self.stone_pos)
        self.display.blit(self.large_stone, self.large_stone_pos)

        self.display.blit(self.small_ice, self.small_ice_pos)
        self.display.blit(self.ice, self.ice_pos)
        self.display.blit(self.large_ice, self.large_ice_pos)

        self.backward_button.draw()
        self.forward_button.draw()

        self.display.blit(self.money_icon, self.money_icon_pos)
        self.display.blit(self.money_text, (self.money_icon_pos[0] + 50, self.money_icon_pos[1] + 10))

        
        # Nothing comes after this
        self.display.blit(pygame.transform.flip(self.cursor_img, True, False), self.cursor_img_rect)
        
        pygame.draw.circle(self.display, (255, 255, 255), (self.cursor_img_rect[0] + 13, self.cursor_img_rect[1] + 51), 30*max(0, (3 - self.play_counter)/3), width=2)


    def set_state(self, state):
        if state == self.state:
            return
        # Do stuff
        if state == _LevelSelectState.EARTH_WORLD:
            self.backward_button.disabled = True
            self.forward_button.disabled = False
            self.cloud_speed = 1
            if self.state is None:
                #pygame.mixer.music.stop()
                #pygame.mixer.music.load(os.path.join( './assets', 'audio', "mixkit-medieval-show-fanfare-announcement-226.wav"))
                pygame.mixer.music.play(-1, fade_ms=LevelSelect.TRANSITION_DELAY*1000)
            else:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(os.path.join( './assets', 'audio', "mixkit-games-worldbeat-466.mp3"))
                pygame.mixer.music.set_volume(0.05)
                pygame.mixer.music.play(-1, fade_ms=LevelSelect.TRANSITION_DELAY*1000)
        elif state == _LevelSelectState.ROCK_WORLD:
            self.backward_button.disabled = False
            self.forward_button.disabled = False
            self.cloud_speed = 8
            pygame.mixer.music.stop()
            pygame.mixer.music.set_volume(0.03)
            pygame.mixer.music.load(os.path.join( './assets', 'audio', "mixkit-medieval-show-fanfare-announcement-226.wav"))
            pygame.mixer.music.play(-1, fade_ms=LevelSelect.TRANSITION_DELAY*1000)
        elif state == _LevelSelectState.ICE_WORLD:
            self.forward_button.disabled = True
            self.backward_button.disabled = False
            self.cloud_speed = 0
            pygame.mixer.music.stop()
            pygame.mixer.music.load(os.path.join( './assets', 'audio', "mixkit-island-beat-250.mp3"))
            pygame.mixer.music.set_volume(0.03)
            pygame.mixer.music.play(-1, start=10.0, fade_ms=LevelSelect.TRANSITION_DELAY*1000)

        elif state == _LevelSelectState.TRANSITION_LEFT or state == _LevelSelectState.TRANSITION_RIGHT:
            pygame.mixer.music.fadeout(LevelSelect.TRANSITION_DELAY*1000)
        
        self.counter = 0
        self.prev_state = self.state
        self.state = state



    # Utility

    def get_screen_center(self, offset_x=0, offset_y=0):
        return (self.display.get_width()/2 + offset_x, self.display.get_height()/2 + offset_y)

    def load_font(self, file_name, size):
        return pygame.font.Font(os.path.join('./', *LevelSelect.RELATIVE_PATH_LIST, 'fonts', file_name), size)

    def horizontal_center(self, obj, offset=0):
        return (self.display.get_width() - obj.get_width()) / 2 + offset
    
    def vertical_center(self, obj, offset=0):
        return (self.display.get_height() - obj.get_height()) / 2 + offset

    def load_img(self, file_name, add_sub_dir=[], alpha=True):
        print(os.path.join('./', *LevelSelect.RELATIVE_PATH_LIST, 'img', *add_sub_dir, file_name))
        ret = pygame.image.load(os.path.join('./', *LevelSelect.RELATIVE_PATH_LIST, 'img', *add_sub_dir, file_name))
        if alpha:
            return ret.convert_alpha()
        return ret