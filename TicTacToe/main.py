import pygame as pg

#pg base setup
pg.init()
W, H = 1280 ,720 
pg.display.set_caption("TicTacToe")
win = pg.display.set_mode((W, H ))

#colors in use
black_color = (0, 0, 0)
white_color = (255,255,255)
FONT = pg.font.Font("freesansbold.ttf", 50)

#tictactoe
def tictactoe():
    win.fill(white_color)
    pg.draw.circle(win, black_color, (1000, 720/3), 90, width=10)
    pg.draw.line(win, black_color, [920, 400], [1080, 580], 10)
    pg.draw.line(win, black_color, [1080, 400], [920, 580], 10)
    Board()


#Board
W1, H1 = 0, 0
W2, H2 = 240, 240
W3, H3 = 480, 480   
class Board:
    def __init__(self):
        
        self.S1 = pg.draw.rect(win, black_color, (W1, H1, 240, 240), width=10)
        self.S2 = pg.draw.rect(win, black_color, (W2, H1, 240, 240), width=10) 
        self.S3 = pg.draw.rect(win, black_color, (W3, H1, 240, 240), width=10)
        self.S4 = pg.draw.rect(win, black_color, (W1, H2, 240, 240), width=10)    
        self.S5 = pg.draw.rect(win, black_color, (W2, H2, 240, 240), width=10)
        self.S6 = pg.draw.rect(win, black_color, (W3, H2, 240, 240), width=10)
        self.S7 = pg.draw.rect(win, black_color, (W1, H3, 240, 240), width=10)
        self.S8 = pg.draw.rect(win, black_color, (W2, H3, 240, 240), width=10)
        self.S9 = pg.draw.rect(win, black_color, (W3, H3, 240, 240), width=10)
    
board = Board()
  
   
def Circle(x, y):
    pg.draw.circle(win, black_color, (x, y), 50, 10)


def X(a, b, c, d):
    pg.draw.line(win, black_color, a, b, 10)
    pg.draw.line(win, black_color, c, d, 10)

'''def play_tictactoe():
    position = pg.mouse.get_pos()
    if pg.mouse.get_pressed()[0]:
        if board.S1.collidepoint(position):
           X([0,0], [240, 240], [240, 0], [0, 240])   ''' 

def main():
    clock = pg.time.Clock()
    number = 0
    running = True
    button = pg.Rect(0, 0, 240, 240)
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break
            # check MOUSEBUTTONDOWN evet
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button.collidepoint(event.pos):
                        number += 1
                        X([0,0], [240, 240], [240, 0], [0, 240]), (0,0)
                        
        
        tictactoe()
        win.fill(white_color)
        pg.draw.rect(win, black_color, button, width=10)
        text_surf = FONT.render(str(number), True, black_color)
        # You can pass the center directly to the `get_rect` method.
        text_rect = text_surf.get_rect(center=(W/2, 30))
        win.blit(text_surf, text_rect)
        pg.display.update()    

main()       
pg.quit()