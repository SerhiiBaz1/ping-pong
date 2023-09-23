import pygame
from random import *
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
ball = Player(450,300,50,50,'ball.png')
plate = Player(850,300,30,180,'platforma.png')

W,H = 900,600
pygame.display.set_caption('Ping-Pong')
scr = pygame.display.set_mode((W,H))
fon = pygame.transform.scale(pygame.image.load('eeeeeeeee.jpg'),(W,H))
run = True
fps = pygame.time.Clock()

dx =1
dy =1
pm =3
f = 100
rand_lis = [1,-1]
def moove():
    global dx,dy
    ball.imgrect.x +=dx
    ball.imgrect.y +=dy
    if ball.imgrect.bottom >H:
        dy = -1
    if player.imgrect.colliderect(ball.imgrect):
        dx =1
    if plate.imgrect.colliderect(ball.imgrect):
        dx =-1
    if ball.imgrect.right >W:
        ball.imgrect.x, ball.imgrect.y = 330,219
    if ball.imgrect.top < 0:
        dy = +1
    if ball.imgrect.left <=0:
        ball.imgrect.x, ball.imgrect.y = 330,219
        dx =1

def plateq():
    global pm
    global f
    if f == 100:
        pm = choice(rand_lis)
        f =0

    plate.imgrect.y -= pm
    if plate.imgrect.top <=0:
        pm = -3
    elif plate.imgrect.bottom>=H:
        pm = 3

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and player.imgrect.top > 0:
        player.imgrect.y -= 2
    if key[pygame.K_DOWN] and player.imgrect.bottom < 600 :
        player.imgrect.y += 2



    moove()
    plateq()
    scr.blit(fon,(0,0))
    scr.blit(player.img_new,(player.imgrect.x,player.imgrect.y))
    scr.blit(plate.img_new,(plate.imgrect.x,plate.imgrect.y))

    scr.blit(ball.img_new,(ball.imgrect.x,ball.imgrect.y))

    f+=1
    fps.tick(120)
    pygame.display.update()





