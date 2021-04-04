import pygame
import time
from pygame.locals import MOUSEBUTTONDOWN
import pygame.freetype
import math
import random
import logging,sys

#colors
WHITE = (255,255,255)
BLUE = (0,0,255)
BLACK = (0,0,0)
GREEN = (0,100,0)
OFF_WHITE = (245,242,208)
GREY = (266,220,205)
BROWN = (195,155,119)

pygame.init()

#set up display
display = pygame.display.set_mode((640,480))
pygame.display.set_caption("Whack-A-Mole")

#setting constants
scrWidth, scrHeight = display.get_size()

burrow_rad = scrWidth // 16

#timer vars
clock = pygame.time.Clock()


#score vars
score_value = 0
font = pygame.font.Font('score_font.ttf',28)
textX = 10
textY = 10

#load mole images
mole_image = pygame.image.load("mole.png")
mole_mod_image = pygame.transform.scale(mole_image, (90,97))

whackedMole_image = pygame.image.load("whackedMole.png")
whackedMole_mod_image = pygame.transform.scale(whackedMole_image, (75,84))

#burrow and mole pos
burrow_x = -100
burrow_y = 175
count = int(0)
burrowPosList = []
molePosList = []
while count != 9:
    count+=1
    burrow_x += 213.3
    if burrow_x >= scrWidth:
        burrow_x -= scrWidth
        burrow_y += 100
    tuple1 = (burrow_x, burrow_y)
    tuple2 = (burrow_x -42 , burrow_y -55)
    burrowPosList.append(tuple1)
    molePosList.append(tuple2)

#button class
class button():
    def __init__(self, color, x,y, w,h, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text

    def draw(self, win, outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.w+4,self.h+4),0)
        pygame.draw.rect(win, self.color, (self.x,self.y,self.w,self.h),0)
        
        if self.text != '':
            font = pygame.font.Font('bounce.otf',18)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.w/2 - text.get_width()/2), self.y + (self.h/2 - text.get_height()/2)))

    def inRange(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.w:
            if pos[1] > self.y and pos[1] < self.y + self.h:
                return True
            
        return False



#displaying score
def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, WHITE)
    display.blit(score, (x,y))

#displaying score
def show_time(t,x,y):
    time = font.render("Time: " + str(t/1000), True, WHITE)
    display.blit(time, (x, y))

#create burrows for moles
def Burrows():
    circles = int(-1)
    while circles != len(burrowPosList) - 1:
        circles += 1
        pygame.draw.circle(display, BROWN, burrowPosList[circles], burrow_rad)

#create moles
def Moles():
    pos = random.choice(molePosList)
    display.blit(mole_mod_image, pos)
    time.sleep(2)
    return pos

def Distance(a, b):
    x1, y1 = a
    x2, y2 = b
    x2s = (x2 - x1) * (x2 - x1)
    y2s = (y2 - y1) * (y2 - y1)
    l = math.sqrt(x2s + y2s)
    return l

#create buttons
trapdoorButton = button(OFF_WHITE,50,65,100,50,"TrapDoor")


#run game until exits
run = True
while run:
    
    #time
    
    pygame.display.flip()
    passed_time = pygame.time.get_ticks()
    print(passed_time)
    show_time(passed_time,400,10)
 
    

    display.fill(GREEN)
    Burrows()
    mole_pos = Moles()
    clock.tick(60)
    show_score(textX,textY)
    #draw button
    trapdoorButton.draw(display, BLACK)
    #button clicked tracker
    button_selected = False

    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
        
        elif event.type == MOUSEBUTTONDOWN:
            
            #pos = pygame.mouse.get_pos()
            if trapdoorButton.inRange(pos):
                print("clicked button")
                button_selected = True

                
            if(not button_selected):
                print('mouse')
                # Loop through every burrow point, checking the distance
                for i, burrow_point in enumerate(burrowPosList):
                    #print('in loop')
                    if Distance(pos, burrow_point) < burrow_rad:
                        # Burrow was clicked
                        print('caught')
                        display.blit(whackedMole_mod_image, mole_pos)
                        time.sleep(1)
                        score_value += 1
    

pygame.quit() 
