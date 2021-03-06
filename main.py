
from definitions import*
from classes import*

import pygame
import random
import time as t

pygame.init()
score = 0
ScoreLat = 0
evil = enemies()
font = pygame.font.SysFont('comicsans', 60, True)
fond = pygame.image.load('fond.jpg')
imageperso = pygame.image.load('perso jeu droite.png')
mechant = pygame.image.load('BouleCovid1.0.png')


         
run = True
para = random.randint(-10, 30)
bud = perso(50, 400)

    

while run:
    pygame.time.delay(60)
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False

    evil.trajectory()

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

