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
        self.t = 0
        self.x = 640
        self.y = -360
        self.Vi = 10
        self.Ang = 398503743
        self.right = True
        self.limit = 0
        #status
        self.health = 5
        self.bonus = 0
    def jump(self):
        if self.right:
            self.Ang = 60
        else:
            self.ang = 120
        self.x = self.Vi*n.cos(self.Ang)*self.t
        self.y = 1*(((self.t**2))/2) + self.Vi* n.sin(self.Ang) + self.x
        self.t +=1
        if self.y <= 20:
            self.y = 20

    


#End