# Python Blob V2#
# description : main ressource file for the project classes 
# Authors : Vincent.

# importation
import pygame as pg
import numpy as n
import time as t
import random as r
# End-importation

#Begin
class player_entity:
    def __init__(self):
        #coordinates values
        self.x = 640
        self.y = 360
        self.Vi = 0
        self.Ang = 0
        #status
        self.health = 5


#End