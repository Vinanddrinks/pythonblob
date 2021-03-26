# Python Blob V2#
# description : main executable for pythonblob  project, containing all the pygame  executive code
# Authors : Vincent, Joseph

#importation
import pygame as pg 
import numpy
import time as t
#end-importation


# BEGIN
pg.init()
#declaration
fond = pg.image.load('fond.jpg')
window = pg.display.set_mode((1280, 720))
pg.display.set_caption("Protect PyBlob")
run = True
#end_declaration
while run == True:
    for event in pg.event.get():
       if event.type == pg.QUIT:
           run = False
    window.blit(fond,(0,0))
    pg.time.delay(60)
    pg.display.update()
pg.quit()
# END
