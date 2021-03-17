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

    print("Exited python script")
    sys.exit() 
    import pygame
    pygame.init()
    dis=pygame.display.set_mode((640,480))

    pygame.display.update()
    pygame.display.set_caption('Polymorphic Virus Gamification')

    blue = (0,0,255)

    x = 300
    y = 300

    xchange = 0
    ychange = 0

    game_over=False
    while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xchange = -20
                    ychange = 0
                elif event.key == pygame.K_RIGHT:
                    xchange = 20
                    ychange = 0
                elif event.key == pygame.K_UP:
                    xchange = 0
                    ychange = -20
                elif event.key == pygame.K_DOWN:
                    xchange = 0
                    ychange = 20
        x += xchange
        y += ychange
        pygame.draw.rect(dis,blue,[310,230,10,10])
        pygame.display.update()
    pygame.quit()
    quit()
