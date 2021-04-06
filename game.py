import pygame
import time
from pygame.locals import MOUSEBUTTONDOWN
import pygame.freetype
from pygame import gfxdraw
from math import sqrt
import random
import logging,sys

#colors
WHITE = (255,255,255)
BLUE = (0,0,255)
BLACK = (0,0,0)

pygame.init()

#for setting up slow down
sleepTime=2

#set up display
display = pygame.display.set_mode((640,480))
pygame.display.set_caption("Whack-A-Mole")

#setting constants
scrWidth, scrHeight = display.get_size()

burrow_rad = scrWidth // 16

clock = pygame.time.Clock()

#load door image (for counter measure)
door_image = pygame.image.load("door.jpg")
door_mod_image = pygame.transform.scale(door_image, (40,40))

#load trap door image (for counter measure)
trap_door_image = pygame.image.load("trap_door.png")
trap_door_mod_image = pygame.transform.scale(trap_door_image, (40,40))

#load mole image
mole_image = pygame.image.load("mole.png")
mole_mod_image = pygame.transform.scale(mole_image, (40,40))

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
burrow_y = 75
count = int(0)
burrowPosList = []
molePosList = []
while count != 3:
    count+=1
    burrow_x += 213.3
    if burrow_x >= scrWidth:
        burrow_x -= scrWidth
        burrow_y += 100
    tuple1 = (burrow_x, burrow_y)
    tuple2 = (burrow_x - 20, burrow_y -20)
    burrowPosList.append(tuple1)
    molePosList.append(tuple2)


#create burrows for moles
def Burrows():
    circles = int(-1)
    while circles != len(burrowPosList) - 1:
        circles += 1
        pygame.draw.circle(display, WHITE, burrowPosList[circles], burrow_rad)

#create moles
def Moles(moleCurrentPosition,doorCurrentPosition, sleepTime):
    #display the mole
    display.blit(mole_mod_image, moleCurrentPosition)
    time.sleep(sleepTime)

def Distance(a, b):
    x1, y1 = a
    x2, y2 = b
    x2s = (x2 - x1) * (x2 - x1)
    y2s = (y2 - y1) * (y2 - y1)
    l = math.sqrt(x2s + y2s)
    return l

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
    #whack the mole
    pass

doorCurrentPosition = random.choice(molePosList)

#run game until exits
run = True

#if firewall countermeasure is active
slowdown=True

#if DDOS countermeasure is active
fiveSeconds = True

while run:
    #black background
    display.fill(BLACK)

    #display burrows
    Burrows()

    #display the door
    display.blit(door_mod_image, doorCurrentPosition)

    #display trap door
    display.blit(door_mod_image, doorCurrentPosition)


    #display the trap door
    #display.blit(door_mod_image, doorCurrentPosition)

    moleCurrentPosition = random.choice(molePosList)

    #slowCurrentPosition = random.choice(molePosList)
    playerCurrentPosition = doorCurrentPosition

    #firewall countermeasure; set by boolean, slows down moles indicated by value passed in Moles
    if slowdown:
        #display moles
        Moles(moleCurrentPosition, doorCurrentPosition,4)
        #displays image saying that moles are being slowed
        display.blit(sleep_mod_image, (0,100))
    else:
        Moles(moleCurrentPosition, doorCurrentPosition,1)
    

    #DDOS countermeasure; set by a boolean, gets rid of moles for 5 seconds
    #if fiveSeconds:
    #    GetRidOfMolesForFiveSeconds(playerCurrentPosition, doorCurrentPosition)
    #fiveSeconds= False


    #anti-virus countermeasure; displays image if mole in same position as door
    DoorCoveringHole(playerCurrentPosition, doorCurrentPosition, moleCurrentPosition)


    #honeypot countermeasure; displays image if mole in same position as door
    #TrapMolesIntoAHole(playerCurrentPosition, trapdoorCurrentPosition)

    #clock
    clock.tick(60)
   
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # elif event.type == MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()
        #     print('mouse')
        #     # Loop through every burrow point, checking the distance
        #     for i, burrow_point in enumerate(burrowPosList):
        #         print('in loop')
        #         if Distance(pos, burrow_point) < burrow_rad:
        #             # Burrow was clicked
        #             print('caught')
        #             pygame.draw.circle(display, BLUE, burrowPosList[i], burrow_rad)

pygame.quit()
