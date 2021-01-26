
from definitions import*
import pygame
pygame.init()

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
    if keys[pygame.K_RIGHT] and x < 1210:
        x += vel
        perso = pygame.image.load('perso jeu droite.png')

    if y >= 600:              #position du perso
        vely = 0              #si dans le sol => remonte a 600
        if y > 600:           #si sur sol vely=0 car pas de gravité
            y = 600
    else :
        vely = min(vely + 3, 100)   #ajout de la gravité

    if keys[pygame.K_SPACE]:
        vely = -20                  #saut sir space appuyé

    window.blit(fond, (0, 0))
    window.blit(perso, (x, y))
    pygame.display.update()

pygame.quit()
