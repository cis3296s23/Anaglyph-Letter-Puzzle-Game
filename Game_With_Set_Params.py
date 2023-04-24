import pygame as pg
import pygame_gui as pg_gui
import math as m
import string as s
import random as r
from Grid import Grid


class Game_With_Set_Params:
    def __init__(self, rows, cols, sequ_len, num_targets, row_space, col_space, num_grids):
        self.rows = rows
        self.cols = cols
        self.grid_size = rows * cols
        self.sequ_len = sequ_len
        self.num_targets = num_targets
        self.row_space = row_space
        self.col_space = col_space
        self.num_grids = num_grids
        self.letter_bank = []
        self.sequ_bank = []
        self.diff_sequ = m.ceil(self.grid_size // 2)
        self.letter_bank_size = m.ceil(self.sequ_len * 1.5)
        self.similar_pairs = ['bd', 'pq', 'kx', 'co', 'mn', 'ec', 'il', 'wv', 'sz']
        self.target_indices = []
        self.sim_pair = ''
        self.target = ''
        self.other = ''
        self.sequ_bank_target_removed = []
        self.grids = []
        self.generate_grids()
        self.grids_completed = 0  # tracks the number of completed grids
        self.color_found = (0, 0, 0)

        # for i in range(self.num_grids):
        #     new_grid = Grid(self.rows, self.cols, self.sequ_len, self.num_targets, self.row_space, self.col_space)
        #     new_grid.generate_grid()
        #     self.grids.append(new_grid)

        pg.init()
        info = pg.display.Info()
        pg.display.set_caption("Anaglyph Letter Puzzle")
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        self.manager = pg_gui.UIManager((self.screen_width, self.screen_height))

        # Load font and calculate cell size for grid drawing
        self.font_size = 40
        self.font = pg.font.Font(None, self.font_size)
        self.cell_width = self.font_size
        self.cell_height = self.font_size


        # Calculate grid size for drawing
        self.grid_width = (self.cell_width * self.cols) + (self.col_space * (self.cols - 1))
        self.grid_height = (self.cell_height * self.rows) + (self.row_space * (self.rows - 1))

        # Calculate grid position for centering on screen
        self.grid_x = (self.screen_width - self.grid_width) / 2
        self.grid_y = (self.screen_height - self.grid_height) / 2

    def generate_grids(self):

        for i in range(self.num_grids):
            new_grid = Grid(self.rows, self.cols, self.sequ_len, self.num_targets, self.row_space, self.col_space)
            self.grids.append(new_grid)

    def draw_grid(self, current_grid, screen):
        for i in range(len(current_grid.grid_list)):
            sequ = current_grid.grid_list[i]
            row = i // self.cols
            col = i % self.cols
            color = (255, 255, 255)
            text_surface = self.font.render(sequ, True, color)
            rect = text_surface.get_rect()
            rect.center = ((col * self.cell_width) + (self.cell_width // 2) + self.grid_x + col * self.col_space,
                           (row * self.cell_height) + (self.cell_height // 2) + self.grid_y + row * self.row_space)
            screen.blit(text_surface, rect)

    def run(self):
        pg.init()
        info = pg.display.Info()
        pg.display.set_caption("Anaglyph Letter Puzzle")
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        self.manager = pg_gui.UIManager((self.screen_width, self.screen_height))
        self.grids = []
        self.generate_grids()
        running = True
        target_count = 0
        self.grids_completed = 0

        while running:
            # Draw the current grid
            current_grid = self.grids[self.grids_completed]
            self.draw_grid(current_grid, self.screen)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.MOUSEBUTTONUP:
                    mouse_pos = pg.mouse.get_pos()
                    clicked_col = (mouse_pos[0] - self.grid_x) // (self.cell_width + self.col_space)
                    clicked_row = (mouse_pos[1] - self.grid_y) // (self.cell_height + self.row_space)
                    clicked_index = (clicked_row * self.cols) + clicked_col
                    if clicked_index in current_grid.target_indices:

                        target_count += 1
                        # Check if all targets have been found
                        if target_count == len(current_grid.target_indices):
                            self.grids_completed += 1
                            if self.grids_completed == self.num_grids:
                                # Game is over, exit the loop
                                running = False
                            else:
                                # Move to the next grid
                                current_grid = self.grids[self.grids_completed]
                                target_count = 0
            self.screen.fill((0, 0, 0))
        pg.display.update()


