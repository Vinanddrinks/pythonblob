from main import*
from definitions import*

import random
import numpy
import pygame
import time as t



class perso:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 15
        self.vely = 0
        self.right = False
        self.left = True

    def MouvementLoop(self):
        self.y += self.vely  #gerer les déplacements y
        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False

        elif keys[pygame.K_RIGHT] and self.x < 1080:
            self.x += self.vel
            self.left = False
            self.right = True

        #if keys[pygame.K_SPACE]:
            #self.vely = -20

        if self.y >= 600:              #position du perso
            self.vely = 0              #si dans le sol => remonte a 600
            if self.y > 600:           #si sur sol vely=0 car pas de gravité
                self.y = 600
        else :
            if keys[pygame.K_DOWN]:
                self.vely = min(self.vely + 10, 100)
            else:
                self.vely = min(self.vely + 3, 100)     #ajout de la gravité

    def moveup(self):
            self.vely = -20


class enemies:
    def __init__(self):
        self.vi = random.randint(20,50)
        self.height = random.randint(20,600)
        self.ang = random.randint(500,1000)
        self.size = random.randint(1,20)/10
        self.type = random.randint(1,3)
        self.x = 0.0
        self.y = 0.0
        self.t = 1.0
    def trajectory(self):
        self.x = self.vi*numpy.cos(self.ang)*self.t
        self.y = 1*(((self.t**2))/2) + self.vi* numpy.sin(self.ang) + self.height
        self.t +=1

    def Difficulty(self):
        if score > 1000 :
            self.vi = random.radint(30, 60)