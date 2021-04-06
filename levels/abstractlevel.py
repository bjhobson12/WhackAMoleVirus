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
        self.hit_sound.set_volume(0.5)
        self.win_sound = pygame.mixer.Sound(os.path.join('./', *AbstractLevel.RELATIVE_PATH_LIST, 'audio', 'mixkit-game-level-completed-2059.wav'))
        self.lose_sound = pygame.mixer.Sound(os.path.join('./', *AbstractLevel.RELATIVE_PATH_LIST, 'audio', 'mixkit-player-losing-or-failing-2042.wav'))
        self.cursor_img_rect = self.cursor_img.get_rect()
        self.font = self.load_font("LuckiestGuy-Regular.ttf", 100)
        self.font_small = self.load_font("LuckiestGuy-Regular.ttf", 18)
        self.dry_grass = self.load_img("dry grass.png", add_sub_dir=["flowers_and_plants"])
        self.kill_count = 0
        self.timer = 10
        self.mole_entities = []
        
        self.burrow_rad = 60

    def reset(self):
        self.kill_count = 0
        self.mole_entities = []

    def update(self, game, dt):
        pass

    def draw(self):
        self.display.fill((255, 100, 100))
        self.draw_mole_holes()

    def handle_event(self, game, event):
        pass

    def draw_mole_holes(self):
        for loc in self.mole_hole_locs:
            for i in range(0, 9):
                self.display.blit(self.dry_grass, (loc[0] + self.dry_grass.get_width()*i, loc[1] + self.dry_grass.get_height()*i))
            pygame.draw.circle(self.display, AbstractLevel.BROWN, loc, self.burrow_rad)
            

    def load_img(self, file_name, add_sub_dir=[], alpha=True):
        ret = pygame.image.load(os.path.join('./', *AbstractLevel.RELATIVE_PATH_LIST, 'img', *add_sub_dir, file_name))
        if alpha:
            return ret.convert_alpha()
        return ret

    def load_font(self, file_name, size):
        return pygame.font.Font(os.path.join('./', *AbstractLevel.RELATIVE_PATH_LIST, 'fonts', file_name), size)