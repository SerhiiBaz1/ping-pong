import pygame
pygame.init()
class Player():
    def __init__(self,x,y,w,h,img):
        self.x = x
        self.y = y
        self.w=w
        self.h=h
        self.img=img
        self.img_new = pygame.transform.scale(pygame.image.load(self.img),(self.w,self.h))
        self.imgrect = self.img_new.get_rect(center = (self.x,self.y))
player = Player(50,300,30,180,'platforma.png')
W,H = 900,600
pygame.display.set_caption('Ping-Pong')
scr = pygame.display.set_mode((W,H))
fon = pygame.transform.scale(pygame.image.load('eeeeeeeee.jpg'),(W,H))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        pass
    if key[pygame.K_DOWN]:
        pass
    scr.blit(fon,(0,0))
    scr.blit(player.img_new,(player.imgrect.x,player.imgrect.y))
    pygame.display.update()



