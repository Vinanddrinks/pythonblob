import pygame

window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Jeux Test")

# pour le perso
x = 50
y = 600
width = 136
height = 96
vel = 15 #vitesse
vely = 0 #gravité

i=0

class enemy(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.vel = vel
        self.vely = vely

# Pour les images
left = False
right = True

WalkCount = 0

fond = pygame.image.load('fond.jpg')
perso = pygame.image.load('perso jeu droite.png')
mechant = pygame.image.load('BouleCovid1.0.png')