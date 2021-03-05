
from definitions import*
from classes import*

import pygame
import random
import time as t

pygame.init()
score = 0
ScoreLat = 0

font = pygame.font.SysFont('comicsans', 60, True)
fond = pygame.image.load('fond.jpg')
imageperso = pygame.image.load('perso jeu droite.png')
mechant = pygame.image.load('BouleCovid1.0.png')


def WindowRedraw():
    window.blit(fond, (0, 0))
    text = font.render('Score : ' + str(score), 1, (0, 0, 0))
    window.blit(text, (20, 20))
    window.blit(imageperso, (bud.x, bud.y))
    #window.blit(mechant, (moove, 600))
    pygame.display.update()

def ScoreClock():
    global ScoreLat
    global score
    if t.time()-ScoreLat >= 0.1: 
        ScoreLat = t.time()
        score += 1

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

class enemy():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = vel
        self.vely = vely
         
run = True
para = random.randint(-10, 30)
bud = perso(50, 400)

def MooveEnnemy(para):

    moove = para**2 + para
    window.blit(mechant, (moove, 600))
    

while run:
    pygame.time.delay(27)
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False

    MooveEnnemy(para)

    bud.MouvementLoop()
    if bud.left:
        imageperso = pygame.image.load('perso jeu gauche.png')

    elif bud.right:
        imageperso = pygame.image.load('perso jeu droite.png')


    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        bud.moveup()
    
    ScoreClock()
    WindowRedraw()

pygame.quit()

