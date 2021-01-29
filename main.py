
from definitions import*
import pygame
import random

pygame.init()

JumpRight = [pygame.image.load('saut_normal_droit_1.png'), pygame.image.load('saut_normal_droit_2.png'), pygame.image.load('saut_normal_droit_3.png'), pygame.image.load('saut_normal_droit_4.png'), pygame.image.load('saut_normal_droit_5.png')]
JumpLeft = [pygame.image.load('saut_normal_gauche_1.png'), pygame.image.load('saut_normal_gauche_2.png'), pygame.image.load('saut_normal_gauche_3.png'), pygame.image.load('saut_normal_gauche_4.png'), pygame.image.load('saut_normal_gauche_5.png')]


run = True
while run:
    pygame.time.delay(27)
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False

    keys = pygame.key.get_pressed()

    y += vely  #gerer les déplacements y

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        perso = pygame.image.load('perso jeu gauche.png')
    if keys[pygame.K_RIGHT] and x < 1120:
        x += vel
        perso = pygame.image.load('perso jeu droite.png')

    

    if y >= 600:              #position du perso
        vely = 0              #si dans le sol => remonte a 600
        if y > 600:           #si sur sol vely=0 car pas de gravité
            y = 600
            

    else :
        if keys[pygame.K_DOWN]:
            vely = min(vely + 10, 100) 
        else :
            vely = min(vely + 3, 100)      #ajout de la gravité

    if keys[pygame.K_SPACE]:                #saut si espace appuyé
        vely = -20

    window.blit(fond, (0, 0))
    window.blit(perso, (x, y))
    pygame.display.update()

pygame.quit()


#trajectoire ennemie

para = random.randint(-10, 30)

if para >= -10:
    neg = 1
    if para < 0:
        neg = -1
y -= (para**2) * 0,5 * neg
para -= 1