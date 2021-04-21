# Python Blob V2#
# description : main executable for pythonblob  project, containing all the pygame  executive code
# Authors : Vincent, Joseph.

#importation
import pygame as pg 
from numpy import *
import time as t
from Classes import *
#end-importation


# BEGIN
#pygame initialisation
pg.init()
clock = pg.time.Clock()
#end pg initialisation
#declaration
fond = pg.image.load('fond.jpg')
#font = pg.font.SysFont('comicsans', 30, True)
#text = font.render('Score : ', score, 1, (0, 0, 0))
keys = pg.key.get_pressed()
window = pg.display.set_mode((1280, 720))
pg.display.set_caption("Protect PyBlob") 
imageperso = pg.image.load('perso jeu droite.png')
blob = player_entity(40, 400)
run = True
score = 0
testcovid = ennemy()
#end_declaration


while run == True:
    pg.time.delay(16)
    for event in pg.event.get():
       if event.type == pg.QUIT:
           run = False
    
    blob.mouvement()
    blob.moveup()
    testcovid.trajectory()
    print('blob x :',blob.x,' blob y:',blob.y)
    window.blit(fond,(0,0))
    window.blit(testcovid.sprite,(testcovid.x,testcovid.y))
    window.blit(imageperso, (blob.x, blob.y))
    pg.display.update()
pg.quit()
# END
