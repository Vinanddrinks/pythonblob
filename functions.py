# Python Blob V2#
# description : main ressource file for the project classes 
# Authors : Joseph,Vincent,Anaïs

# importation
import pygame as pg
import numpy as n
import time as t
import random as r
import os
# End-importation

# Colors
white=(255, 255, 255)
pink = (223, 45, 201)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
grey = (85, 85, 85)
screen_width=1280
screen_height=720

os.environ['SDL_VIDEO_CENTERED'] = '1'

font = "Retro.ttf"
screen  = pg.display.set_mode((1280, 720),pg.DOUBLEBUF, 32)

# Variables
def chooseSong(health):
    if health == 3:
        pg.mixer.music.fadeout(500)
        pg.mixer.music.load('musiques/Powerup.ogg')
        pg.mixer.music.play(-1)
    elif health == 2:
        pg.mixer.music.fadeout(500)
        pg.mixer.music.load('musiques/Maze.wav')
        pg.mixer.music.play(-1)
    elif health == 1:
        pg.mixer.music.fadeout(500)
        pg.mixer.music.load('musiques/Dungeonboss.wav')
        pg.mixer.music.play(-1)
    elif health == 0:
        pg.mixer.music.fadeout(500)
        pg.mixer.music.load('musiques/Virtualboy.wav')
        pg.mixer.music.play(-1)


def text_format(message, textFont, textSize, textColor):
    newFont=pg.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText

def main_menu():
    menu=True
    selected = "Start"
    constante = True

    pg.mixer.music.load('musiques/Nightshade.ogg')
    pg.mixer.music.play(-1)

    while menu:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                quit()
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_UP:
                    selected="Start"
                    
                elif event.key==pg.K_DOWN:
                    selected="quit"
                    
                if event.key==pg.K_RETURN:
                    if selected=="Start":
                        return False
                    if selected=="quit":
                        pg.quit()
                        quit()

        # Main Menu UI
        screen.fill(black)
        title=text_format("PROTECT LITTLE BUD", font, 90, pink)
        if selected=="Start":
            text_start=text_format("START", font, 75, white)
        else:
            text_start = text_format("START", font, 75, grey)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, grey)

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pg.display.update()


# End - Variable