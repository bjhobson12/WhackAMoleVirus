# Hacking related Modules
import os, sys
from subprocess import Popen, PIPE

class PolymorphicAttack():

    def __init__(self):
        self.gcc_path = None
        



def run_weak_process(cmd, blocking=False):
    # This is a non-blocking call
    p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    # This is a blocking call to wait for the process
    output, error = p.communicate()

    if p.returncode != 0: 
        raise Exception(error.decode('utf-8').strip())
    else:
        return output.decode('utf-8').strip()


if __name__ == '__main__':

    # Check python version at runtime https://stackoverflow.com/questions/9079036/how-do-i-detect-the-python-version-at-runtime
    if sys.version_info[0] < 3:
        raise Exception("Must be using Python 3")

    PolyAttack = PolymorphicAttack()

    # python docs https://docs.python.org/3/library/sys.html#sys.platform
    try:
        
        if sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
            # Mac OS or Linux
            PolyAttack.gcc_path = run_weak_process(["which", "gcc"])
        elif sys.platform.startswith('win32'):
            # Windows (true)
            pass
        elif sys.platform.startswith('cygwin'):
            # Windows ('cygwin')
            pass
        else:
            raise Exception("The environment was not recognized")
    
    except Exception as e:
        print(e)
        print("Sorry we cannot run Whack a Mole on your OS")
        sys.exit()

    run_weak_process([PolyAttack.gcc_path, os.path.join(os.getcwd(), "main.c"), "-o", "main"])
    run_weak_process(['chmod', '+x', './main'])
    
    Popen(['./main'], shell=True)
    #Popen(['./main'], stderr=PIPE, stdout=PIPE, shell=True)
    # 
#------------ Start of Pygame code
    
    import pygame
   

class Mole(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("mole.gif").convert_alpha()
        self.rect - self.image.get_rect()

    #if hit, move mole
    def flee(self):
    x = random.randint(0, scrWidth-1-self.rect.width)
    y = random.randint(0, scrHeight-1-self.rect.height)
    self.rect.topleft = (x,y)


    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Hammer(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("hammer.gif").convert_alpha()
        self.rect = self.image.get_rect()

    # check if shovel hit mole
    def hit(self, target):
        return self.rect.colliderect(target)

    # follows the mouse cursor
    def update(self, pt):
        self.rect.center = pt

    def draw(self, screen):
        screen.blit(self.image, self.rect)

#------------Start of Main

pygame.init()
dis=pygame.display.set_mode((640,480))
screen.fill(WHITE)
pygame.display.update()
pygame.display.set_caption('Whack-a-Mole Game')

#Set height and width
scrWidth, scrHeight = screen.get_size()

#create sprites
mole = Mole()
shovel = Shovel()

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

print("Exited python script")
sys.exit() 
