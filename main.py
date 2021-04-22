# Python Blob V2#
# description : main executable for pythonblob  project, containing all the pygame  executive code
# Authors : Vincent, Joseph.

#importation
import pygame as pg 
from numpy import *
import time as t
from Classes import *
from functions import *
#end-importation


# BEGIN

#pygame initialisation
pg.init()
clock = pg.time.Clock()
#end pg initialisation


#declaration
fond = pg.image.load('resources/fond.jpg')
font = pg.font.SysFont('comicsans', 50, True)
Markscore = font.render('Score : ' + str(score), 1, (0, 0, 255))
keys = pg.key.get_pressed()
window = pg.display.set_mode((1280, 720))
pg.display.set_caption("Protect PyBlob") 
imageperso = pg.image.load('resources/saut_normal_droit_0.png')
blob = player_entity(40, 400)
run = True
testcovid = ennemy()
#end_declaration

# Def Update (don't touch !)
def WindowUpdate():
    window.blit(fond,(0,0))
    window.blit(testcovid.sprite,(testcovid.x,testcovid.y))
    window.blit(imageperso, (blob.x, blob.y))
    window.blit(Markscore, (30, 30) )
# End def Update


while run == True:
    pg.time.delay(16)
    for event in pg.event.get():
       if event.type == pg.QUIT:
           run = False
    
    blob.mouvement()
    blob.moveup()
    testcovid.trajectory()
    print('blob x :',blob.x,' blob y:',blob.y)
    SpreadTime()
    print(score)
    WindowUpdate()
    pg.display.update()
    

pg.quit()
# END

