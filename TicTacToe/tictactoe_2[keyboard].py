import pygame as pg
from time import sleep
#pg base setup
pg.init()
W, H = 720 ,720 
pg.display.set_caption("TicTacToe")
Display = pg.display.set_mode((W, H ))

#colors in use
black_color = (0, 0, 0)
white_color = (255,255,255)
FONT = pg.font.Font("freesansbold.ttf", 50)

#Board
W1, H1 = 0, 0
W2, H2 = 240, 240
W3, H3 = 480, 480   
class Board:
    def __init__(self):
        self.S1 = pg.draw.rect(Display, black_color, (W1, H1, 240, 240), width=10)
        self.S2 = pg.draw.rect(Display, black_color, (W2, H1, 240, 240), width=10) 
        self.S3 = pg.draw.rect(Display, black_color, (W3, H1, 240, 240), width=10)
        self.S4 = pg.draw.rect(Display, black_color, (W1, H2, 240, 240), width=10)    
        self.S5 = pg.draw.rect(Display, black_color, (W2, H2, 240, 240), width=10)
        self.S6 = pg.draw.rect(Display, black_color, (W3, H2, 240, 240), width=10)
        self.S7 = pg.draw.rect(Display, black_color, (W1, H3, 240, 240), width=10)
        self.S8 = pg.draw.rect(Display, black_color, (W2, H3, 240, 240), width=10)
        self.S9 = pg.draw.rect(Display, black_color, (W3, H3, 240, 240), width=10) 
          

#Another variation to play the game
n = ['1','2','3','4','5','6','7','8','9']
def Play():
    Board()
    text_surf1 = FONT.render(n[0], True, black_color)
    text_rect1 = text_surf1.get_rect(center=(120,120))
    Display.blit(text_surf1, text_rect1)
    text_surf2 = FONT.render(n[1], True, black_color)
    text_rect2 = text_surf1.get_rect(center=(360,120))
    Display.blit(text_surf2, text_rect2)
    text_surf3 = FONT.render(n[2], True, black_color)
    text_rect3 = text_surf3.get_rect(center=(600,120))
    Display.blit(text_surf3, text_rect3)
    text_surf4 = FONT.render(n[3], True, black_color)
    text_rect4 = text_surf4.get_rect(center=(120,360))
    Display.blit(text_surf4, text_rect4)
    text_surf5 = FONT.render(n[4], True, black_color)
    text_rect5 = text_surf5.get_rect(center=(360,360))
    Display.blit(text_surf5, text_rect5)
    text_surf6 = FONT.render(n[5], True, black_color)
    text_rect6 = text_surf6.get_rect(center=(600,360))
    Display.blit(text_surf6, text_rect6)
    text_surf7 = FONT.render(n[6], True, black_color)
    text_rect7 = text_surf7.get_rect(center=(120,600))
    Display.blit(text_surf7, text_rect7)
    text_surf8 = FONT.render(n[7], True, black_color)
    text_rect8 = text_surf8.get_rect(center=(360,600))
    Display.blit(text_surf8, text_rect8)
    text_surf9 = FONT.render(n[8], True, black_color)
    text_rect9 = text_surf9.get_rect(center=(600,600))
    Display.blit(text_surf9, text_rect9)

   
def main():
    clock = pg.time.Clock()
    number = 0
    running = True
    Display.fill(white_color) 
    
    while running:
        clock.tick(60)
        Play()
        pg.display.update()
        print(n)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break
        
        
        keys = pg.key.get_pressed()
        pg.key.set_repeat(10000)
        if keys[pg.K_1] or keys[pg.K_KP1]:
            sleep(1)
            if number % 2 == 0:
                n[0] = 'X'
                number += 1
            else:
                n[0] = 'O' 
                number += 1
                
        elif keys[pg.K_2] or keys[pg.K_KP2]:
            sleep(1)
            if number % 2 == 0:
                n[1] = 'X'
                number += 1
            else:
                n[1] = 'O'
                number += 1
                
        elif keys[pg.K_3] or keys[pg.K_KP3]:
            sleep(1)
            if number % 2 == 0:
                n[2] = 'X'
                number += 1
            else:
                n[2] = 'O'
                number += 1 
                
        elif keys[pg.K_4] or keys[pg.K_KP4]:
            sleep(1)
            if number % 2 == 0:
                n[3] = 'X'
                number += 1
            else:
                n[3] = 'O'
                number += 1
                
        elif keys[pg.K_5] or keys[pg.K_KP5]:
            sleep(1)
            if number % 2 == 0:
                n[4] = 'X'
                number += 1
            else:
                n[4] = 'O'
                number += 1
                
        elif keys[pg.K_6] or keys[pg.K_KP6]:
            sleep(1)
            if number % 2 == 0:
                n[5] = 'X'
                number += 1
            else:
                n[5] = 'O'
                number += 1
                
        elif keys[pg.K_7] or keys[pg.K_KP7]:
            sleep(1)
            if number % 2 == 0:
                n[6] = 'X'
                number += 1
            else:
                n[6] = 'O'
                number += 1
                
        elif keys[pg.K_8] or keys[pg.K_KP8]:
            sleep(1)
            if number % 2 == 0:
                n[7] = 'X'
                number += 1
            else:
                n[7] = 'O'
                number += 1
                
        elif keys[pg.K_9] or keys[pg.K_KP9]:
            sleep(1)
            if number % 2 == 0:
                n[8] = 'X'
                number += 1
            else:
                n[8] = 'O'
                number += 1
        
        pg.display.update()    

main()       
pg.quit()