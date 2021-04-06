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
TRANSPARENT = (0,0,0)

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

#load door image (for counter measure)
door_image = pygame.image.load("door.jpg")
door_mod_image = pygame.transform.scale(door_image, (40,40))

#load trap door image (for counter measure)
trap_door_image = pygame.image.load("trap_door.png")
trap_door_mod_image = pygame.transform.scale(trap_door_image, (40,40))

#antivirus image
overlay_image = pygame.image.load("AVS.png")
overlay_mod_image = pygame.transform.scale(overlay_image, (100,100))

#honeypot image
honeypot_image = pygame.image.load("honeypot.png")
honeypot_mod_image = pygame.transform.scale(honeypot_image, (100,100))

#slow down image
overlay_image = pygame.image.load("Sleep.png")
sleep_mod_image = pygame.transform.scale(overlay_image, (100,100))

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

#Jon's push for Moles
# def Moles(moleCurrentPosition,doorCurrentPosition, sleepTime):
#     #display the mole
#     display.blit(mole_mod_image, moleCurrentPosition)
#     time.sleep(sleepTime)

def Distance(a, b):
    x1, y1 = a
    x2, y2 = b
    x2s = (x2 - x1) * (x2 - x1)
    y2s = (y2 - y1) * (y2 - y1)
    l = math.sqrt(x2s + y2s)
    return l

#create buttons
trapdoorButton = button(OFF_WHITE,50,65,100,50,"TrapDoor")

#gets rid of moles for five seconds
def GetRidOfMolesForFiveSeconds(playerCurrentPosition, doorCurrentPosition):
    #re-creates the white burrows
    circles = int(-1)
    while circles != len(burrowPosList) - 1:
        circles += 1
        pygame.draw.circle(display, WHITE, burrowPosList[circles], burrow_rad)
    #displays original door(s), trap door(s)
    display.blit(door_mod_image, doorCurrentPosition)
    #wait five seconds before progressing
    time.sleep(5)

#covers the door so that the mole will not show
def DoorCoveringHole(playerCurrentPosition, doorCurrentPosition, moleCurrentPosition):
    #checks if moleis in position of door
    if (moleCurrentPosition == doorCurrentPosition):
        #display a message saying that the door blocked the mole
        display.blit(overlay_mod_image, (0,0))

#creates a honeypot for the mole
def TrapMolesIntoAHole(moleCurrentPosition, trapdoorCurrentPosition):
    if (moleCurrentPosition == trapdoorCurrentPosition):
        #display a message saying that the trap door caught the mole
        display.blit(honeypot_mod_image, (0,200))

#slows down the mole; time is actually set in Moles()
def SlowDownMoles(moleCurrentPosition, slowCurrentPosition):
    pass
        
#whack the mole; implemented in Rocky's push. Need to merge.
def WhackTheMole(moleCurrentPosition, doorCurrentPosition):
    #whack
    pass

#run game until exits
run = True

#if firewall countermeasure is active
slowdown=True

#if DDOS countermeasure is active
fiveSeconds = True

while run:

    #time
    
    pygame.display.flip()
    passed_time = pygame.time.get_ticks()
    #print(passed_time)
    #show_time(passed_time,400,10)

    display.fill(GREEN)
    Burrows()
    mole_pos = Moles()
    modified_mole_pos = list(mole_pos)
    modified_mole_pos[0] = mole_pos[0] + 7
    modified_mole_pos[1] = mole_pos[1] + 9
    mole_pos = tuple(modified_mole_pos)

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
            
            # #firewall countermeasure; set by boolean, slows down moles indicated by value passed in Moles
            # if slowdown:
            #     #display moles
            #     Moles(moleCurrentPosition, doorCurrentPosition,4)
            #     #displays image saying that moles are being slowed
            #     display.blit(sleep_mod_image, (0,100))
            # else:
            #     Moles(moleCurrentPosition, doorCurrentPosition,1)
            #         #pos = pygame.mouse.get_pos()
            if trapdoorButton.inRange(pos):
                print("clicked button")
                button_selected= True
                burrows_selected = False
                if not burrows_selected:
                    for i in range(len(burrowPosList) - 1):
                        if pos[0] > burrowPosList[i][0] and pos[0] < burrowPosList[i][0] + burrow_rad:
                            if pos[1] > burrowPosList[i][1] and pos[1] < burrowPosList[i][1] + burrow_rad:
                                print("burrow: ")
                                print(i)
                                burrows_selected = True



            #DDOS countermeasure; set by a boolean, gets rid of moles for 5 seconds
            #if fiveSeconds:
            #    GetRidOfMolesForFiveSeconds(playerCurrentPosition, doorCurrentPosition)
            #fiveSeconds= False


            #anti-virus countermeasure; displays image if mole in same position as door
            #DoorCoveringHole(playerCurrentPosition, doorCurrentPosition, moleCurrentPosition)


            #honeypot countermeasure; displays image if mole in same position as door
            #TrapMolesIntoAHole(playerCurrentPosition, trapdoorCurrentPosition)

            if(not button_selected):
                print('mouse')
                # Loop through every burrow point, checking the distance
                for i, burrow_point in enumerate(burrowPosList):
                    #print('in loop')
                    if Distance(pos, burrow_point) < burrow_rad:
                        # Burrow was clicked
                        print('caught')
                        display.blit(whackedMole_mod_image, mole_pos)
                        time.sleep(1.5)
                        score_value += 1
    

pygame.quit() 