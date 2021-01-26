import pygame

window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Jeux Test")

# pour le perso
x = 50
y = 400
width = 136
height = 96
vel = 15 #vitesse
vely = 0 #gravité

# Pour les jump
Jump = False
JumpCount = 10

# Pour les images
left = False
right = True
WalkCount = 0

fond = pygame.image.load('fond.jpg')
perso = pygame.image.load('perso jeu droite.png')