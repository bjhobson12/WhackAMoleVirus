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

pygame.init()

#set up display
display = pygame.display.set_mode((640,480))
pygame.display.set_caption("Whack-A-Mole")

#setting constants
scrWidth, scrHeight = display.get_size()

burrow_rad = scrWidth // 16

clock = pygame.time.Clock()

#load mole image
mole_image = pygame.image.load("mole.png")
mole_mod_image = pygame.transform.scale(mole_image, (40,40))

#burrow and mole pos
burrow_x = -100
burrow_y = 75
count = int(0)
burrowPosList = []
molePosList = []
while count != 12:
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
def Moles():
    display.blit(mole_mod_image, random.choice(molePosList))
    time.sleep(2)

def Distance(a, b):
    x1, y1 = a
    x2, y2 = b
    x2s = (x2 - x1) * (x2 - x1)
    y2s = (y2 - y1) * (y2 - y1)
    l = math.sqrt(x2s + y2s)
    return l

#run game until exits
run = True
while run:
    
    display.fill(BLACK)
    Burrows()
    Moles()
    clock.tick(60)
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print('mouse')
            # Loop through every burrow point, checking the distance
            for i, burrow_point in enumerate(burrowPosList):
                print('in loop')
                if Distance(pos, burrow_point) < burrow_rad:
                    # Burrow was clicked
                    print('caught')
                    pygame.draw.circle(display, BLUE, burrowPosList[i], burrow_rad)

pygame.quit()
