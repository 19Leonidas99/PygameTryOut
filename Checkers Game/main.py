import pygame as pg 
from checkers.constants import *

pg.init()
pg.display.set_caption('Checkers')
Display = pg.display.set_mode(SIZE)


def main():
    run = True
    clock = pg.time.Clock()
    
    while run:
        clock.tick(60)
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                run = False
            
            if ev.type == pg.MOUSEBUTTONDOWN:
                pass
                
        pg.display.update()
        
    pygame.quit()
        
main()