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

#music loading#
pg.mixer.init()
pg.mixer.music.load('musiques/Dungeonboss.wav')
pg.mixer.music.load('musiques/Maze.wav')
pg.mixer.music.load('musiques/Nightshade.ogg')
pg.mixer.music.load('musiques/Powerup.ogg')
pg.mixer.music.load('musiques/Underclocked.wav')
pg.mixer.music.load('musiques/Virtualboy.wav')

#declaration
fond = pg.image.load('resources/fond.jpg')
keys = pg.key.get_pressed()
window = pg.display.set_mode((1280, 720),pg.DOUBLEBUF, 32)
pg.display.set_caption("Protect PyBlob") 
life = pg.image.load('resources/heart.png')
no_life = pg.image.load('resources/no_heart.png')
blob = player_entity(40, 400)
run = True
covids = []
jumpspam = 0
invulnerability = 0
slowerspawn = 0
#end_declaration

# Def Update (don't touch !)
def WindowUpdate(): 
    global invulnerability
    window.blit(fond,(0,0))
    for covid in covids:
        hitboxenemy = (covid.x + 15, covid.y + 15, 40, 40)
        if  pg.Rect.colliderect(pg.draw.rect(window, (0, 0, 0), blob.hitboxblob, 2), pg.draw.rect(window, (0, 0, 0), hitboxenemy, 2)) == True and invulnerability == 60:
            blob.health -= 1
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
    window.blit(blob.spritesscore[blob.score1], (1170 , 35))
    window.blit(blob.spritesscore[blob.score10], (1150 , 35))
    window.blit(blob.spritesscore[blob.score100], (1130 , 35))
        

# End def Update

while run == True:
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
    
    if invulnerability < 60:
        invulnerability += 1

    #music play#
    pg.mixer.music.play('musiques/Dungeonboss.wav')

    blob.mouvement()
    blob.moveup()
    blob.scoreblob()

    #print('blob x :',blob.x,' blob y:',blob.y)

    #print('enemy x :', testcovid.x, 'enemy y :', testcovid.y )
    WindowUpdate()
    pg.display.update()
    #print(blob.health)
    #print(invulnerability)
    

pg.quit()
# END
