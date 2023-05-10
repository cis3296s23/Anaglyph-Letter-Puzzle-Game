

import Menu
from Menu import Menu
import pygame
import pygame_gui
import Game
import sys
from pygame_gui.windows import UIColourPickerDialog
from pygame_gui.elements import UIButton
from Grid import Grid
import unittest


pygame.init()

button_width = 200
button_height = 50
info = pygame.display.Info()
BLACK = (0, 0, 0)

screen_width = info.current_w
screen_height = info.current_h
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Anaglyph Letter Puzzle")
manager = pygame_gui.UIManager((screen_width, screen_height))
middle = (screen_width - button_width) / 2
right = screen_width - button_width - 10
top = 10
font = pygame.font.SysFont(None, 100)
selected_colour = None
#THIS IS THE CURRENT COLOR VARIABLES FOR LEFT AND RIGHT, HAVE GAME CLASS USE THESE:
okay_left = (200, 0, 0) 
okay_right = (0, 0, 200)
right_clicked = 0 
left_clicked = 0
 


class test_Menu(unittest.TestCase):
    
    
    right_color = (255, 0, 0)
    left_color = (0, 0, 255)
    selected_colour = (255, 255, 255)
    prev_left = left_color
    prev_right = right_color
    




    def test_generate_letter_bank(self):
        g = Grid(rows=5, cols=5, sequ_len=2, num_targets=2, row_space=1, col_space=1)
        g.generate_letter_bank()
        assert len(g.letter_bank) == 2
        
    def test_generate_target_indices(self):
        g = Grid(rows=5, cols=5, sequ_len=2, num_targets=3, row_space=1, col_space=1)
        g.generate_target_indices()
        assert not len(g.target_indices) == 2

    def test_generate_2d_grid(self):
        g = Grid(rows=5, cols=5, sequ_len=2, num_targets=2, row_space=1, col_space=1)
        g.generate_2d_grid()
        assert not len(g.grid) == 94
        #assert g.target in ''.join(g.grid)
        



    def test_right_eye_back_to_mode_page(self):
        selected_colour = (255, 255, 255)
        Menu.reset_colors(self)
        assert self.right_color == self.prev_right

