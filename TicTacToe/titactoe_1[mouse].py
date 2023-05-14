import pygame as pg
from time import sleep
#pg base setup
pg.init()
W, H = 1280 ,720 
pg.display.set_caption("TicTacToe")
window = pg.display.set_mode((W, H ))

#colors in use
black_color = (0, 0, 0)
white_color = (255,255,255)
FONT = pg.font.Font("freesansbold.ttf", 50)

#tictactoe
def tictactoe():
    window.fill(white_color)
    pg.draw.circle(window, black_color, (1000, 720/3), 90, width=10)
    pg.draw.line(window, black_color, [920, 400], [1080, 580], 10)
    pg.draw.line(window, black_color, [1080, 400], [920, 580], 10)
    Board()

#Board
W1, H1 = 0, 0
W2, H2 = 240, 240
W3, H3 = 480, 480   
class Board:
    def __init__(self):
        self.S1 = pg.draw.rect(window, black_color, (W1, H1, 240, 240), width=10)
        self.S2 = pg.draw.rect(window, black_color, (W2, H1, 240, 240), width=10) 
        self.S3 = pg.draw.rect(window, black_color, (W3, H1, 240, 240), width=10)
        self.S4 = pg.draw.rect(window, black_color, (W1, H2, 240, 240), width=10)    
        self.S5 = pg.draw.rect(window, black_color, (W2, H2, 240, 240), width=10)
        self.S6 = pg.draw.rect(window, black_color, (W3, H2, 240, 240), width=10)
        self.S7 = pg.draw.rect(window, black_color, (W1, H3, 240, 240), width=10)
        self.S8 = pg.draw.rect(window, black_color, (W2, H3, 240, 240), width=10)
        self.S9 = pg.draw.rect(window, black_color, (W3, H3, 240, 240), width=10) 
          
board = Board()

#TicTacToe O
O = [[],
     (120,120), #1
     (360,120), #2
     (600,120), #3
     (120,360), #4
     (360,360), #5
     (600,360), #6
     (120,600), #7
     (360,600), #8
     (600,600)]  #9
     
def Circle(e):
    pg.draw.circle(window, black_color, e, 50, 10)

#TicTacToe X
x = [[],
     [(0,0), (240,240), (240,0), (0,240)],        #1
     [(240,0), (480,240), (480,0), (240,240)],    #2
     [(480,0), (720,240), (720,0), (480,240)],    #3
     [(0,240), (240,480), (240,240), (0,480)],    #4
     [(240,240), (480,480), (480,240),(240,480)], #5
     [(480,240), (720,480), (720,240), (480,480)],#6
     [(0,480), (240,720), (240,480), (0,720)],    #7
     [(240,480), (480,720), (480,480), (240,720)],#8
     [(480,480),(720,720), (720,480), (480,720)]] #9

def X(a, b, c, d):
    pg.draw.line(window, black_color, a, b, 10)
    pg.draw.line(window, black_color, c, d, 10)
#WIN
WIN = [2,2,2,2,
         2,2,2,
         2,2,2]
def wincon():
    #X wincon
    if WIN[1]==0 and WIN[2]==0 and WIN[3]==0: 
        text_surf9 = FONT.render('X Win', True, black_color)
        text_rect9 = text_surf9.get_rect(center=(1000,100))
        window.blit(text_surf9, text_rect9)
    elif WIN[4]==0 and WIN[5]==0 and WIN[6]==0:
        text_surf9 = FONT.render('X Win', True, black_color)
        text_rect9 = text_surf9.get_rect(center=(1000,100))
        window.blit(text_surf9, text_rect9)
    elif WIN[7]==0 and WIN[8]==0 and WIN[9]==0:
        text_surf9 = FONT.render('X Win', True, black_color)
        text_rect9 = text_surf9.get_rect(center=(1000,100))
        window.blit(text_surf9, text_rect9)
    elif WIN[1]==0 and WIN[4]==0 and WIN[7]==0:
        text_surf9 = FONT.render('X Win', True, black_color)
        text_rect9 = text_surf9.get_rect(center=(1000,100))
        window.blit(text_surf9, text_rect9)
    elif WIN[2]==0 and WIN[5]==0 and WIN[8]==0:
        text_surf9 = FONT.render('X Win', True, black_color)
        text_rect9 = text_surf9.get_rect(center=(1000,100))
        window.blit(text_surf9, text_rect9)
    elif WIN[3]==0 and WIN[6]==0 and WIN[9]==0:
        text_surf9 = FONT.render('X Win', True, black_color)
        text_rect9 = text_surf9.get_rect(center=(1000,100))
        window.blit(text_surf9, text_rect9)
    elif WIN[1]==0 and WIN[5]==0 and WIN[9]==0:
        text_surf9 = FONT.render('X Win', True, black_color)
        text_rect9 = text_surf9.get_rect(center=(1000,100))
        window.blit(text_surf9, text_rect9)
    elif WIN[3]==0 and WIN[5]==0 and WIN[7]==0:
        text_surf9 = FONT.render('X Win', True, black_color)
        text_rect9 = text_surf9.get_rect(center=(1000,100))
        window.blit(text_surf9, text_rect9)
    #O wincon    
    elif WIN[1]==1 and WIN[2]==1 and WIN[3]==1: 
        text_surf9 = FONT.render('O Win', True, black_color)
        text_rect9 = text_surf9.get_rect(center=(1000,700))
        window.blit(text_surf9, text_rect9)
    elif WIN[4]==1 and WIN[5]==1 and WIN[6]==1:
        text_surf9 = FONT.render('O Win', True, black_color)
        text_rect9 = text_surf9.get_rect(center=(1000,700))
        window.blit(text_surf9, text_rect9)
    elif WIN[7]==1 and WIN[8]==1 and WIN[9]==1:
        text_surf9 = FONT.render('O Win', True, black_color)
        text_rect9 = text_surf9.get_rect(center=(1000,700))
        window.blit(text_surf9, text_rect9)
    elif WIN[1]==1 and WIN[4]==1 and WIN[7]==1:
        text_surf9 = FONT.render('O Win', True, black_color)
        text_rect9 = text_surf9.get_rect(center=(1000,700))
        window.blit(text_surf9, text_rect9)
    elif WIN[2]==1 and WIN[5]==1 and WIN[8]==1:
        text_surf9 = FONT.render('O Win', True, black_color)
        text_rect9 = text_surf9.get_rect(center=(1000,700))
        window.blit(text_surf9, text_rect9)
    elif WIN[3]==1 and WIN[6]==1 and WIN[9]==1:
        text_surf9 = FONT.render('O Win', True, black_color)
        text_rect9 = text_surf9.get_rect(center=(1000,700))
        window.blit(text_surf9, text_rect9)
    elif WIN[1]==1 and WIN[5]==1 and WIN[9]==1:
        text_surf9 = FONT.render('O Win', True, black_color)
        text_rect9 = text_surf9.get_rect(center=(1000,700))
        window.blit(text_surf9, text_rect9)
    elif WIN[3]==1 and WIN[5]==1 and WIN[7]==1:
        text_surf9 = FONT.render('O Win', True, black_color)
        text_rect9 = text_surf9.get_rect(center=(1000,700))
        window.blit(text_surf9, text_rect9)
    #Draw
    else:
        print('DRAW')
        
        
def main():
    clock = pg.time.Clock()
    number = 0
    running = True
    
    tictactoe()
    while running:
        print(WIN)
        clock.tick(30)
        print(number)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break 
        
        position = pg.mouse.get_pos()
        if pg.mouse.get_pressed()[0]:
            if board.S1.collidepoint(position):
                sleep(0.5)
                if number % 2 == 0:
                    X(x[1][0], x[1][1], x[1][2], x[1][3])
                    WIN[1] = 0
                    number += 1 
                else:
                    Circle(O[1])
                    WIN[1] = 1
                    number += 1
                    
            elif board.S2.collidepoint(position):
                sleep(0.5)
                if number % 2 == 0:
                    X(x[2][0], x[2][1], x[2][2], x[2][3])
                    WIN[2] = 0
                    number += 1  
                else:
                    Circle(O[2])
                    WIN[2] = 1
                    number += 1 
                    
            elif board.S3.collidepoint(position):
                sleep(0.5)
                if number % 2 == 0:
                    X(x[3][0], x[3][1], x[3][2], x[3][3])
                    WIN[3] = 0
                    number += 1  
                else:
                    Circle(O[3])
                    WIN[3] = 1
                    number += 1 
            
            elif board.S4.collidepoint(position):
                sleep(0.5)
                if number % 2 == 0:
                    X(x[4][0], x[4][1], x[4][2], x[4][3])
                    WIN[4] = 0
                    number += 1  
                else:
                    Circle(O[4])
                    WIN[4] = 1
                    number += 1 
                    
            elif board.S5.collidepoint(position):
                sleep(0.5)
                if number % 2 == 0:
                    X(x[5][0], x[5][1], x[5][2], x[5][3]) 
                    WIN[5] = 0
                    number += 1 
                else:
                    Circle(O[5])
                    WIN[5] = 1
                    number += 1 
                    
            elif board.S6.collidepoint(position):
                sleep(0.5)
                if number % 2 == 0:
                    X(x[6][0], x[6][1], x[6][2], x[6][3]) 
                    WIN[6] = 0
                    number += 1 
                else:
                    Circle(O[6])
                    WIN[6] = 1
                    number += 1 
                    
            elif board.S7.collidepoint(position):
                sleep(0.5)
                if number % 2 == 0:
                    X(x[7][0], x[7][1], x[7][2], x[7][3]) 
                    WIN[7] = 0
                    number += 1 
                else:
                    Circle(O[7])
                    WIN[7] = 1
                    number += 1 
                    
            elif board.S8.collidepoint(position):
                sleep(0.5)
                if number % 2 == 0:
                    X(x[8][0], x[8][1], x[8][2], x[8][3]) 
                    WIN[8] = 0
                    number += 1 
                else:
                    Circle(O[8])
                    WIN[8] = 1
                    number += 1 
                    
            elif board.S9.collidepoint(position):
                sleep(0.5)
                if number % 2 == 0:
                    X(x[9][0], x[9][1], x[9][2], x[9][3]) 
                    WIN[9] = 0
                    number += 1 
                else:
                    Circle(O[9])
                    WIN[9] = 1
                    number += 1 
            wincon()                                   
        pg.display.update()    

main()       
pg.quit()