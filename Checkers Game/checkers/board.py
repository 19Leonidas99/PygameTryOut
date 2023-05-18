import pygame as pg
from .constants import *

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        
    def draw_checkers_board(self, display):
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pg.draw.rect(display, )