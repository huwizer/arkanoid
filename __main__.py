import pygame,time,settings as set
from pygame import display,event,draw,key
pygame.init()
window=display.set_mode([set.SCREEN_WIDTH,set.SCREEN_HEIGHT])
#Подготовка управления
key.set_repeat(75)
#Подготовка модели
speedx=5
speedy=5
krug=pygame.Rect(600,600,set.RADIUS*2,set.RADIUS*2)
ne_krug=pygame.Rect(100,600,250,10)


while True:

    #Обработка событий
    time.sleep(1 / 360)

    ev=event.get()

    for e in ev:

        if e.type==pygame.QUIT:
            exit()

        if e.type==pygame.KEYDOWN and e.key==pygame.K_LEFT:
            ne_krug.x -= 25
            if ne_krug.colliderect(krug) == 1:
                ne_krug.x = krug.right
            if ne_krug.x<0:
                ne_krug.x=0


        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            ne_krug.x += 25
            if ne_krug.colliderect(krug) == 1:
                ne_krug.right=krug.x
            if ne_krug.right>set.SCREEN_WIDTH:
                ne_krug.right=set.SCREEN_WIDTH







    #Движение круга и отбивка по x
    krug.x+=speedx


    if krug.right>set.SCREEN_WIDTH:
        krug.right=set.SCREEN_WIDTH
        speedx=-5

    if krug.x < 0:
        krug.x=0
        speedx = 5

    if ne_krug.colliderect(krug)==1 and speedx>0:
        krug.right=ne_krug.x
        speedx=-5
    elif ne_krug.colliderect(krug)==1 and speedx<0:
        krug.x=ne_krug.right
        speedx=5


    #Движение круга и отбивка по y
    krug.top += speedy


    if krug.bottom>set.SCREEN_HEIGHT:
        krug.bottom = set.SCREEN_HEIGHT
        speedy=-5

    if krug.y< 0:
        krug.y=0
        speedy=5

    if ne_krug.colliderect(krug)==1 and speedy>0:
        krug.bottom=ne_krug.top
        speedy=-5
    elif ne_krug.colliderect(krug)==1 and speedy<0:
        krug.top = ne_krug.bottom
        speedy = 5










    #Отрисовка
    draw.rect(window,[255, 246, 18],ne_krug)
    # draw.rect(window,[255, 246, 18],krug)
    draw.circle(window,[33,55,77],krug.center,set.RADIUS)


    display.flip()

    window.fill([138,21,255])

