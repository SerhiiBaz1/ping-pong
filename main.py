import pygame
pygame.init()
W,H = 900,600
pygame.display.set_caption('Ping-Pong')
scr = pygame.display.set_mode((W,H))
fon = pygame.transform.scale(pygame.image.load('eeeeeeeee.jpg'),(W,H))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    scr.blit(fon,(0,0))
    pygame.display.update()


