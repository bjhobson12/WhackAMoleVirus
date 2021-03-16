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
