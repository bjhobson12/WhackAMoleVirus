import pygame
import os

class AbstractLevel:

    RELATIVE_PATH_LIST = ["assets"]

    TRANSITION_DELAY = 3

    WHITE = (255,255,255)
    BLUE = (0,0,255)
    BLACK = (0,0,0)
    GREEN = (0,100,0)
    OFF_WHITE = (245,242,208)
    GREY = (266,220,205)
    BROWN = (195,155,119)
    TRANSPARENT = (0,0,0)

    def __init__(self, display):
        self.index = None
        self.display = display
        self.cursor_img = self.load_img("hammer.png")
        self.hit_sound = pygame.mixer.Sound(os.path.join('./', *AbstractLevel.RELATIVE_PATH_LIST, 'audio', 'mixkit-cartoon-monkey-laugh-100.wav'))
        self.hit_sound.set_volume(0.02)
        self.win_sound = pygame.mixer.Sound(os.path.join('./', *AbstractLevel.RELATIVE_PATH_LIST, 'audio', 'mixkit-game-level-completed-2059.wav'))
        self.win_sound.set_volume(0.02)
        self.lose_sound = pygame.mixer.Sound(os.path.join('./', *AbstractLevel.RELATIVE_PATH_LIST, 'audio', 'mixkit-player-losing-or-failing-2042.wav'))
        self.lose_sound.set_volume(0.02)
        self.explosion_sound = pygame.mixer.Sound(os.path.join('./', *AbstractLevel.RELATIVE_PATH_LIST, 'audio', 'mixkit-magic-sweep-game-trophy-257.wav'))
        self.explosion_sound.set_volume(0.02)

        self.money_icon = pygame.transform.scale(self.load_img('c.png', add_sub_dir=['ui_gold']), (30,30))
        self.money_icon_pos = self.money_icon.get_rect()
        self.money_icon_pos.x = self.display.get_width()*0.90
        self.money_icon_pos.y = 10
        
        self.cursor_img_rect = self.cursor_img.get_rect()
        self.font = self.load_font("LuckiestGuy-Regular.ttf", 100)
        self.font_small = self.load_font("LuckiestGuy-Regular.ttf", 18)
        self.dry_grass = self.load_img("dry grass.png", add_sub_dir=["flowers_and_plants"])
        self.kill_count = 0
        self.timer = 20
        self.timer_to_leave = 0
        self.mole_entities = []
        self.burrow_cover_list = []
        self.trap_door_list = []
        #self.explosions = []

        self.mole_hole_locs = [
            (self.display.get_width()/4*1,self.display.get_height()/4*1),
            (self.display.get_width()/4*1,self.display.get_height()/4*2),
            (self.display.get_width()/4*1,self.display.get_height()/4*3),
            (self.display.get_width()/4*2,self.display.get_height()/4*1),
            (self.display.get_width()/4*2,self.display.get_height()/4*2),
            (self.display.get_width()/4*2,self.display.get_height()/4*3),
            (self.display.get_width()/4*3,self.display.get_height()/4*1),
            (self.display.get_width()/4*3,self.display.get_height()/4*2),
            (self.display.get_width()/4*3,self.display.get_height()/4*3)
        ]
        
        self.burrow_rad = 60

    def reset(self):
        self.kill_count = 0
        self.mole_entities = []
        self.timer_to_leave = 0

    def update(self, game, dt):
        pass

    def explode(self):
        i = len(self.mole_entities) - 1
        self.explosion_sound.play()
        while i > -1:
            if not self.mole_entities[i].is_dead:
                self.mole_entities[i].die()
                self.mole_entities[i].sprite = self.load_sprite("boom.png")
                self.kill_count += 1

            i -= 1

    def slow_down_moles(self, l):
        for mole in self.mole_entities:
            mole.lifespan = l
            #mole.sprite = pygame.transform.scale2x(mole.sprite)

    def draw(self):
        self.display.fill((255, 100, 100))

    def handle_event(self, game, event):
        pass

    def draw_mole_holes(self):
        for loc in self.mole_hole_locs:
            pygame.draw.circle(self.display, AbstractLevel.BROWN, loc, self.burrow_rad)
            

    def load_img(self, file_name, add_sub_dir=[], alpha=True):
        ret = pygame.image.load(os.path.join('./', *AbstractLevel.RELATIVE_PATH_LIST, 'img', *add_sub_dir, file_name))
        if alpha:
            return ret.convert_alpha()
        return ret

    def load_sprite(self, file_name, add_sub_dir=[], alpha=True):
        ret = pygame.image.load(os.path.join('./', *AbstractLevel.RELATIVE_PATH_LIST, 'sprites', *add_sub_dir, file_name))
        if alpha:
            return ret.convert_alpha()
        return ret

    def load_font(self, file_name, size):
        return pygame.font.Font(os.path.join('./', *AbstractLevel.RELATIVE_PATH_LIST, 'fonts', file_name), size)