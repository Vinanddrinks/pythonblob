# Python Blob V2#
# description : main ressource file for the project classes 
# Authors : Joseph

# importation
import pygame as pg
import numpy as n
import time as t
import random as r
# End-importation

# Variables
def chooseSong(health):
    if health == 3:
        pg.mixer.music.load('musiques/Powerup.wav')
        pg.mixer.music.play(-1)
    elif health == 2:
        pg.mixer.music.load('musiques/Maze.wav')
        pg.mixer.music.play(-1)
    elif health == 1:
        pg.mixer.music.load('musiques/Dungeonboss.ogg')
        pg.mixer.music.play(-1)
    elif health == 0:
        pg.mixer.music.load('musiques/Virtualboy.wav')
        pg.mixer.music.play(-1)




# End - Variable