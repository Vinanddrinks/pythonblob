# Python Blob V2#
# description : main ressource file for the project classes 
# Authors : Vincent, Joseph

# importation
import pygame as pg
import numpy as n
import time as t
import random as r
from functions import *
# End-importation

#Begin

class player_entity:
    def __init__(self, x, y):
        #coordinates values
        self.t = 0
        self.x = x
        self.y = y
        self.vel = 15
        self.vely = 0
        self.right = False
        self.left = True
        self.Vi = 10
        self.Ang = 398503743
        
        #status
        self.health = 5
        self.bonus = 0
    
    #def jump(self):
        #if self.right:
            #self.Ang = 60
        #else:
            #self.ang = 120
        #self.x = self.Vi*n.cos(self.Ang)*self.t
        #self.y = 1*(((self.t**2))/2) + self.Vi* n.sin(self.Ang) + self.x
        #self.t +=1
        #if self.y <= 20:
            #self.y = 20

    
    def mouvement(self):
        self.y += self.vely  #gerer les déplacements y
        keys = pg.key.get_pressed()


        if keys[pg.K_LEFT] and self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False

        elif keys[pg.K_RIGHT] and self.x < 1100:
            self.x += self.vel
            self.left = False
            self.right = True

        #elif keys[pg.K_SPACE]:
            #self.vely = -20

        if self.y >= 600:              #position du perso
            self.vely = 0              #si dans le sol => remonte a 600
            if self.y > 600:           #si sur sol vely=0 car pas de gravité
                self.y = 600
        else :
            if keys[pg.K_DOWN]:
                self.vely = min(self.vely + 10, 100)
            else:
                self.vely = min(self.vely + 3, 100)     #ajout de la gravité

    def moveup(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.vely = -30

#End