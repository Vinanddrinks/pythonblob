import pygame

window = pygame.display.set_mode((1280, 700))
pygame.display.set_caption("Protect little Bud")

# pour le perso
x = 50
y = 400
width = 136
height = 96
vel = 15 #vitesse
vely = 0 #gravité

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
right = False

WalkCount = 0

fond = pygame.image.load('fond.jpg')
perso = pygame.image.load('perso jeu droite.png')
mechant = pygame.image.load('BouleCovid1.0.png')
JumpRight = [pygame.image.load('saut_normal_droit_1.png'), pygame.image.load('saut_normal_droit_2.png'), pygame.image.load('saut_normal_droit_3.png'), pygame.image.load('saut_normal_droit_4.png'), pygame.image.load('saut_normal_droit_5.png')]