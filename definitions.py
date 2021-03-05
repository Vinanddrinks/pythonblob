import pygame
import random
import numpy

window = pygame.display.set_mode((1280, 700))
pygame.display.set_caption("Protect little Bud")

# pour le perso
x = 50
y = 400
width = 136
height = 96
vel = 15 #vitesse
vely = 0 #gravité

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
         


        


# Pour les images
left = False
right = False

WalkCount = 0

fond = pygame.image.load('fond.jpg')
perso = pygame.image.load('perso jeu droite.png')
mechant = pygame.image.load('BouleCovid1.0.png')
JumpRight = [pygame.image.load('saut_normal_droit_1.png'), pygame.image.load('saut_normal_droit_2.png'), pygame.image.load('saut_normal_droit_3.png'), pygame.image.load('saut_normal_droit_4.png'), pygame.image.load('saut_normal_droit_5.png')]