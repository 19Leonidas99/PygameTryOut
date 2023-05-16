import pygame as pg
from time import sleep

#pg base setup
pg.init()
Size = Width, Height = 1280 ,720 
pg.display.set_caption("TicTacToe")
window = pg.display.set_mode((Size))

#colors and font in use
black_color = (0, 0, 0)
white_color = (255,255,255)
text_font = pg.font.Font("freesansbold.ttf", 50)
S_Q_font = pg.font.SysFont('Helvetica', 50)
Title_font = pg.font.SysFont('Verdana', 100)
End_font = pg.font.SysFont('Arial', 200)

#Background
class Screens:
#menu Screen
    def Menu_bg():
        window.fill(black_color)
        Title_surf = Title_font.render('Tic Tac Toe', True, white_color)
        Title_rect = Title_surf.get_rect(center=(Width/2,100))
        window.blit(Title_surf, Title_rect)
        start_surf = S_Q_font.render('Start', True, white_color)
        start_rect = start_surf.get_rect(center=(Width/2,310))
        window.blit(start_surf, start_rect)
        pg.draw.rect(window, white_color, (490, 240, 300, 140), width=10)
        quit_surf = S_Q_font.render('Quit', True, white_color)
        quit_rect = quit_surf.get_rect(center=(Width/2,510))
        window.blit(quit_surf, quit_rect)

#Game screen
    def tictactoe():
        window.fill(white_color)
        pg.draw.circle(window, black_color, (1000, 720/3), 90, width=10)
        pg.draw.line(window, black_color, [920, 400], [1080, 580], 10)
        pg.draw.line(window, black_color, [1080, 400], [920, 580], 10)
        pg.draw.rect(window, black_color, (0, 0, 720, 720), width=10)
        pg.draw.rect(window, black_color, (240, 0, 240, 720), width=10)
        pg.draw.rect(window, black_color, (0, 240, 720, 240), width=10)
        
#End screen X win
    def End_Screen_X():
        window.fill(white_color)
        window.fill(black_color, rect=(0,Height/2,Width,Height))
        End_X_surf = End_font.render('X', True, black_color)
        End_rect = End_X_surf.get_rect(center=(Width/2,Height/4))
        window.blit(End_X_surf, End_rect)
        win_X_surf = End_font.render('WIN', True, white_color)
        win_rect = win_X_surf.get_rect(center=(Width/2,(Height/2+Height/4)))
        window.blit(win_X_surf, win_rect)
        Button.Reset_button_img(1160)
        
#End screen O win
    def End_Screen_O():
        window.fill(white_color)
        window.fill(black_color, rect=(0,Height/2,Width,Height))
        End_O_surf = End_font.render('O', True, black_color)
        End_rect = End_O_surf.get_rect(center=(Width/2,Height/4))
        window.blit(End_O_surf, End_rect)
        win_O_surf = End_font.render('WIN', True, white_color)
        win_rect = win_O_surf.get_rect(center=(Width/2,(Height/2+Height/4)))
        window.blit(win_O_surf, win_rect)
        Button.Reset_button_img(1160)

#End screen Draw
    def End_Screen_Draw():
        window.fill(white_color)
        End_Draw_surf = End_font.render('DRAW', True, black_color)
        End_rect = End_Draw_surf.get_rect(center=(Width/2,Height/2))
        window.blit(End_Draw_surf, End_rect)
        Button.Reset_button_img(1160)
class Button:
    def __init__(self):
        self.Start_B1 = pg.draw.rect(window, white_color, (490, 240, 300, 140), width=10)
        self.Quit_B2 = pg.draw.rect(window, white_color, (490, 440, 300, 140), width=10)
        self.Reset_B3 = pg.draw.rect(window, white_color, (1160, 0, 100, 100), width=10)
        self.S1 = pg.draw.rect(window, black_color, (0, 0, 240, 240), width=10)
        self.S2 = pg.draw.rect(window, black_color, (240, 0, 240, 240), width=10) 
        self.S3 = pg.draw.rect(window, black_color, (480, 0, 240, 240), width=10)
        self.S4 = pg.draw.rect(window, black_color, (0, 240, 240, 240), width=10)    
        self.S5 = pg.draw.rect(window, black_color, (240, 240, 240, 240), width=10)
        self.S6 = pg.draw.rect(window, black_color, (480, 240, 240, 240), width=10)
        self.S7 = pg.draw.rect(window, black_color, (0, 480, 240, 240), width=10)
        self.S8 = pg.draw.rect(window, black_color, (240, 480, 240, 240), width=10)
        self.S9 = pg.draw.rect(window, black_color, (480, 480, 240, 240), width=10) 

    def Reset_button_img(x):
        Reset_img = pg.image.load('TicTacToe/reset_img.png')
        Reset_img_resize = pg.transform.scale(Reset_img, (120,100))
        window.blit(Reset_img_resize, (x, 0))    
    
class Draw:
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

    O = [(),
        (120,120), #1
        (360,120), #2
        (600,120), #3
        (120,360), #4
        (360,360), #5
        (600,360), #6
        (120,600), #7
        (360,600), #8
        (600,600)] #9
    
    def X(a):
        pg.draw.line(window, black_color, Draw.x[a][0], Draw.x[a][1], 10)
        pg.draw.line(window, black_color, Draw.x[a][2], Draw.x[a][3], 10)
           
    def Circle(e):
        pg.draw.circle(window, black_color, Draw.O[e], 50, 10)
        

class Playing:
    def play():
        if button.S1.collidepoint(position) and used[1] == 0:
            used[1] = 1
            if number % 2 == 0:
                Draw.X(1)
                WIN_check[1] = 0    
            else:
                Draw.Circle(1)
                WIN_check[1] = 5
                    
        elif button.S2.collidepoint(position) and used[2] == 0:
            used[2] = 1
            if number % 2 == 0:
                Draw.X(2)
                WIN_check[2] = 0  
            else:
                Draw.Circle(2)
                WIN_check[2] = 5
                                    
        elif button.S3.collidepoint(position) and used[3] == 0:
            used[3] = 1
            if number % 2 == 0:
                Draw.X(3)
                WIN_check[3] = 0     
            else:
                Draw.Circle(3)
                WIN_check[3] = 5
        
        elif button.S4.collidepoint(position) and used[4] == 0:
            used[4] = 1
            if number % 2 == 0:
                Draw.X(4)
                WIN_check[4] = 0      
            else:
                Draw.Circle(4)
                WIN_check[4] = 5
        
        elif button.S5.collidepoint(position) and used[5] == 0:
            used[5] = 1
            if number % 2 == 0:
                Draw.X(5) 
                WIN_check[5] = 0
            else:
                Draw.Circle(5)
                WIN_check[5] = 5
                
        elif button.S6.collidepoint(position) and used[6] == 0:
            used[6] = 1
            if number % 2 == 0:
                Draw.X(6) 
                WIN_check[6] = 0
            else:
                Draw.Circle(6)
                WIN_check[6] = 5
                
        elif button.S7.collidepoint(position) and used[7] == 0:
            used[7] = 1
            if number % 2 == 0:
                Draw.X(7) 
                WIN_check[7] = 0
            else:
                Draw.Circle(7)
                WIN_check[7] = 5
                
        elif button.S8.collidepoint(position) and used[8] == 0:
            used[8] = 1
            if number % 2 == 0:
                Draw.X(8) 
                WIN_check[8] = 0
            else:
                Draw.Circle(8)
                WIN_check[8] = 5
                
        elif button.S9.collidepoint(position) and used[9] == 0:
            used[9] = 1
            if number % 2 == 0:
                Draw.X(9) 
                WIN_check[9] = 0
            else:
                Draw.Circle(9)
                WIN_check[9] = 5
                
    def wincon():
        #X wincon
        #row
        if WIN_check[1]==0 and WIN_check[2]==0 and WIN_check[3]==0: 
            Screens.End_Screen_X()
        elif WIN_check[4]==0 and WIN_check[5]==0 and WIN_check[6]==0:
            Screens.End_Screen_X()
        elif WIN_check[7]==0 and WIN_check[8]==0 and WIN_check[9]==0:
            Screens.End_Screen_X()
        #column
        elif WIN_check[1]==0 and WIN_check[4]==0 and WIN_check[7]==0:
            Screens.End_Screen_X()
        elif WIN_check[2]==0 and WIN_check[5]==0 and WIN_check[8]==0:
            Screens.End_Screen_X()
        elif WIN_check[3]==0 and WIN_check[6]==0 and WIN_check[9]==0:
            Screens.End_Screen_X()
        #diagonal
        elif WIN_check[1]==0 and WIN_check[5]==0 and WIN_check[9]==0:
            Screens.End_Screen_X()
        elif WIN_check[3]==0 and WIN_check[5]==0 and WIN_check[7]==0:
            Screens.End_Screen_X()
            
        #O wincon
        #row    
        if WIN_check[1]==5 and WIN_check[2]==5 and WIN_check[3]==5: 
            Screens.End_Screen_O()
        elif WIN_check[4]==5 and WIN_check[5]==5 and WIN_check[6]==5:
            Screens.End_Screen_O()
        elif WIN_check[7]==5 and WIN_check[8]==5 and WIN_check[9]==5:
            Screens.End_Screen_O()
        #column
        elif WIN_check[1]==5 and WIN_check[4]==5 and WIN_check[7]==5:
            Screens.End_Screen_O()
        elif WIN_check[2]==5 and WIN_check[5]==5 and WIN_check[8]==5:
            Screens.End_Screen_O()
        elif WIN_check[3]==5 and WIN_check[6]==5 and WIN_check[9]==5:
            Screens.End_Screen_O()
        #diagonal
        elif WIN_check[1]==5 and WIN_check[5]==5 and WIN_check[9]==5:
            Screens.End_Screen_O()
        elif WIN_check[3]==5 and WIN_check[5]==5 and WIN_check[7]==5:
            Screens.End_Screen_O()
        #Draw
        else:
            if any(i == 2 for i in WIN_check):
                pass
            else:
                Screens.End_Screen_Draw()
    
#main
def main(window): 
    global button, position, number, used, WIN_check
    button = Button()
    used = ['_',0,0,0, 0,0,0, 0,0,0]
    WIN_check = ['_', 2,2,2, 2,2,2, 2,2,2]
    number = 0
    clock = pg.time.Clock()
    s = True
    running = True
    
    Screens.Menu_bg()
    
    while running:
        
        clock.tick(60)
        position = pg.mouse.get_pos()
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                running = False
                break
            
            elif ev.type == pg.MOUSEBUTTONUP:
                if s == True: 
                    if button.Start_B1.collidepoint(position):
                        Screens.tictactoe()
                        
                        s = False
                    elif button.Quit_B2.collidepoint(position):
                       running = False
                elif button.Reset_B3.collidepoint(position):
                    Screens.tictactoe()
                    used = ['_',0,0,0, 0,0,0, 0,0,0]
                    WIN_check = ['_', 2,2,2, 2,2,2, 2,2,2]
                else:  
                    Playing.play()
                    number += 1             
        Playing.wincon()
        pg.display.update()
    
if __name__ == "__main__":
    main(window)