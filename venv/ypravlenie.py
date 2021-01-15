import pygame, time, settings as set, dvigenie as dvi
from pygame import display, event, draw, key

pygame.init()
key.set_repeat(75)


def cont():
    ev = event.get()

    for e in ev:

        if e.type == pygame.QUIT:
            exit()

        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            dvi.ne_krug.x -= 25
            if dvi.ne_krug.colliderect(dvi.krug) == 1:
                dvi.ne_krug.x = dvi.krug.right
            if dvi.ne_krug.x < 0:
                dvi.ne_krug.x = 0

        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            dvi.ne_krug.x += 25
            if dvi.ne_krug.colliderect(dvi.krug) == 1:
                dvi.ne_krug.right = dvi.krug.x
            if dvi.ne_krug.right > set.SCREEN_WIDTH:
                dvi.ne_krug.right = set.SCREEN_WIDTH

        # управление платформой
        if e.type == pygame.MOUSEMOTION:
            if dvi.ne_krug.x < dvi.krug.x:
                sleva = True
            else:
                sleva = False
            print(e.pos)
            dvi.ne_krug.centerx = e.pos[0]

            if sleva == True:
                if dvi.ne_krug.colliderect(dvi.krug) == 1:
                    dvi.ne_krug.right = dvi.krug.x
            if sleva == False:
                if dvi.ne_krug.colliderect(dvi.krug) == 1:
                    dvi.ne_krug.x = dvi.krug.right

            if dvi.ne_krug.x < 0:
                dvi.ne_krug.x = 0
            if dvi.ne_krug.right > set.SCREEN_WIDTH:
                dvi.ne_krug.right = set.SCREEN_WIDTH
