import pygame,time,settings as set
from pygame import display,event,draw
krug=pygame.Rect(600,600,set.RADIUS*2,set.RADIUS*2)
ne_krug=pygame.Rect(100,600,250,10)
pygame.init()
window=display.set_mode([set.SCREEN_WIDTH,set.SCREEN_HEIGHT])
speedx=10
speedy=10

while True:

    #Обработка событий

    ev=event.get()

    for e in ev:

        if e.type==pygame.QUIT:
            exit()

        if e.type==pygame.KEYDOWN and e.key==pygame.K_LEFT:
            ne_krug.x-=3







    #Движение круга и отбивка по x
    krug.x+=speedx


    if krug.right>set.SCREEN_WIDTH:
        krug.right=set.SCREEN_WIDTH
        speedx=-10

    if krug.x < 0:
        krug.x=0
        speedx = 10

    if ne_krug.colliderect(krug)==1 and speedx>0:
        krug.right=ne_krug.x
        speedx=-10
    elif ne_krug.colliderect(krug)==1 and speedx<0:
        krug.x=ne_krug.right
        speedx=10


    #Движение круга и отбивка по y
    krug.top += speedy


    if krug.bottom>set.SCREEN_HEIGHT:
        krug.bottom = set.SCREEN_HEIGHT
        speedy=-10

    if krug.y< 0:
        krug.y=0
        speedy=10

    if ne_krug.colliderect(krug)==1 and speedy>0:
        krug.bottom=ne_krug.top
        speedy=-10
    elif ne_krug.colliderect(krug)==1 and speedy<0:
        krug.top = ne_krug.bottom
        speedy = 10











    draw.rect(window,[255, 246, 18],ne_krug)
    # draw.rect(window,[255, 246, 18],krug)
    draw.circle(window,[33,55,77],krug.center,set.RADIUS)

    time.sleep(1 / 60)
    display.flip()

    window.fill([138,21,255])

