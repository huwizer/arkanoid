import pygame, time, settings as set

speedx = 5
speedy = 5
krug = pygame.Rect(250, 100, set.RADIUS * 2, set.RADIUS * 2)
ne_krug = pygame.Rect(100, 600, 250, 10)


def log():
    global speedx, speedy
    # Движение круга и отбивка по x
    krug.x += speedx

    if krug.right > set.SCREEN_WIDTH:
        krug.right = set.SCREEN_WIDTH
        speedx = -5

    if krug.x < 0:
        krug.x = 0
        speedx = 5

    if ne_krug.colliderect(krug) == 1 and speedx > 0:
        krug.right = ne_krug.x
        speedx = -5
    elif ne_krug.colliderect(krug) == 1 and speedx < 0:
        krug.x = ne_krug.right
        speedx = 5

    # Движение круга и отбивка по y
    krug.top += speedy

    if krug.bottom > set.SCREEN_HEIGHT:
        exit()

    if krug.y < 0:
        krug.y = 0
        speedy = 5

    if ne_krug.colliderect(krug) == 1 and speedy > 0:
        krug.bottom = ne_krug.top
        speedy = -5
    elif ne_krug.colliderect(krug) == 1 and speedy < 0:
        krug.top = ne_krug.bottom
        speedy = 5
