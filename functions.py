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

test = 0
ScoreLat = 0

# End - Variable

def SpreadTime():
    global test
    global ScoreLat
    if t.time() - ScoreLat >= 0.1:
        ScoreLat = t.time()
        score += 1
    print(score)
    