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
score = 0
fond = pg.image.load('resources/fond.jpg')
font = pg.font.SysFont('comicsans', 50, True)
text = font.render('Score : ' + str(score), 1, (0, 0, 255))
keys = pg.key.get_pressed()
window = pg.display.set_mode((1280, 720))
pg.display.set_caption("Protect PyBlob") 

life = pg.image.load('resources/heart.png')
no_life = pg.image.load('resources/no_heart.png')

blob = player_entity(40, 400)
run = True
testcovid = ennemy()
jumpspam = 0
#end_declaration

# Def Update (don't touch !)
def WindowUpdate():
    window.blit(fond,(0,0))
    window.blit(testcovid.sprite,(testcovid.x,testcovid.y))
    window.blit(blob.image, (blob.x, blob.y))
    window.blit(text, (1070, 30) )
    if blob.health == 3:
        window.blit(life, (30, 30))
        window.blit(life, (60, 30))
        window.blit(life, (90, 30))
    elif blob.health == 2:
        window.blit(life, (30, 30))
        window.blit(life, (60, 30))
    elif blob.health == 1:
        window.blit(life, (30, 30))
    else :
        window.blit(no_life, (30, 30))

# End def Update
    

while run == True:
    pg.time.delay(16)
    sec = t.time()
    for event in pg.event.get():
       if event.type == pg.QUIT:
           run = False
    
    blob.mouvement()
    blob.moveup()

    testcovid.trajectory()
    print('blob x :',blob.x,' blob y:',blob.y)
    #print('enemy x :', testcovid.x, 'enemy y :', testcovid.y )
    WindowUpdate()
    pg.display.update()
    print(blob.health)
    

pg.quit()
# END

