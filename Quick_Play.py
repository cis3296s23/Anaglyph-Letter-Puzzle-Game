import pygame as pg
import pygame_gui as pg_gui
import math as m
import string as s
import random 
from Grid import Grid


class Quick_Play:
    def __init__(self, min_num_grids, max_num_grids, min_rows, max_rows, min_cols, max_cols, min_sequ_len, max_sequ_len, min_num_targets, max_num_targets, min_row_space, max_row_space, min_col_space, max_col_space):
        self.min_num_grids = min_num_grids
        self.max_num_grids = max_num_grids
        self.min_rows = min_rows
        self.max_rows = max_rows
        self.min_cols = min_cols
        self.max_cols = max_cols
        self.min_sequ_len = min_sequ_len
        self.max_sequ_len = max_sequ_len
        self.min_num_targets = min_num_targets
        self.max_num_targets = max_num_targets
        self.min_row_space = min_row_space
        self.max_row_space = max_row_space
        self.min_col_space = min_col_space
        self.max_col_space = max_col_space
        #makign rows and columns 
        self.rows_count = random.randint(self.min_rows, self.max_rows) 
        self.cols_count = random.randint(self.min_cols, self.max_cols)
        self.sequ_len_count = random.randint(self.min_sequ_len, self.max_sequ_len)
        self.num_targets_count = random.randint(self.min_num_targets, self.max_num_targets)
        self.row_space_count = random.randint(self.min_row_space, self.max_row_space)
        self.col_space_count = random.randint(self.min_col_space, self.max_col_space)
        self.num_grids_count = random.randint(self.min_num_grids, self.max_num_grids)
        
        self.grid_size = self.rows_count * self.cols_count
        self.letter_bank = []
        self.sequ_bank = []
        self.diff_sequ = m.ceil(self.grid_size // 2)
        self.letter_bank_size = m.ceil(self.sequ_len_count * 1.5)
        self.similar_pairs = ['bd', 'pq', 'kx', 'co', 'mn', 'ec', 'il', 'wv']
        self.target_indices = []
        self.sim_pair = ''
        self.target = ''
        self.other = ''
        self.sequ_bank_target_removed = []
        self.grids = []
        self.generate_grids()
        self.grids_completed = 0 
        self.color_found = (0, 0, 0)

        pg.init()
        info = pg.display.Info()
        pg.display.set_caption("Anaglyph Letter Puzzle")
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        self.manager = pg_gui.UIManager((self.screen_width, self.screen_height))
        self.font_size = 60
        self.font = pg.font.Font(None, self.font_size)
        sequ_surface = self.font.render(self.target, True, (0,0,0))
        self.sequ_width = sequ_surface.get_rect().width
        self.sequ_height = sequ_surface.get_rect().height
        new_line_surface = self.font.render("\n", True, (0,0,0))
        self.col_space_string = "\t" * self.col_space_count * self.sequ_len_count * 10
        tab_surface = self.font.render(self.col_space_string, True, (0,0,0))
        self.row_space_height = new_line_surface.get_rect().height
        self.col_space_width = tab_surface.get_rect().width
        self.col_space_render = self.col_space_count * self.col_space_width

        self.cell_width = self.sequ_width
        self.cell_height = self.sequ_height
        self.grid_width = (self.cell_width * self.cols_count) + (self.col_space_render * (self.cols_count - 1))
        self.grid_height = (self.cell_height * self.rows_count) + (self.row_space_count * (self.rows_count - 1))

        self.grid_x = (self.screen_width - self.grid_width) // 2
        self.grid_y = (self.screen_height - self.grid_height) // 2

        self.target_indices = []
        self.already_found = []

    def generate_grids(self):
        for i in range(self.num_grids_count):
            new_grid = Grid(self.rows_count, self.cols_count, self.sequ_len_count, self.num_targets_count, self.row_space_count, self.col_space_count)
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
            row = i // self.cols_count
            col = i % self.cols_count
            color = (255, 255, 255)
            text_surface = self.font.render(sequ, True, color)
            rect = text_surface.get_rect()
            rect.center = (
            (col * self.cell_width) + (self.cell_width / 2) + self.grid_x + col * self.col_space_render,
            (row * self.cell_height) + (self.cell_height / 2) + self.grid_y + row * self.row_space_count)
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
                    clicked_row = (mouse_pos[1] - self.grid_y) // (self.cell_height + self.row_space_count)

                    clicked_index = (clicked_row * self.cols_count) + clicked_col

                    if clicked_index in current_grid.target_indices and clicked_index not in self.already_found:
                        current_grid.targets_left -= 1
                        self.already_found.append(clicked_index)

                        if current_grid.targets_left == 0:
                            self.grids_completed += 1
                            if self.grids_completed == self.num_grids_count:
                                return
                            else:
                                current_grid = self.grids[self.grids_completed]
                                self.already_found = []

            self.screen.fill((0, 0, 0))
        pg.display.update()

    '''
    def generate_grids(self):
    num_grids = random.randint(self.min_num_grids, self.max_num_grids)
    for i in range(num_grids):
        rows = random.randint(self.min_rows, self.max_rows)
        cols = random.randint(self.min_cols, self.max_cols)
        sequ_len = random.randint(self.min_sequ_len, self.max_sequ_len)
        num_targets = random.randint(self.min_num_targets, self.max_num_targets)
        row_space = random.randint(self.min_row_space, self.max_row_space)
        col_space = random.randint(self.min_col_space, self.max_col_space)
        this_grid = Grid(rows, cols, sequ_len, num_targets, row_space, col_space)
        self.grids.append(this_grid)
        
    '''