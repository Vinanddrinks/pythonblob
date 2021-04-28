# Python Blob V2#
# description : main ressource file for the project classes 
# Authors : Vincent, Joseph, Hugo

# importation
import pygame as pg
import numpy as n
import time as t
import random as r
from functions import *
import os
# End-importation

#Begin

class player_entity:
    def __init__(self, x, y):
        #coordinates values
        self.t = 0
        self.x = x
        self.y = y
        self.vel = 10
        self.vely = 0
        self.right = False
        self.left = True
        
        
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

        self.actualsprites0 = self.sprites0_right
        self.actualsprites1 = self.sprites1_right
        self.actualsprites2 = self.sprites2_left
        
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

        #infos about blob sprites management
        self.current_sprite = 0
        self.image = self.sprites0_right[0]
        self.Jump = False

        #hitboxes management 
        self.hitboxblob = (self.x + 36, self.y + 115, 120, 30)
        self.sizey = 0

        #score management 
        self.score = 0
        self.scorecopy = 0
        self.scorecopy2 = 0

        self.score1 = 0
        self.score10 = 0
        self.score100 = 0

        self.scorelist = []
        self.scorelist2 = []

        self.countscore = 0
        self.countscore2 = 0

        self.spritesscore = []

        self.spritesscore.append(pg.image.load('resources/0.png'))
        self.spritesscore.append(pg.image.load('resources/1.png'))
        self.spritesscore.append(pg.image.load('resources/2.png'))
        self.spritesscore.append(pg.image.load('resources/3.png'))
        self.spritesscore.append(pg.image.load('resources/4.png'))
        self.spritesscore.append(pg.image.load('resources/5.png'))
        self.spritesscore.append(pg.image.load('resources/6.png'))
        self.spritesscore.append(pg.image.load('resources/7.png'))
        self.spritesscore.append(pg.image.load('resources/8.png'))
        self.spritesscore.append(pg.image.load('resources/9.png'))


    def mouvement(self):
        self.y += self.vely  #gerer les déplacements y
        keys = pg.key.get_pressed()


        if keys[pg.K_LEFT] and self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False

            if self.current_sprite < 6 :
                if self.health == 3 :
                    self.image = self.sprites0_left[int(self.current_sprite)]
                    self.actualsprites0 = self.sprites0_left

                if self.health == 2 :
                    self.image = self.sprites1_left[int(self.current_sprite)]
                    self.actualsprites1 = self.sprites1_left

                if self.health == 1 :
                    self.image = self.sprites2_left[int(self.current_sprite)]
                    self.actualsprites2 = self.sprites2_left   


        elif keys[pg.K_RIGHT] and self.x < 1150:
            self.x += self.vel
            self.left = False
            self.right = True

            if self.current_sprite < 6 :
                if self.health == 3 :
                    self.image = self.sprites0_right[int(self.current_sprite)]
                    self.actualsprites0 = self.sprites0_right 
                
                if self.health == 2 :
                    self.image = self.sprites1_right[int(self.current_sprite)]
                    self.actualsprites1 = self.sprites1_right

                if self.health == 1 :
                    self.image = self.sprites2_right[int(self.current_sprite)]
                    self.actualsprites2 = self.sprites2_right


        if self.y >= 500:              #position du perso
            self.vely = 0              #si dans le sol => remonte a 500
            if self.y > 500:           #si sur sol vely=0 car pas de gravité
                self.y = 500
        else :
            if keys[pg.K_DOWN]:
                self.vely = min(self.vely + 5, 100)
            else:
                self.vely = min(self.vely + 1, 100)     #ajout de la gravité


    def moveup(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.Jump = True
        if self.Jump == True and self.health != 0:
            if self.current_sprite < 6 :
                if int(self.current_sprite) == 4 :
                    self.vely = -16
                    self.sizey -= 20

                if int(self.current_sprite) == 5 :
                   self.sizey -= 10

                if self.health == 3 :
                    if keys[pg.K_LEFT] and self.x > self.vel :
                        self.image = self.sprites0_left[int(self.current_sprite)]
                    elif keys[pg.K_RIGHT] and self.x < 1100:
                        self.image = self.sprites0_right[int(self.current_sprite)]
                    else : 
                        self.image = self.actualsprites0[int(self.current_sprite)]

                elif self.health == 2 :
                    if keys[pg.K_LEFT] and self.x > self.vel :
                        self.image = self.sprites1_left[int(self.current_sprite)] 
                    elif keys[pg.K_RIGHT] and self.x < 1100:
                        self.image = self.sprites1_right[int(self.current_sprite)]
                    else : 
                        self.image = self.actualsprites1[int(self.current_sprite)]
                        
                elif self.health == 1 :
                    if keys[pg.K_LEFT] and self.x > self.vel :
                        self.image = self.sprites2_left[int(self.current_sprite)]   
                    elif keys[pg.K_RIGHT] and self.x < 1100:
                        self.image = self.sprites2_right[int(self.current_sprite)]
                    else : 
                        self.image = self.actualsprites2[int(self.current_sprite)]
                
            else : 
                self.current_sprite = 0
                self.sizey = 0
                self.Jump = False
            self.current_sprite += 0.3

        if self.y < -350 :
            self.y = 500
            self.health = self.health - 1

        self.hitboxblob = (self.x + 42  , self.y + 120 + self.sizey, 110 , 70)

        if self.health <= 0 :
            self.y = 500
            self.x = 540
            self.image = pg.image.load('resources/mort2.png')
            self.vel = 0
            self.hitboxblob = ( 0, 0, 0, 0)


    def scoreblob(self):

        self.scorecopy2 = self.score
        self.scorecopy = self.scorecopy2

        while self.scorecopy != 0 : 
            self.countscore = 0
            while self.scorecopy >= 10 :
                while self.scorecopy >= 10 :
                    self.scorecopy = int(self.scorecopy/10)
                    self.countscore += 1
                self.scorelist.append(self.scorecopy)

                if int(self.scorecopy2/10)%10 == 0 :
                    self.scorelist.append(0)

                self.scorecopy = self.scorecopy2 - self.scorecopy*(10**self.countscore)
                self.scorecopy2 = self.scorecopy
                if self.countscore > self.countscore2 :
                    self.countscore2 = self.countscore
                self.countscore = 0
            self.scorelist.append(self.scorecopy)

            if self.scorecopy < 10 :
                self.scorecopy = 0

            if self.countscore2 == 2 :
                self.score1 = self.scorelist[2]
                self.score10 = self.scorelist[1]
                self.score100 = self.scorelist[0]

            if self.countscore2 == 1 :
                self.score1 = self.scorelist[1]
                self.score10 = self.scorelist[0]

            if self.countscore2 == 0 :
                self.score1 = self.scorelist[0]

            self.scorelist2 = self.scorelist
            self.scorelist = []



#Fin classe joueur

class ennemy:
    def __init__(self):
        #variables initialisation
        self.sprite = pg.image.load('resources/covidtest.png')
        if r.choice([True,False]):
            self.x = 1200
            self.theta = n.radians(r.randint(90,225))
        else:
            self.x = 10
            self.theta = n.radians(r.randint(-45,90))
        self.vi = r.randint(1200000,1600000)
        self.x_init = self.x
        self.y = r.randint(-360,0)
        self.init_height = self.y
        self.vi = 200
        self.time = 0
        self.gravity = r.randint(30,60)

        self.ennemyrect = self.sprite.get_rect()
        #end variable initialisation
    def trajectory(self):
        self.time += 0.045
        self.x = self.vi*n.cos(self.theta)*self.time + self.x_init
        self.y = self.gravity*((self.time*self.time)/2) - self.vi*n.sin(self.theta)*self.time - self.init_height
    

#End