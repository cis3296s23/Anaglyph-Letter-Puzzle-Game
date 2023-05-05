import sys

import pygame as pg
import pygame_gui as pg_gui
import math as m
import string as s
import random as r
from Grid import Grid


class Game:

    def __init__(self, rows, cols, sequ_len, num_targets, num_grids, right_color, left_color, quick):
        self.rows = rows
        self.cols = cols
        self.grid_size = self.rows * self.cols
        self.sequ_len = sequ_len
        self.num_targets = num_targets
        self.num_grids = num_grids
        self.letter_bank = []
        self.sequ_bank = []
        self.diff_sequ = m.ceil(self.grid_size // 2)
        self.letter_bank_size = m.ceil(self.sequ_len * 1.5)
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
        self.font_size = 60
        self.font = pg.font.Font(None, self.font_size)
        self.sequ_spacer = "w  " * self.sequ_len
        self.sequ_surface = self.font.render(self.sequ_spacer, True, (0,0,0))
        self.sequ_width = self.sequ_surface.get_rect().width
        self.sequ_height = self.sequ_surface.get_rect().height
        new_line_surface = self.font.render("\n", True, (0,0,0))
        self.row_space_height = new_line_surface.get_rect().height
        self.col_space_width = self.sequ_surface.get_rect().width


        self.cell_width = self.sequ_width
        self.cell_height = self.sequ_height

        # Calculate grid size for drawing
        self.grid_width = (self.sequ_width * self.cols) + (self.cols - 1)
        self.grid_height = (self.sequ_height * self.rows) + (self.rows - 1)
        # self.grid_x = (self.screen_width - self.grid_width) // 2
        self.grid_x = (self.screen_width - self.grid_width) // 2 - self.grid_width //2
        self.grid_y = 200

        self.already_found = []
        self.right_color = right_color
        self.left_color = left_color

    def generate_grids(self):
        for i in range(self.num_grids):
            new_grid = Grid(self.rows, self.cols, self.sequ_len, self.num_targets)
            self.grids.append(new_grid)

    def generate_quick_grids(self):

        for i in range(self.num_grids):

            if i < 2:
                rows = r.randint(5, 6)
                cols = r.randint(5, 6)
                sequ_len = 1
                num_targets = r.randint(1, 3)
            elif i < 4:
                rows = r.randint(5, 6)
                cols = r.randint(5, 6)
                sequ_len = 2
                num_targets = 1
            elif i < 7:
                rows = r.randint(7,9)
                cols = r.randint(8,9)
                sequ_len = 1
                num_targets = r.randint(2,3)
            elif i < 9:
                rows = r.randint(9, 10)
                cols = r.randint(10, 11)
                sequ_len = 1
                num_targets = 2
            elif i < 11:
                rows = r.randint(7, 8)
                cols = r.randint(8, 9)
                sequ_len = 2
                num_targets = r.randint(2,3)
            elif i < 12:
                rows = r.randint(5, 6)
                cols = 6
                sequ_len = 3
                num_targets = 1
            elif i < 13:
                rows = 6
                cols = r.randint(6, 7)
                sequ_len = 3
                num_targets = 2
            elif i < self.num_grids:
                rows = r.randint(6, 8)
                cols = r.randint(6, 8)
                sequ_len = 3
                num_targets = r.randint(1,3)

            new_grid = Grid(rows, cols, sequ_len, num_targets)
            self.grids.append(new_grid)

    def draw_grid(self, screen, col_space_multiplier):

        rect_centers = []
        cell_rects = []  # Create a list to store Rect objects for each cell
        target_text = "Target sequence: " + "".join(self.current_grid.target)
        target_surface = self.font.render(target_text, True, (255, 255, 255))
        target_rect = target_surface.get_rect()
        target_rect.topleft = (10, 10)
        screen.blit(target_surface, target_rect)
        grid_text = "Grids remaining: " + "".join(str(self.num_grids-self.grids_completed))
        grid_surface = self.font.render(grid_text, True, (255, 255, 255))
        grid_rect = grid_surface.get_rect()
        grid_rect.topright = (self.screen_width-10, 10)
        screen.blit(grid_surface, grid_rect)
        esc_text = "Press escape to exit"
        esc_surface = self.font.render(esc_text, True, (255, 255, 255))
        esc_rect = esc_surface.get_rect()
        esc_rect.topleft = (10, esc_rect.height + 20)
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
                (row * self.cell_height) + (self.cell_height / 2) + self.grid_y + row)

            cell_rect = pg.Rect(rect.midleft, (self.cell_width + self.cell_width//self.sequ_width + 1, self.cell_height))
            cell_rects.append(cell_rect)

            # if self.current_grid.targets_left > 0:
            remaining_text = f"Targets remaining: {self.current_grid.targets_left}"
            remaining_surface = self.font.render(remaining_text, True, (255, 255, 255))
            remaining_rect = remaining_surface.get_rect()
            remaining_rect.topright = (self.screen_width - 10, remaining_rect.height + 20)
            screen.blit(remaining_surface, remaining_rect)
            screen.blit(text_surface, rect)
            rect_centers.append(rect.center)

        # Return both the list of cell centers and the list of cell Rects
        return rect_centers, cell_rects

    def run(self):
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
            self.num_grids = 15
            self.generate_quick_grids()
        else:
            col_space_multiplier = self.sequ_len * self.sequ_len * (self.sequ_len + self.sequ_len//2)
            self.generate_grids()
        running = True
        print(self.current_grid.grid_list)
        rect_centers = []
        cell_rects = []

        while running:
            self.current_grid = self.grids[self.grids_completed]
            self.rows = self.current_grid.rows
            self.cols = self.current_grid.cols
            self.grid_size = self.current_grid.rows * self.current_grid.cols
            self.sequ_len = self.current_grid.sequ_len
            self.num_targets = self.current_grid.num_targets
            self.grid_width = (self.sequ_width * self.cols) + (self.cols - 1)
            self.grid_height = (self.sequ_height * self.rows) + (self.rows - 1)
            self.grid_x =(self.screen_width - self.grid_width) // 2 - self.grid_width // 3
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
                    if event.key == pg.K_ESCAPE: #return to menu
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
                            return # Game is over, exit the loop, return to menu
                        else:
                            # Move to the next grid
                            self.current_grid = self.grids[self.grids_completed]
                            self.already_found = []
                            cell_rects = []
            self.screen.fill((0, 0, 0))
        pg.display.update()