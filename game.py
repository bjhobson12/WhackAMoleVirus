import pygame

WHITE = (255,255,255)
BLACK = (0,0,0)

class Mole:

    def __init__(self, display):
        self.display = display
        self.image = pygame.image.load("mole.gif").convert_alpha()
        self.rect - self.image.get_rect()

    #if hit, move mole
    def flee(self):
        x = random.randint(0, scrWidth-1-self.rect.width)
        y = random.randint(0, scrHeight-1-self.rect.height)
        self.rect.topleft = (x,y)

    def draw(self, screen):
        self.display.blit(self.image, self.rect)

class Hammer:

    def __init__(self, display):
        self.display = display
        self.image = pygame.image.load("hammer.gif").convert_alpha()
        self.rect = self.image.get_rect()

    # check if shovel hit mole
    def hit(self, target):
        return self.rect.colliderect(target)

    # follows the mouse cursor
    def update(self, pt):
        self.rect.center = pt

    def draw(self, screen):
        self.display.blit(self.image, self.rect)

class WhackAMole:

    def __init__(self):
        pygame.init()
        self.dis=pygame.display.set_mode((640,480))
        self.dis.fill(WHITE)
        pygame.display.update()
        pygame.display.set_caption('Whack-a-Mole Game')

    def draw(self):

        #Set height and width
        scrWidth, scrHeight = self.dis.get_size()

        #create sprites
        mole = Mole(self.dis)
        shovel = Shovel(self.dis)

        game_over=False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == MOUSEMOTION:
                    mousePos = pygame.mouse.get_pos()
                if event.type == MOUSEBUTTONDOWN:
                    isPressed = True
                  
            pygame.display.update()



        pygame.quit()
        quit()
