import pygame as pg
import pygame_gui as pg_gui
import math as m
import string as s
import random as r
from Grid import Grid
from Game_With_Set_Params import Game_With_Set_Params




class Game_With_Set_Params:
    def __init__(self, rows, cols, sequ_len, num_targets, row_space, col_space, num_grids, right_color, left_color):
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
        self.similar_pairs = ['bd', 'pq', 'kx', 'co', 'mn', 'ec', 'il', 'wv']
        self.target_indices = []
        self.sim_pair = ''
        self.target = ''
        self.other = ''
        self.sequ_bank_target_removed = []
        self.grids = []
        self.generate_grids()
        self.grids_completed = 0  # tracks the number of completed grids
        self.color_found = (0, 0, 0)

        pg.init()
        info = pg.display.Info()
        pg.display.set_caption("Anaglyph Letter Puzzle")
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        self.manager = pg_gui.UIManager((self.screen_width, self.screen_height))

        # Load font and calculate cell size for grid drawing
        self.font_size = 60
        self.font = pg.font.Font(None, self.font_size)
        sequ_surface = self.font.render(self.target, True, (0, 0, 0))
        self.sequ_width = sequ_surface.get_rect().width
        self.sequ_height = sequ_surface.get_rect().height
        new_line_surface = self.font.render("\n", True, (0, 0, 0))
        self.col_space_string = "\t" * col_space * self.sequ_len * 10
        tab_surface = self.font.render(self.col_space_string, True, (0, 0, 0))
        self.row_space_height = new_line_surface.get_rect().height
        self.col_space_width = tab_surface.get_rect().width
        self.col_space_render = col_space * self.col_space_width

        self.cell_width = self.sequ_width
        self.cell_height = self.sequ_height

        # Calculate grid size for drawing
        self.grid_width = (self.cell_width * self.cols) + (self.col_space_render * (self.cols - 1))
        self.grid_height = (self.cell_height * self.rows) + (self.row_space * (self.rows - 1))

        # Calculate grid position for centering on screen
        # self.grid_x = (self.screen_width - self.grid_width) / 2
        # self.grid_y = (self.screen_height - self.grid_height) / 2
        self.grid_x = (self.screen_width - self.grid_width) // 2
        self.grid_y = (self.screen_height - self.grid_height) // 2

        self.target_indices = []
        self.already_found = []
        self.right_color = right_color
        self.left_color = left_color

    def generate_grids(self):
        for i in range(self.num_grids):
            new_grid = Grid(self.rows, self.cols, self.sequ_len, self.num_targets, self.row_space, self.col_space)
            self.grids.append(new_grid)

    def draw_grid(self, current_grid, screen, targets_left):
        for i in range(len(current_grid.grid_list)):
            print(current_grid.target)
            target_text = "Target sequences: " + "".join(current_grid.target)
            print(target_text)
            target_surface = self.font.render(target_text, True, (255, 255, 255))
            target_rect = target_surface.get_rect()
            target_rect.topleft = (10, 10)
            screen.blit(target_surface, target_rect)
            sequ = current_grid.grid_list[i]
            if i in self.already_found:
                sequ = ""
            # else:
            #     sequ = current_grid.grid_list[i]
            row = i // self.cols
            col = i % self.cols
            if i % 2 == 0:
                color = self.right_color
            else:
                color = self.left_color
            # color = (255, 255, 255)
            text_surface = self.font.render(sequ, True, color)
            rect = text_surface.get_rect()
            rect.center = (
                (col * self.cell_width) + (self.cell_width / 2) + self.grid_x + col * self.col_space_render,
                (row * self.cell_height) + (self.cell_height / 2) + self.grid_y + row * self.row_space)

            # rect = text_surface.get_rect()
            # rect.center = ((col * self.cell_width + 5) + (self.cell_width / 2) + self.grid_x + col * self.col_space_render,
            #                (row * self.cell_height) + (self.cell_height / 2) + self.grid_y + row * self.row_space)
            screen.blit(text_surface, rect)
            if targets_left > 0:
                remaining_text = f"Targets remaining: {targets_left}"
                remaining_surface = self.font.render(remaining_text, True, color)
                remaining_rect = remaining_surface.get_rect()
                remaining_rect.topright = (self.screen_width - 10, 10)
                screen.blit(remaining_surface, remaining_rect)

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
        current_grid = self.grids[self.grids_completed]
        self.already_found = []

        self.target_indices = current_grid.target_indices

        while running:
            # Draw the current grid
            self.draw_grid(current_grid, self.screen, current_grid.targets_left)

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = pg.mouse.get_pos()

                    clicked_col = (mouse_pos[0] - self.grid_x) // (self.cell_width + self.col_space_render)
                    clicked_row = (mouse_pos[1] - self.grid_y) // (self.cell_height + self.row_space)

                    clicked_index = (clicked_row * self.cols) + clicked_col

                    if clicked_index in current_grid.target_indices and clicked_index not in self.already_found:
                        current_grid.targets_left -= 1
                        self.already_found.append(clicked_index)

                        # Check if all targets have been found

                        # if current_grid.targets_left > 1:
                        #     continue
                        #
                        # # if target_count == len(current_grid.target_indices):
                        # else:
                        if current_grid.targets_left == 0:
                            self.grids_completed += 1
                            if self.grids_completed == self.num_grids:
                                # Game is over, exit the loop
                                return
                            else:
                                # Move to the next grid
                                current_grid = self.grids[self.grids_completed]
                                self.already_found = []

            self.screen.fill((0, 0, 0))
        pg.display.update()


