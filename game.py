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
mole_pos = 0

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
AVS_image = pygame.image.load("AVS.png")
AVS_mod_image = pygame.transform.scale(AVS_image, (100,100))

#honeypot image
honeypot_image = pygame.image.load("honeypot.png")
honeypot_mod_image = pygame.transform.scale(honeypot_image, (100,100))

#slow down image
overlay_image = pygame.image.load("Sleep.png")
sleep_mod_image = pygame.transform.scale(overlay_image, (100,100))

#slow down image
ddos_image = pygame.image.load("ddos.png")
ddos_mod_image = pygame.transform.scale(ddos_image, (100,100))

#slow down image
idps_image = pygame.image.load("idps.png")
idps_mod_image = pygame.transform.scale(idps_image, (100,100))

#burrow and mole pos
burrow_x = -100
burrow_y = 175
count = int(0)
burrowPosList = []
molePosList = []
doorPositions = []
trapDoorPositions=[]
points =0



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
    while pos[0] == 0 and pos[1] == 0:
        pos = random.choice(molePosList)
    if len(doorPositions) > 0:
        for i in doorPositions:
            display.blit(door_mod_image, i)
    if len(trapDoorPositions) > 0:
        for j in trapDoorPositions:
            display.blit(trap_door_mod_image, j)
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
doorCoveringHoleButton = button(OFF_WHITE,50,65,100,50,"Burrow Cover")
TrapMolesIntoAHoleButton = button(OFF_WHITE,200,65,100,50,"Trap Door")
GetRidOfMolesForFiveSecondsButton = button(OFF_WHITE,350,65,100,50,"Five Seconds")
SlowDownMolesButton = button(OFF_WHITE,500,65,100,50,"Slow Down")

#gets rid of moles for five seconds
def GetRidOfMolesForFiveSeconds():
    #re-creates the white burrows
    circles = int(-1)
    
    while circles != len(burrowPosList) - 1:
        circles += 1
        pygame.draw.circle(display, WHITE, burrowPosList[circles], burrow_rad)

    #time.sleep(5)
    


    #displays original door(s), trap door(s)
    #display.blit(door_mod_image, 0,0)
    #wait five seconds before progressing


#covers the door so that the mole will not show
def DoorCoveringHole(doorPosition):
    #blocks our hole
    #print(molePosList[doorPosition])
    display.blit(AVS_mod_image, (0,100))
    doorPositions.append(molePosList[doorPosition])
    molePosList[doorPosition] = (0,0)
    


#creates a honeypot for the mole; if mole gets trapped, immediately get points for it
def TrapMolesIntoAHole(mole_pos):
    #display.blit(honeypot_mod_image, (0,100))
    for burrow in trapDoorPositions:
        #print(burrow)
        score_value = 0
        if (abs(mole_pos[0] - burrow[0]) < 7.25):
            #display a message saying that the trap door caught the mole
            print("ew! the honeypot caught one of em moles!")
            score_value += 1
        return score_value


#slows down the mole; time is actually set in Moles()
def SlowDownMoles(moleCurrentPosition, slowCurrentPosition):
    pass
        
#whack the mole; implemented in Rocky's push. Need to merge.
def WhackTheMole(moleCurrentPosition, doorCurrentPosition):
    #whack
    pass

def PlaceDoor(burrowPosition):
    doorPositions += burrowPosition

def PlaceTrapDoor(trapDoorPosition):
    #print(molePosList[trapDoorPosition])
    trapDoorPositions.append(molePosList[trapDoorPosition])

#run game until exits
run = True

#if firewall countermeasure is active
slowdown=False

#if DDOS countermeasure is active
fiveSeconds = True


while run:
    #time
    
    pygame.display.flip()
    passed_time = pygame.time.get_ticks()

    #print(passed_time)
    #print(molePosList)
    #print(trapDoorPositions)
    #print(mole_pos)

    show_time(passed_time,400,10)

    points = TrapMolesIntoAHole(mole_pos)

    #print(points)

    #add points for honeypot
    if (points is not None):
        if points > 0:
            score_value += points


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
    doorCoveringHoleButton.draw(display, BLACK)
    TrapMolesIntoAHoleButton.draw(display, BLACK)
    GetRidOfMolesForFiveSecondsButton.draw(display, BLACK)
    SlowDownMolesButton.draw(display, BLACK)
    #button clicked tracker
    button_selected = False

    pygame.display.update()

    # #firewall countermeasure; set by boolean, slows down moles indicated by value passed in Moles
    if slowdown:
        display.blit(sleep_mod_image, (0,100))
        #display moles
        time.sleep(4)

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False


        elif event.type == MOUSEBUTTONDOWN:
            
            pos = pygame.mouse.get_pos()

            TrapMolesIntoAHole(mole_pos)
            #print("test")
            if doorCoveringHoleButton.inRange(pos):
                print("clicked button 1")
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN:
                    print("key pressed")
                    if event.key == pygame.K_1:
                        print("1")
                        DoorCoveringHole(0)
                    elif event.key == pygame.K_2:
                        print("2")
                        DoorCoveringHole(1)
                    elif event.key == pygame.K_3:
                        DoorCoveringHole(2)
                        print("3")
                    elif event.key == pygame.K_4:
                        DoorCoveringHole(3)
                        print("4")
                    elif event.key == pygame.K_5:
                        DoorCoveringHole(4)
                        print("5")
                    elif event.key == pygame.K_6:
                        DoorCoveringHole(5)
                        print("6")
                    elif event.key == pygame.K_7:
                        DoorCoveringHole(6)
                        print("7")
                    elif event.key == pygame.K_8:
                        DoorCoveringHole(7)
                        print("8")
                    elif event.key == pygame.K_9:
                        DoorCoveringHole(8)
                        print("9")

            if TrapMolesIntoAHoleButton.inRange(pos):
                print("clicked button 2")
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN:
                    print("key pressed")
                    if event.key == pygame.K_1:
                        print("1")
                        PlaceTrapDoor(0)
                    elif event.key == pygame.K_2:
                        print("2")
                        PlaceTrapDoor(1)
                    elif event.key == pygame.K_3:
                        PlaceTrapDoor(2)
                        print("3")
                    elif event.key == pygame.K_4:
                        PlaceTrapDoor(3)
                        print("4")
                    elif event.key == pygame.K_5:
                        PlaceTrapDoor(4)
                        print("5")
                    elif event.key == pygame.K_6:
                        PlaceTrapDoor(5)
                        print("6")
                    elif event.key == pygame.K_7:
                        PlaceTrapDoor(6)
                        print("7")
                    elif event.key == pygame.K_8:
                        PlaceTrapDoor(7)
                        print("8")
                    elif event.key == pygame.K_9:
                        PlaceTrapDoor(8)
                        print("9")

            if GetRidOfMolesForFiveSecondsButton.inRange(pos):
                print("clicked button 3")
                GetRidOfMolesForFiveSeconds()
                display.blit(ddos_mod_image, (0,100))

            if SlowDownMolesButton.inRange(pos):
                display.blit(idps_mod_image, (0,100))
                print("clicked button 4")
                slowdown=True


            
                button_selected= True
        
            if(not button_selected):
                #print('mouse')
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