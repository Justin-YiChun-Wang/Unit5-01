'''
Created: Nov 2024
unit5-01.py
'''
import pygame

from pygame import Color, Rect
from pygame import draw
from pygame import display

SCREEN_SIZE = (500, 500)

pygame.init()

gameDisplay = display.set_mode(SCREEN_SIZE)

gameDisplay.fill(Color('lightblue'))

draw.rect(gameDisplay, Color('brown'), Rect(100, 200, 300, 200))
draw.polygon(gameDisplay, Color('black'), [(100, 200), (400, 200), (250, 50)])

draw.rect(gameDisplay, Color('green'), Rect(0, 400, 500, 100))

draw.circle(gameDisplay, Color('yellow'), (50, 50), 50)

display.flip()

input("Press enter to exit")
