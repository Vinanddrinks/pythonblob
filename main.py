
from definitions import*
from classes import*

import pygame
import random
import time as t

pygame.init()
score = 0
ScoreLat = 0
def ScoreClock():
    global ScoreLat
    global score
    if t.time()-ScoreLat >= 0.1: 
        ScoreLat = t.time()
        score += 1
        print(score)


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
            self.vely = min(self.vely + 3, 100)      #ajout de la gravité

    def moveup(self):
            self.vely = -20


run = True

bud = perso(50, 400)
imageperso = pygame.image.load('perso jeu droite.png')


while run:
    pygame.time.delay(27)
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False

    bud.MouvementLoop()
    if bud.left:
        imageperso = pygame.image.load('perso jeu gauche.png')

    elif bud.right:
        imageperso = pygame.image.load('perso jeu droite.png')


    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        bud.moveup()

    ScoreClock()

    window.blit(fond, (0, 0))
    window.blit(imageperso, (bud.x, bud.y))
    pygame.display.update()

pygame.quit()


#trajectoire ennemie

#para = random.randint(-10, 30)

#if para >= -10:
#    neg = 1
#    if para < 0:
#        neg = -1
#y -= (para**2) * 0,5 * neg
#para -= 1