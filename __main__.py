import pygame,time,settings as set
krug=[set.RADIUS,set.RADIUS]
pygame.init()
window=pygame.display.set_mode([set.SCREEN_WIDTH,set.SCREEN_HEIGHT])
speedx=2
speedy=2

while True:


    krug[0]+=speedx

    if krug[0]>set.SCREEN_WIDTH-set.RADIUS:
        speedx=-2

    if krug[0] < set.SCREEN_WIDTH - set.RADIUS:
        speedx = 2

    #if krug[1]>set.SCREEN_HEIGHT-set.RADIUS:
        #speedy=-2


    pygame.draw.circle(window, [255, 246, 18], krug, set.RADIUS)

    time.sleep(1 / 60)
    pygame.display.flip()
    pygame.event.get()
    window.fill([138,21,255])

