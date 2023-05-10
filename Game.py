import sys

import pygame as pg
import pygame_gui as pg_gui
import math as m
import string as s
import random as r
from Grid import Grid


class Game:
    
    '''
        The Game class imports the grid created from the Grid class and uses that to transform the once non-interactive grid printed in the terminal
        into an interactive grid that is displayed through pygame and sets up the actual gameplay. The class contans a contructor:
        _init_(self, rows, cols, sequ_len, num_targets, row_space, col_space, num_grids, right_color, left_color, quick), a generate_grids(self) method, generate_quick_grids(self)
        method, and lastly two more methods for drawing and running the game. Running this class, will run the game, causing for the grids to show.  
    '''

    def __init__(self, rows, cols, sequ_len, num_targets, row_space, col_space, num_grids, right_color, left_color, quick):
        
        '''
            __init__(self, rows, cols, sequ_len, num_targets, row_space, col_space, num_grids, right_color, left_color, quick). This method is the constructor
            for the Game class. It initializes all the instance variables of the class. It also initializes some additional variables that are used throughout
            the class, such as letter_bank, sequ_bank, similar_pairs, target_indices, sim_pair, target, other, sequ_bank_target_removed, grids, grids_completed,
            screen_width, and many more. This specific constructor is different from the others due to the fact 
            that it aids in producing the grid in a pygame window. It takes in 11 parameters, and it does not return anything.  
        '''
        self.rows = rows
        self.cols = cols
        self.grid_size = self.rows * self.cols
        self.sequ_len = sequ_len
        self.num_targets = num_targets
        self.row_space = row_space
        self.col_space = col_space
        self.num_grids = num_grids
        self.letter_bank = []
        self.sequ_bank = []
        self.diff_sequ = m.ceil(self.grid_size // 2)
        self.letter_bank_size = m.ceil(self.sequ_len * 1.5)
        self.similar_pairs = ['bd', 'pq', 'kx', 'co', 'mn', 'ec', 'il', 'wv']
        self.target_indices = []
        self.sim_pair = ''
        self.target = ''
        self.other = ''
        self.sequ_bank_target_removed = []
        self.grids = []
        self.generate_grids()
        self.grids_completed = 0  # tracks the number of completed grids
        self.quick = quick

        pg.init()
        info = pg.display.Info()
        pg.display.set_caption("Anaglyph Letter Puzzle")
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        self.manager = pg_gui.UIManager((self.screen_width, self.screen_height))
        self.current_grid = self.grids[self.grids_completed]
        self.font_size = 50
        self.font = pg.font.Font(None, self.font_size)
        self.sequ_spacer = "w" * self.sequ_len
        self.sequ_surface = self.font.render(self.sequ_spacer, True, (0,0,0))
        self.sequ_width = self.sequ_surface.get_rect().width
        self.sequ_height = self.sequ_surface.get_rect().height
        new_line_surface = self.font.render("\n", True, (0,0,0))
        self.col_space_string = " " * self.col_space
        self.row_space_height = new_line_surface.get_rect().height
        self.col_space_width = self.sequ_surface.get_rect().width


        self.cell_width = self.sequ_width
        self.cell_height = self.sequ_height

        # Calculate grid size for drawing
        self.grid_width = (self.cell_width * self.cols) + (self.col_space * (self.cols - 1))
        self.grid_height = (self.cell_height * self.rows) + (self.row_space * (self.rows - 1))
        self.grid_x = (self.screen_width - self.grid_width) // 2 -200
        self.grid_y = (self.screen_height - self.grid_height) // 2-200

        self.already_found = []
        self.right_color = right_color
        self.left_color = left_color

    def generate_grids(self):
        
        '''
            The method generate_grids(self) is a smaller method that has
            the role of choosing how many grids to produce before the user gets to the play the game.
            It uses the Grid class to create these new grids. It takes in 1 parameter, self, and it does not return anything.  
        '''
        for i in range(self.num_grids):
            new_grid = Grid(self.rows, self.cols, self.sequ_len, self.num_targets, self.row_space, self.col_space)
            self.grids.append(new_grid)

    def generate_quick_grids(self):
        
        '''
            The method “generate_quick_grids(self)” generates a list of Grid objects using randomly selected values for rows, cols, sequ_len, and num_targets.
            It appends each newly created Grid object to the grids list of the Game class. This method displays the grids used when the option “Quick Play”
            is chosen on the Menu page. Depending on the number of grids being produced, it sets a definite range for the rows, columns, sequence length,
            and target amount. By doing so, it organizes the grids into difficulty levels. Starting off with easy, moving into medium, and ending at hard.
            It then appends the new grid following its regulations. It takes in 1 parameter, self, and it does not return anything. It creates and appends a new grid.  
        '''

        for i in range(self.num_grids):
            if i < 2:
                rows = r.randint(5, 6)
                cols = r.randint(5, 6)
                sequ_len = 1
                num_targets = r.randint(1, 2)
            elif i < 4:
                rows = r.randint(5, 6)
                cols = r.randint(6, 7)
                sequ_len = 2
                num_targets = r.randint(2, 3)
            elif i < self.num_grids:
                rows = r.randint(6, 7)
                cols = r.randint(7, 8)
                sequ_len = 2
                num_targets = r.randint(3, 4)
            elif i < 8:
                rows = r.randint(5, 6)
                cols = r.randint(6, 7)
                sequ_len = 3
                num_targets = r.randint(2, 3)
            elif i < 10:
                rows = r.randint(5, 6)
                cols = r.randint(5, 6)
                sequ_len = r.randint(2, 3)
                num_targets = r.randint(4, 5)
            elif i < 17:
                rows = r.randint(4, 5)
                cols = r.randint(4, 6)
                sequ_len = 4
                num_targets = r.randint(1, 2)

            new_grid = Grid(rows, cols, sequ_len, num_targets, self.row_space, self.col_space)
            self.grids.append(new_grid)

    def draw_grid(self, screen, col_space_multiplier):
        
        '''
            Draw_grid(self, screen, col_space_multiplier)). This method is responsible for drawing the current grid on the screen. It takes in two arguments,
            screen and col_space_multiplier, where screen is the Pygame screen object and col_space_multiplier is a multiplier used to calculate the x-position
            of each cell in the grid. It calculates the dimensions and position of the grid based on the values of the initialized variable that were first
            stated in the _init_ constructor. It then uses Pygame to draw the grid on the screen, including the cells, the sequence of letters
            in each cell, and the target sequence.Takes in 3 parameters: self, screen, and col_space_multiplier. And it returns the list of cell_centers and rect_centers.  
        '''
        rect_centers = []
        cell_rects = []  # Create a list to store Rect objects for each cell
        target_text = "Target sequence: " + "".join(self.current_grid.target)
        target_surface = self.font.render(target_text, True, (255, 255, 255))
        target_rect = target_surface.get_rect()
        target_rect.topleft = (10, 10)
        screen.blit(target_surface, target_rect)
        esc_text = "Press escape to exit"
        esc_surface = self.font.render(esc_text, True, (255, 255, 255))
        esc_rect = esc_surface.get_rect()
        esc_rect.bottomleft = (10, self.screen_height - 100)
        screen.blit(esc_surface, esc_rect)

        for i in range(self.current_grid.grid_size):
            sequ = self.current_grid.grid_list[i]
            if i in self.already_found:
                sequ = ""
            row = i // self.cols
            col = i % self.cols
            if col % 2 == 1:
                color = self.right_color
            else:
                color = self.left_color
            text_surface = self.font.render(sequ, True, color)
            rect = text_surface.get_rect()
            rect.center = (
                (col * self.cell_width) + (self.cell_width / 2) + self.grid_x + col * col_space_multiplier,
                (row * self.cell_height) + (self.cell_height / 2) + self.grid_y + row * self.row_space)

            cell_rect = pg.Rect(rect.midleft, (self.cell_width+self.cell_width//self.sequ_width + 1, self.cell_height))
            cell_rects.append(cell_rect)

            if self.current_grid.targets_left > 0:
                remaining_text = f"Targets remaining: {self.current_grid.targets_left}"
                remaining_surface = self.font.render(remaining_text, True, (255, 255, 255))
                remaining_rect = remaining_surface.get_rect()
                remaining_rect.topleft = (10, 100)
                screen.blit(remaining_surface, remaining_rect)
            screen.blit(text_surface, rect)
            rect_centers.append(rect.center)

        # Return both the list of cell centers and the list of cell Rects
        return rect_centers, cell_rects

    def run(self):
        
        '''
            The run(self) method is what runs the gameplay loop and showcases the screen on which the game is played.
            It initzialies the pygame librabry, setting up the window with its labels, and uses the lists returned
            from the  draw_grid() method. It also uses some of the variables listed in the constructor, and
            while running, it takes note of what characters are being selected, and removes the selectedtarget when clicked on,
            ending the game once all the targets of all the produced grids have been found. It takes in 1 parameter, and it does not return anything 
        '''
        
        pg.init()
        info = pg.display.Info()
        pg.display.set_caption("Anaglyph Letter Puzzle")
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        self.manager = pg_gui.UIManager((self.screen_width, self.screen_height))
        self.grids = []
        self.grids_completed = 0
        self.already_found = []

        if self.quick == True:
            self.num_grids = 10
            self.generate_quick_grids()
        else:
            col_space_multiplier = self.sequ_len * self.sequ_len * (self.sequ_len + self.sequ_len//2)
            self.generate_grids()
        running = True
        print(self.current_grid.grid_list)
        rect_centers = []
        cell_rects = []
        # col_space_multiplier = 1
        # if self.quick == False:
        #     col_space_multiplier = self.sequ_len * self.sequ_len * (self.sequ_len + 1)
        while running:
            self.current_grid = self.grids[self.grids_completed]
            self.rows = self.current_grid.rows
            self.cols = self.current_grid.cols
            self.grid_size = self.current_grid.rows * self.current_grid.cols
            self.sequ_len = self.current_grid.sequ_len
            self.num_targets = self.current_grid.num_targets
            self.row_space = self.current_grid.row_space
            self.col_space = self.current_grid.col_space
            if self.quick == True:
                col_space_multiplier = self.sequ_len * self.sequ_len * (self.sequ_len + 2)

            rect_centers, cell_rects = self.draw_grid(self.screen, col_space_multiplier)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = pg.mouse.get_pos()
                    for i, cell_rect in enumerate(cell_rects):
                        if cell_rect.collidepoint(mouse_pos) and i in self.current_grid.target_indices:
                           if i not in self.already_found:  # Check if the mouse click was inside the cell Rect
                                self.current_grid.targets_left -= 1
                                self.already_found.append(i)

                    if self.current_grid.targets_left == 0:
                        self.grids_completed += 1
                        if self.grids_completed == self.num_grids:
                            # Game is over, exit the loop
                            return
                        else:
                            # Move to the next grid
                            self.current_grid = self.grids[self.grids_completed]
                            self.already_found = []
                            rect_centers = []
                            cell_rects = []
            self.screen.fill((0, 0, 0))
        pg.display.update()







