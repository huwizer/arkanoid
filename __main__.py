import pygame,time,settings as set
krug=pygame.Rect(100,100,set.RADIUS*2,set.RADIUS*2)
ne_krug=pygame.Rect(50,600,250,10)
pygame.init()
window=pygame.display.set_mode([set.SCREEN_WIDTH,set.SCREEN_HEIGHT])
speedx=0
speedy=3

while True:


    krug[0]+=speedx


    if krug.right>set.SCREEN_WIDTH:
        krug.right=set.SCREEN_WIDTH
        speedx=-10

    if krug.x < 0:
        krug.x=0
        speedx = 10


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





    pygame.draw.rect(window,[255, 246, 18],ne_krug)
    # pygame.draw.rect(window,[255, 246, 18],krug)
    pygame.draw.circle(window,[33,55,77],krug.center,set.RADIUS)

    time.sleep(1 / 60)
    pygame.display.flip()
    pygame.event.get()
    window.fill([138,21,255])

