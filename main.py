# Python Blob V2#
# description : main executable for pythonblob  project, containing all the pygame  executive code
# Authors : Vincent, Joseph,Léna

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



#music loading#
pg.mixer.init(44100, 16, 2, 4096)

#declaration
fond = pg.image.load('resources/fond.jpg')
keys = pg.key.get_pressed()
window = pg.display.set_mode((1280, 720),pg.DOUBLEBUF, 32)
pg.display.set_caption("Protect PyBlob") 
life = pg.image.load('resources/heart.png')
no_life = pg.image.load('resources/no_heart.png')
init_blob = player_entity(40, 400)
blob = init_blob
run = True
covids = []
jumpspam = 0
invulnerability = 0
slowerspawn = 0
constante = True
counter = 0
trigger = 120
#end_declaration


# Def Update (don't touch !)
def WindowUpdate(): 
    global invulnerability, trigger
    window.blit(fond,(0,0))
    for covid in covids:
        hitboxenemy = (covid.x + 15, covid.y + 15, 40, 40)
        if  pg.Rect.colliderect(pg.draw.rect(window, (0, 0, 0), blob.hitboxblob, 2), pg.draw.rect(window, (0, 0, 0), hitboxenemy, 2)) == True and invulnerability == 60:
            blob.health -= 1
            chooseSong(blob.health)
            invulnerability = 0
    window.blit(fond,(0,0))
    for covid in covids:
        window.blit(covid.sprite,(covid.x,covid.y))
        
        
    window.blit(blob.image, (blob.x, blob.y))

    if blob.health == 3:
        window.blit(life, (30, 30))
        window.blit(life, (60, 30))
        window.blit(life, (90, 30))
        blob.image = blob.actualsprites0[0]
    elif blob.health == 2:
        window.blit(life, (30, 30))
        window.blit(life, (60, 30))
        blob.image = blob.actualsprites1[0]
    elif blob.health == 1:
        window.blit(life, (30, 30))
        blob.image = blob.actualsprites2[0]
    elif blob.health <= 0: 
        window.blit(no_life, (30, 30))

    #score
    window.blit(pg.image.load('resources/score blob.png'), (1016 , 32))
    if trigger == 120:
        window.blit(blob.spritesscore[blob.score1], (1170 , 35))
        window.blit(blob.spritesscore[blob.score10], (1150 , 35))
        window.blit(blob.spritesscore[blob.score100], (1130 , 35))
        

# End def Update


while constante == True:
    constante = main_menu()
chooseSong(3)

while run == True:
    if blob.health == 0:
        counter += 1
    if counter == 180:
        counter = 0
        gameover(blob.score)
        blob.health=3
        # reset score 
    pg.time.delay(16)
    sec = t.time()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    # enemy spawn

    if len(covids) < 15 and slowerspawn == 30 and blob.health != 0:
        covids.append(ennemy())
        blob.score += 1
        slowerspawn = 0
    if slowerspawn < 30:
        slowerspawn +=1
    if blob.health == 0 :
        for covid in covids :
            covids.pop(covids.index(covid))
        
    # enemy movement and offscreen checking
    for covid in covids:
        if covid.x < 1280 and covid.x > -80 and covid.y > -740 and covid.y > -350 :
            covid.trajectory()
        else:
            covids.pop(covids.index(covid))
    if trigger < 120:
        trigger+=1
    if invulnerability < 60:
        invulnerability += 1
    blob.mouvement()
    blob.moveup()
    blob.scoreblob()
    WindowUpdate()
    print(blob.health)
    pg.display.update()
# END
