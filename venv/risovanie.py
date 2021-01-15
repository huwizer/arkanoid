import pygame, time, settings as set, dvigenie as dvi
from pygame import display, event, draw, key

pygame.init()
window = display.set_mode([set.SCREEN_WIDTH, set.SCREEN_HEIGHT])


def dra():
    # Отрисовка
    draw.rect(window, [255, 246, 18], dvi.ne_krug)
    draw.circle(window, [33, 55, 77], dvi.krug.center, set.RADIUS)

    display.flip()

    window.fill([138, 21, 255])
