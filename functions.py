# Python Blob V2#
# description : main ressource file for the project classes 
# Authors : Joseph,Vincent,Anaïs,Léna

# importation
from Classes import *
import pygame as pg
import numpy as n
import time as t
import random as r
import os
# End-importation

# Colors
white=(255, 255, 255)
pink = (255, 107, 255)
black=(0, 0, 0)
screen_w=1280
screen_h=720

window = pg.display.set_mode((1280, 720),pg.DOUBLEBUF, 32)

os.environ['SDL_VIDEO_CENTERED'] = '1'

font = "Retro.ttf"
font2 = "SadanaSquare.ttf"
screen  = pg.display.set_mode((1280, 720),pg.DOUBLEBUF, 32)

# Variables
def chooseSong(health):
    if health == 3:

        pg.mixer.music.load('musiques/Powerup.ogg')
        pg.mixer.music.play(-1)
    elif health == 2:

        pg.mixer.music.load('musiques/Maze.wav')
        pg.mixer.music.play(-1)
    elif health == 1:

        pg.mixer.music.load('musiques/Dungeonboss.wav')
        pg.mixer.music.play(-1)
    elif health == 0:

        pg.mixer.music.load('musiques/Virtualboy.wav')
        pg.mixer.music.play(-1)


def text_format(message, textFont, textSize, textColor):
    newFont=pg.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText

def main_menu():
    menu=True
    select = "Start"
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
                    select="Start"
                    
                elif event.key==pg.K_DOWN:
                    select="quit"
                    
                if event.key==pg.K_RETURN:
                    if select=="Start":
                        return False
                    if select=="quit":
                        pg.quit()
                        quit()

        # Main Menu UI
        fondt = pg.image.load('resources/FondPrincipal.png')
        window.blit(fondt, (0,0))
        title=text_format("PROTECT LITTLE BUD", font2, 91, white)
        title2=text_format("PROTECT LITTLE BUD", font2, 90, pink)
        if select=="Start":
            Text_Start=text_format("START", font, 75, white)
        else:
            Text_Start = text_format("START", font, 75, black)
        if select=="quit":
            Text_Quit=text_format("QUIT", font, 75, white)
        else:
            Text_Quit = text_format("QUIT", font, 75, black)

        title_r=title.get_rect()
        title2_r=title2.get_rect()
        start_r=Text_Start.get_rect()
        quit_r=Text_Quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_w/2 - (title_r[2]/2), 80))
        screen.blit(title2, (screen_w/2 - (title2_r[2]/2)-3, 83))
        screen.blit(Text_Start, (screen_w/2 - (start_r[2]/2), 300))
        screen.blit(Text_Quit, (screen_w/2 - (quit_r[2]/2), 360))
        pg.display.update()

def gameover(score):
    menu=True
    select = "Retry"
    constante = True

    while menu:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                quit()
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_UP:
                    select="Retry"
                    
                elif event.key==pg.K_DOWN:
                    select="quit"
                    
                if event.key==pg.K_RETURN:
                    if select=="Retry":
                         chooseSong(3)
                         return
                    if select=="quit":
                        pg.quit()
                        quit()

        # Main Menu UI
        fondt = pg.image.load('resources/FondPrincipal.png')
        window.blit(fondt, (0,0))
        title=text_format("Game Over", font2, 91, white)
        title2=text_format("Game Over", font2, 90, black)
        Score =text_format(str(score),font2,80,pink)
        if select=="Retry":
            Text_Start=text_format("RETRY", font, 75, white)
        else:
            Text_Start = text_format("RETRY", font, 75, black)
        if select=="quit":
            Text_Quit=text_format("QUIT", font, 75, white)
        else:
            Text_Quit = text_format("QUIT", font, 75, black)

        title_r=title.get_rect()
        title2_r=title2.get_rect()
        start_r=Text_Start.get_rect()
        quit_r=Text_Quit.get_rect()

        # Main Menu Text
        screen.blit(Score,(screen_w/2 - 35,500))
        screen.blit(title, (screen_w/2 - (title_r[2]/2), 80))
        screen.blit(title2, (screen_w/2 - (title2_r[2]/2)-3, 83))
        screen.blit(Text_Start, (screen_w/2 - (start_r[2]/2), 300))
        screen.blit(Text_Quit, (screen_w/2 - (quit_r[2]/2), 360))
        pg.display.update()
# End - Variable