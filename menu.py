import pygame
from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP
from components.button import Button
import os
from gamestate import _GameState
from menustate import _MenuState
from utility import easeInBounce, easeOutBound
import math


class Menu:

    RELATIVE_PATH_LIST = ['assets']
    TRANSITION_DELAY = 1
    #https://cga-creative-game-assets.itch.io/gold-2d-mobile-ui-for-casual-game
    #https://raventale.itch.io/parallax-background?download

    def __init__(self, display):
        self.display = display
        self.state = None
        self.font = self.load_font("LuckiestGuy-Regular.ttf", 100)
        self.font_small = self.load_font("LuckiestGuy-Regular.ttf", 18)

        self.cursor_img = self.load_img("hammer.png")

        self.cursor_img_rect = self.cursor_img.get_rect()

        self.background = pygame.transform.scale(self.load_img('11_background.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        self.trees = pygame.transform.scale(self.load_img('02_trees_and_bushes.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        self.ground = pygame.transform.scale(self.load_img('01_ground.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        self.clouds = pygame.transform.scale(self.load_img('10_distant_clouds.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 
        self.clouds_pos = self.clouds.get_rect()
        self.huge_clouds = pygame.transform.scale(self.load_img('07_huge_clouds.png', add_sub_dir=['background_pack']), (self.display.get_width(), self.display.get_height())) 

        
        
        self.title_text = self.font.render('Whack A Mole', True, (110, 60, 19))
        self.title_text_pos = self.title_text.get_rect()
        self.title_text_pos.x = int((self.display.get_width() - self.title_text.get_width()) / 2.0)
        self.title_text_pos.y = int(self.display.get_height()*0.15)

        

        self.menu_level_button = pygame.transform.scale(self.load_img('b_3.png', add_sub_dir=['ui_gold']), (int(803/5), int(305/6))) 

        self.menu_level_select_button_text = self.font_small.render('Level Select', True, (255, 255, 255))
        self.menu_level_settings_button_text = self.font_small.render('Settings', True, (255, 255, 255))

        self.button_select = Button(self.display, self.menu_level_button, self.get_screen_center(offset_y=100), self.font_small, "Level Select")
        self.button_settings = Button(self.display, self.menu_level_button, self.get_screen_center(offset_y=160), self.font_small, "Settings")

        self.set_state(_MenuState.TRANSITION_IN)
        

    def update(self, game, dt):
        cur_pos = pygame.mouse.get_pos()
        self.cursor_img_rect = (cur_pos[0] - 13, cur_pos[1] - 51)
        self.clouds_pos = self.clouds_pos.move(-2,0)
        if self.clouds_pos.width+self.clouds_pos.x <= 0:
            self.clouds_pos.x = self.display.get_width()*1.2
        
        if self.state == _MenuState.TRANSITION_IN:
            self.counter += dt
            
            #https://stackoverflow.com/questions/13462001/ease-in-and-ease-out-animation-formula
            x = min(self.counter/Menu.TRANSITION_DELAY, 1)
            self.menu_level_button.set_alpha(x*255)
            self.button_select.text.set_alpha((x)*255)
            self.button_settings.text.set_alpha((x)*255)
            #y = int((x**2/(2*(x**2-x) + 1))*(self.display.get_width() - self.button_select.button_rect.width)/2)
            #https://easings.net/#easeOutElastic
            y = easeInBounce(x)*(self.display.get_width() - self.button_select.button_rect.width)/2

            self.title_text_pos.y = easeInBounce(x)*int(self.display.get_height()*0.15)
            
            self.button_select.button_rect.x = y
            self.button_settings.button_rect.x = self.display.get_width() -  self.button_settings.button_rect.width - y

            if x == 1:
                self.set_state(_MenuState.STATIC)
        elif self.state == _MenuState.STATIC:
            pass

        elif self.state == _MenuState.TRANSITION_OUT:
            self.counter += dt
            #https://stackoverflow.com/questions/13462001/ease-in-and-ease-out-animation-formula
            x = min(self.counter/Menu.TRANSITION_DELAY, 1)
            self.menu_level_button.set_alpha((1-x)*255)
            self.button_select.text.set_alpha((1-x)*255)
            self.button_settings.text.set_alpha((1-x)*255)
            #y = int((x**2/(2*(x**2-x) + 1))*(self.display.get_width() - self.button_select.button_rect.width)/2)
            #https://easings.net/#easeOutElastic
            y = easeOutBound(x)*(self.display.get_width() - self.button_select.button_rect.width)/2
            
            self.title_text_pos.y = easeOutBound(x)*int(self.display.get_height()*0.15)
            
            self.button_select.button_rect.x = y
            self.button_settings.button_rect.x = self.display.get_width() -  self.button_settings.button_rect.width - y

            if x == 1:
                game.set_state(self.next_game_state)
                self.set_state(_MenuState.TRANSITION_IN)



        

    def handle_event(self, game, event):
        if event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if self.state == _MenuState.STATIC:
                if self.button_select.contains(pos):
                    self.next_game_state = _GameState.LEVEL_SELECT
                    self.set_state(_MenuState.TRANSITION_OUT)
                elif self.button_settings.contains(pos):
                    self.next_game_state = _GameState.SETTINGS
                    self.set_state(_MenuState.TRANSITION_OUT)

    def draw(self):
            
        self.display.blit(self.background, self.background.get_rect())
        self.display.blit(self.huge_clouds, self.huge_clouds.get_rect())
        self.display.blit(self.trees, self.trees.get_rect())
        self.display.blit(self.ground, self.ground.get_rect())
        self.display.blit(self.clouds, self.clouds_pos)
        self.display.blit(self.title_text, self.title_text_pos)
        
        self.button_select.draw()
        self.button_settings.draw()
        
        # Nothing comes after this
        self.display.blit(pygame.transform.flip(self.cursor_img, True, False), self.cursor_img_rect)


    def set_state(self, state):
        if state == self.state:
            return
        # Do stuff
        if state == _MenuState.TRANSITION_IN:
            pygame.mixer.music.load(os.path.join( './assets', 'audio', "mixkit-games-worldbeat-466.mp3"))
            pygame.mixer.music.play(-1, fade_ms=Menu.TRANSITION_DELAY*1000)
            self.counter = 0
        elif state == _MenuState.STATIC:
            pass
        elif state == _MenuState.TRANSITION_OUT:
            pygame.mixer.music.fadeout(Menu.TRANSITION_DELAY*1000)
            self.counter = 0

        self.state = state



    # Utility

    def get_screen_center(self, offset_x=0, offset_y=0):
        return (self.display.get_width()/2 + offset_x, self.display.get_height()/2 + offset_y)

    def load_font(self, file_name, size):
        return pygame.font.Font(os.path.join('./', *Menu.RELATIVE_PATH_LIST, 'fonts', file_name), size)

    def horizontal_center(self, obj, offset=0):
        return (self.display.get_width() - obj.get_width()) / 2 + offset
    
    def vertical_center(self, obj, offset=0):
        return (self.display.get_height() - obj.get_height()) / 2 + offset

    def load_img(self, file_name, add_sub_dir=[], alpha=True):
        print(os.path.join('./', *Menu.RELATIVE_PATH_LIST, 'img', *add_sub_dir, file_name))
        ret = pygame.image.load(os.path.join('./', *Menu.RELATIVE_PATH_LIST, 'img', *add_sub_dir, file_name))
        if alpha:
            return ret.convert_alpha()
        return ret