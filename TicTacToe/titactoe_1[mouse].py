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
text_font = pg.font.Font("freesansbold.ttf", 50)
S_Q_font = pg.font.SysFont('Helvetica', 50)
Title_font = pg.font.SysFont('Verdana', 100)
End_font = pg.font.SysFont('Arial', 200)

#Menu
def Menu():
    window.fill(black_color)
    start_surf = S_Q_font.render('start', True, white_color)
    start_rect = start_surf.get_rect(center=(W/2,310))
    window.blit(start_surf, start_rect)
    pg.draw.rect(window, white_color, (490, 240, 300, 140), width=10)
    quit_surf = S_Q_font.render('quit', True, white_color)
    quit_rect = quit_surf.get_rect(center=(W/2,510))
    window.blit(quit_surf, quit_rect)
    pg.draw.rect(window, white_color, (490, 440, 300, 140), width=10)
    Title_surf = Title_font.render('Tic Tac Toe', True, white_color)
    Title_rect = Title_surf.get_rect(center=(W/2,100))
    window.blit(Title_surf, Title_rect)


#End screen
def End_Screen_X():
    window.fill(black_color)
    window.fill(white_color, rect=(0,H/2,W,H))
    End_X_surf = End_font.render('X', True, white_color)
    End_rect = End_X_surf.get_rect(center=(W/2,H/4))
    window.blit(End_X_surf, End_rect)
    win_X_surf = End_font.render('WIN', True, black_color)
    win_rect = win_X_surf.get_rect(center=(W/2,(H/2+H/4)))
    window.blit(win_X_surf, win_rect)
    
def End_Screen_O():
    window.fill(white_color)
    window.fill(black_color, rect=(0,H/2,W,H))
    End_O_surf = End_font.render('O', True, black_color)
    End_rect = End_O_surf.get_rect(center=(W/2,H/4))
    window.blit(End_O_surf, End_rect)
    win_O_surf = End_font.render('WIN', True, white_color)
    win_rect = win_O_surf.get_rect(center=(W/2,(H/2+H/4)))
    window.blit(win_O_surf, win_rect)
    
def End_Screen_Draw():
    window.fill(black_color)
    End_Draw_surf = End_font.render('DRAW', True, white_color)
    End_rect = End_Draw_surf.get_rect(center=(W/2,H/2))
    window.blit(End_Draw_surf, End_rect)
    

#buttons
class Button:
    def __init__(self):
        self.B1 = pg.draw.rect(window, white_color, (490, 240, 300, 140), width=10)
        self.B2 = pg.draw.rect(window, white_color, (490, 440, 300, 140), width=10)
        self.S1 = pg.draw.rect(window, black_color, (0, 0, 240, 240), width=10)
        self.S2 = pg.draw.rect(window, black_color, (240, 0, 240, 240), width=10) 
        self.S3 = pg.draw.rect(window, black_color, (480, 0, 240, 240), width=10)
        self.S4 = pg.draw.rect(window, black_color, (0, 240, 240, 240), width=10)    
        self.S5 = pg.draw.rect(window, black_color, (240, 240, 240, 240), width=10)
        self.S6 = pg.draw.rect(window, black_color, (480, 240, 240, 240), width=10)
        self.S7 = pg.draw.rect(window, black_color, (0, 480, 240, 240), width=10)
        self.S8 = pg.draw.rect(window, black_color, (240, 480, 240, 240), width=10)
        self.S9 = pg.draw.rect(window, black_color, (480, 480, 240, 240), width=10) 
button = Button()

#tictactoe background
def tictactoe():
    window.fill(white_color)
    pg.draw.circle(window, black_color, (1000, 720/3), 90, width=10)
    pg.draw.line(window, black_color, [920, 400], [1080, 580], 10)
    pg.draw.line(window, black_color, [1080, 400], [920, 580], 10)
    pg.draw.rect(window, black_color, (0, 0, 720, 720), width=10)
    pg.draw.rect(window, black_color, (240, 0, 240, 720), width=10)
    pg.draw.rect(window, black_color, (0, 240, 720, 240), width=10)

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
     [(40,40), (200,200), (200,40), (40,200)],    #1
     [(280,40), (440,200), (440,40), (280,200)],  #2
     [(520,40), (680,200), (680,40), (520,200)],  #3
     [(40,280), (200,440), (200,280), (40,440)],  #4
     [(280,280), (440,440), (440,280),(280,440)], #5
     [(520,280), (680,440), (680,280), (520,440)],#6
     [(40,520), (200,680), (200,520), (40,680)],  #7
     [(280,520), (440,680), (440,520), (280,680)],#8
     [(520,520),(680,680), (680,520), (520,680)]] #9

def X(a, b, c, d):
    pg.draw.line(window, black_color, a, b, 10)
    pg.draw.line(window, black_color, c, d, 10)

def Playing():
    if pg.mouse.get_pressed()[0]:
            if button.S1.collidepoint(position) and used[1] == 0:
                used[1] = 1
                sleep(0.5)
                if number % 2 == 0:
                    X(x[1][0], x[1][1], x[1][2], x[1][3])
                    WIN[1] = 0    
                else:
                    Circle(O[1])
                    WIN[1] = 5
                             
            elif button.S2.collidepoint(position) and used[2] == 0:
                used[2] = 1
                sleep(0.5)
                if number % 2 == 0:
                    X(x[2][0], x[2][1], x[2][2], x[2][3])
                    WIN[2] = 0  
                else:
                    Circle(O[2])
                    WIN[2] = 5
                                        
            elif button.S3.collidepoint(position) and used[3] == 0:
                used[3] = 1
                sleep(0.5)
                if number % 2 == 0:
                    X(x[3][0], x[3][1], x[3][2], x[3][3])
                    WIN[3] = 0     
                else:
                    Circle(O[3])
                    WIN[3] = 5
            
            elif button.S4.collidepoint(position) and used[4] == 0:
                used[4] = 1
                sleep(0.5)
                if number % 2 == 0:
                    X(x[4][0], x[4][1], x[4][2], x[4][3])
                    WIN[4] = 0      
                else:
                    Circle(O[4])
                    WIN[4] = 5
         
            elif button.S5.collidepoint(position) and used[5] == 0:
                used[5] = 1
                sleep(0.5)
                if number % 2 == 0:
                    X(x[5][0], x[5][1], x[5][2], x[5][3]) 
                    WIN[5] = 0
                else:
                    Circle(O[5])
                    WIN[5] = 5
                    
            elif button.S6.collidepoint(position) and used[6] == 0:
                used[6] = 1
                sleep(0.5)
                if number % 2 == 0:
                    X(x[6][0], x[6][1], x[6][2], x[6][3]) 
                    WIN[6] = 0
                else:
                    Circle(O[6])
                    WIN[6] = 5
                    
            elif button.S7.collidepoint(position) and used[7] == 0:
                used[7] = 1
                sleep(0.5)
                if number % 2 == 0:
                    X(x[7][0], x[7][1], x[7][2], x[7][3]) 
                    WIN[7] = 0
                else:
                    Circle(O[7])
                    WIN[7] = 5
                    
            elif button.S8.collidepoint(position) and used[8] == 0:
                used[8] = 1
                sleep(0.5)
                if number % 2 == 0:
                    X(x[8][0], x[8][1], x[8][2], x[8][3]) 
                    WIN[8] = 0
                else:
                    Circle(O[8])
                    WIN[8] = 5
                    
            elif button.S9.collidepoint(position) and used[9] == 0:
                used[9] = 1
                sleep(0.5)
                if number % 2 == 0:
                    X(x[9][0], x[9][1], x[9][2], x[9][3]) 
                    WIN[9] = 0
                else:
                    Circle(O[9])
                    WIN[9] = 5
                    
    
#WIN
WIN = ['',2,2,2,
         2,2,2,
         2,2,2]
def wincon():
    #X wincon
    #row
    if WIN[1]==0 and WIN[2]==0 and WIN[3]==0: 
        End_Screen_X()
    elif WIN[4]==0 and WIN[5]==0 and WIN[6]==0:
        End_Screen_X()
    elif WIN[7]==0 and WIN[8]==0 and WIN[9]==0:
        End_Screen_X()
    #column
    elif WIN[1]==0 and WIN[4]==0 and WIN[7]==0:
        End_Screen_X()
    elif WIN[2]==0 and WIN[5]==0 and WIN[8]==0:
        End_Screen_X()
    elif WIN[3]==0 and WIN[6]==0 and WIN[9]==0:
        End_Screen_X()
    #diagonal
    elif WIN[1]==0 and WIN[5]==0 and WIN[9]==0:
        End_Screen_X()
    elif WIN[3]==0 and WIN[5]==0 and WIN[7]==0:
        End_Screen_X()
        
    #O wincon
    #row    
    if WIN[1]==5 and WIN[2]==5 and WIN[3]==5: 
        End_Screen_O()
    elif WIN[4]==5 and WIN[5]==5 and WIN[6]==5:
        End_Screen_O()
    elif WIN[7]==5 and WIN[8]==5 and WIN[9]==5:
        End_Screen_O()
    #column
    elif WIN[1]==5 and WIN[4]==5 and WIN[7]==5:
        End_Screen_O()
    elif WIN[2]==5 and WIN[5]==5 and WIN[8]==5:
        End_Screen_O()
    elif WIN[3]==5 and WIN[6]==5 and WIN[9]==5:
        End_Screen_O()
    #diagonal
    elif WIN[1]==5 and WIN[5]==5 and WIN[9]==5:
        End_Screen_O()
    elif WIN[3]==5 and WIN[5]==5 and WIN[7]==5:
        End_Screen_O()
    #Draw
    else:
        if any(i == 2 for i in WIN):
            pass
        else:
            End_Screen_Draw()
                
             
def main():
    clock = pg.time.Clock()
    global number, used
    number = 0
    used = [0,0,0,0,0,0,0,0,0,0]
    running = True
    stop = False
    
    Menu()          

    while running:
        clock.tick(30)
        global position
        position = pg.mouse.get_pos()
        print(used, WIN) 
         
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break 
            
            elif event.type == pg.MOUSEBUTTONUP:
                print(number)
                number += 1
                print('up')
                if stop == False:
                    if button.B1.collidepoint(position):
                        tictactoe()
                        used[6], WIN[6] = 0, 2
                        stop = True
                
        Playing()
         
        wincon()                                   
        pg.display.update()    

main()       
pg.quit()