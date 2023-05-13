import pygame

#pygame base setup
pygame.init()
H, W = 720, 1280
pygame.display.set_caption("TicTacToe")
win = pygame.display.set_mode((W, H ))
clock = pygame.time.Clock()
running = True

#colors in use
black_color = (0, 0, 0)
white_color = (255,255,255)

def tictactoe():
    win.fill(white_color)
    c = pygame.draw.circle(win, black_color, (1000, 720/3), 90, width=10)
    x = (pygame.draw.line(win, (0, 0, 0), [920, 400], [1080, 580], 10), 
    pygame.draw.line(win, (0, 0, 0), [1080, 400], [920, 580], 10))
    Board()
    
def Board():
    S1 = pygame.draw.rect(win, black_color, (0, 0, 240, 240), width=10)
    S2 = pygame.draw.rect(win, black_color, (240, 0, 240, 240), width=10) 
    S3 = pygame.draw.rect(win, black_color, (480, 0, 240, 240), width=10)
    S4 = pygame.draw.rect(win, black_color, (0, 240, 240, 240), width=10)    
    S5 = pygame.draw.rect(win, black_color, (240, 240, 240, 240), width=10)
    S6 = pygame.draw.rect(win, black_color, (480, 240, 240, 240), width=10)
    S7 = pygame.draw.rect(win, black_color, (0, 480, 240, 240), width=10)
    S8 = pygame.draw.rect(win, black_color, (240, 480, 240, 240), width=10)
    S9 = pygame.draw.rect(win, black_color, (480, 480, 240, 240), width=10)
     
    
def Circle():
    pygame.draw.circle(win, black_color, (360, 360), 50, 10)

#def X():
    


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #elif event.type == pygame.mouse.get_pressed():
            
    tictactoe() 
    pygame.display.flip()
    
    clock.tick(60)
    
        
pygame.quit()