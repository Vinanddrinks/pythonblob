# Python Blob V2#
# description : main ressource file for the project classes 
# Authors : Joseph

# importation
import pygame as pg
import numpy as n
import time as t
import random as r
from main import*
# End-importation

#Declaration
score = 0
window = pg.display.set_mode((1280, 720))
#end Declaration

def ScoreClock():                       #pour le score affiché sur l'écran
    global ScoreLat
    global score
    if t.time()-ScoreLat >= 0.1:
        ScoreLat = t.time()
        score += 1

def GameWindow():
    window.blit(fond,(0,0))
    window.blit(imageperso, (blob.x, blob.y))
    pg.display.update()