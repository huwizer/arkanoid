import pygame,time,settings as set
krug=[set.RADIUS,set.RADIUS]
ne_krug=pygame.Rect(50,600,250,10)
pygame.init()
window=pygame.display.set_mode([set.SCREEN_WIDTH,set.SCREEN_HEIGHT])
speedx=10
speedy=10

while True:


    krug[0]+=speedx
    krug[1]+=speedy

    if krug[0]>set.SCREEN_WIDTH-set.RADIUS:
        krug[0]=set.SCREEN_WIDTH-set.RADIUS
        speedx=-10

    if krug[0] < set.RADIUS:
        krug[0]=set.RADIUS
        speedx = 10

    if krug[1]>set.SCREEN_HEIGHT-set.RADIUS:
        krug[1] = set.SCREEN_HEIGHT-set.RADIUS
        speedy=-10

    if krug[1]< set.RADIUS:
        krug[1]=set.RADIUS
        speedy=10

    pygame.draw.circle(window, [255, 246, 18], krug, set.RADIUS)
    pygame.draw.rect(window,[255, 246, 18],ne_krug)

    time.sleep(1 / 60)
    pygame.display.flip()
    pygame.event.get()
    window.fill([138,21,255])

