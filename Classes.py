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
        self.health = 3
        self.bonus = 0

        #all sprites
        self.sprites0_right = []
        self.sprites0_left = []
        self.sprites1_right = []
        self.sprites1_left = []
        self.sprites2_right = []
        self.sprites2_left = []
        self.sprites3_right = []
        self.sprites3_left = []
        
        #SPRITE 0 ( normal )
        self.sprites0_right.append(pg.image.load('resources/saut_normal_droit_0.png'))
        self.sprites0_right.append(pg.image.load('resources/saut_normal_droit_1.png'))
        self.sprites0_right.append(pg.image.load('resources/saut_normal_droit_2.png'))
        self.sprites0_right.append(pg.image.load('resources/saut_normal_droit_3.png'))
        self.sprites0_right.append(pg.image.load('resources/saut_normal_droit_4.png'))
        self.sprites0_right.append(pg.image.load('resources/saut_normal_droit_5.png'))

        self.sprites0_left.append(pg.image.load('resources/saut_normal_gauche_0.png'))
        self.sprites0_left.append(pg.image.load('resources/saut_normal_gauche_1.png'))
        self.sprites0_left.append(pg.image.load('resources/saut_normal_gauche_2.png'))
        self.sprites0_left.append(pg.image.load('resources/saut_normal_gauche_3.png'))
        self.sprites0_left.append(pg.image.load('resources/saut_normal_gauche_4.png'))
        self.sprites0_left.append(pg.image.load('resources/saut_normal_gauche_5.png'))

        #SPRITE 1
        self.sprites1_right.append(pg.image.load('resources/saut_stade1_droit_0.png'))
        self.sprites1_right.append(pg.image.load('resources/saut_stade1_droit_1.png'))
        self.sprites1_right.append(pg.image.load('resources/saut_stade1_droit_2.png'))
        self.sprites1_right.append(pg.image.load('resources/saut_stade1_droit_3.png'))
        self.sprites1_right.append(pg.image.load('resources/saut_stade1_droit_4.png'))
        self.sprites1_right.append(pg.image.load('resources/saut_stade1_droit_5.png'))

        self.sprites1_left.append(pg.image.load('resources/saut_stade1_gauche_0.png'))
        self.sprites1_left.append(pg.image.load('resources/saut_stade1_gauche_1.png'))
        self.sprites1_left.append(pg.image.load('resources/saut_stade1_gauche_2.png'))
        self.sprites1_left.append(pg.image.load('resources/saut_stade1_gauche_3.png'))
        self.sprites1_left.append(pg.image.load('resources/saut_stade1_gauche_4.png'))
        self.sprites1_left.append(pg.image.load('resources/saut_stade1_gauche_5.png'))

        #SPRITE 2
        self.sprites2_right.append(pg.image.load('resources/saut_stade2_droit_0.png'))
        self.sprites2_right.append(pg.image.load('resources/saut_stade2_droit_1.png'))
        self.sprites2_right.append(pg.image.load('resources/saut_stade2_droit_2.png'))
        self.sprites2_right.append(pg.image.load('resources/saut_stade2_droit_3.png'))
        self.sprites2_right.append(pg.image.load('resources/saut_stade2_droit_4.png'))
        self.sprites2_right.append(pg.image.load('resources/saut_stade2_droit_5.png'))

        self.sprites2_left.append(pg.image.load('resources/saut_stade2_gauche_0.png'))
        self.sprites2_left.append(pg.image.load('resources/saut_stade2_gauche_1.png'))
        self.sprites2_left.append(pg.image.load('resources/saut_stade2_gauche_2.png'))
        self.sprites2_left.append(pg.image.load('resources/saut_stade2_gauche_3.png'))
        self.sprites2_left.append(pg.image.load('resources/saut_stade2_gauche_4.png'))
        self.sprites2_left.append(pg.image.load('resources/saut_stade2_gauche_5.png'))

        #SPRITE 3 ( mort )
        self.sprites3_right.append(pg.image.load('resources/mort2.png'))
        self.sprites3_left.append(pg.image.load('resources/mort1.png'))

        #infos about blob sprites management
        self.image = self.sprites0_right[0]
        self.current_sprite = 0
    
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
            
            if self.current_sprite == 0 :
                if self.health == 3 :
                    self.image = self.sprites0_left[int(self.current_sprite)]
                if self.health == 2 :
                    self.image = self.sprites1_left[int(self.current_sprite)]
                if self.health == 1 :
                    self.image = self.sprites2_left[int(self.current_sprite)]


        elif keys[pg.K_RIGHT] and self.x < 1100:
            self.x += self.vel
            self.left = False
            self.right = True
            
            if self.current_sprite == 0 :
                if self.health == 3 :
                    self.image = self.sprites0_right[int(self.current_sprite)]
                if self.health == 2 :
                    self.image = self.sprites1_right[int(self.current_sprite)]
                if self.health == 1 :
                    self.image = self.sprites2_right[int(self.current_sprite)]


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
        Jump = True
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            if Jump == True:
                self.vely = -30

                Jump = False
                for i in range(24):
                    if self.health == 3 :
                        if keys[pg.K_LEFT] and self.x > self.vel :
                            self.image = self.sprites0_left[int(self.current_sprite)]
                        elif keys[pg.K_RIGHT] and self.x < 1100:
                            self.image = self.sprites0_right[int(self.current_sprite)]
                    elif self.health == 2 :
                        if keys[pg.K_LEFT] and self.x > self.vel :
                            self.image = self.sprites1_left[int(self.current_sprite)]
                        elif keys[pg.K_RIGHT] and self.x < 1100:
                            self.image = self.sprites1_right[int(self.current_sprite)]
                    elif self.health == 1 :
                        if keys[pg.K_LEFT] and self.x > self.vel :
                            self.image = self.sprites2_left[int(self.current_sprite)]
                        elif keys[pg.K_RIGHT] and self.x < 1100:
                            self.image = self.sprites2_right[int(self.current_sprite)]


    def actualiseSprites(self):
        global imageperso
        imageperso = self.image
        

#End