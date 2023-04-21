import math as m
import string as s
import random as r


class Grid:
    def __init__(self, rows, cols, sequ_len, num_targets, row_space, col_space):
        self.rows = rows
        self.cols = cols
        self.grid_size = rows * cols
        self.sequ_len = sequ_len
        self.num_targets = num_targets
        self.row_space = row_space
        self.col_space = col_space
        # self.random_spacing = random_spacing
        self.letter_bank = []
        self.sequ_bank = []
        self.diff_sequ = m.ceil(self.grid_size // 2)
        self.letter_bank_size = m.ceil(self.sequ_len * 1.5)
        self.similar_pairs = ['bd', 'pq', 'kx', 'co', 'mn', 'ec', 'il', 'wv','sz']
        self.target_indices = []
        self.sim_pair = ''
        self.target = ''
        self.other = ''
        self.sequ_bank_target_removed = []
        # self.space_btn_rows = ""
        # self.space_btn_cols = ""
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]

    def generate_letter_bank(self):
        sim_pair = r.choice(self.similar_pairs)
        if self.sequ_len == 1 or self.sequ_len == 2:
            self.letter_bank = [str(c) for c in sim_pair]
        else:
            vowels = ['a', 'e', 'i', 'o', 'u']
            for i in range(self.letter_bank_size):
                letter = (r.choice(s.ascii_lowercase))
                if letter not in vowels and letter not in self.letter_bank:
                    self.letter_bank.append(letter)
        print(self.letter_bank)

    def generate_sequ(self):
        if self.sequ_len == 1:
            return r.choice(self.letter_bank)
        elif self.sequ_len == 2:
            sequ = [r.choice(self.letter_bank) for i in range(self.sequ_len)]
            return "".join(sequ)
        else:
            sequ = r.sample(self.letter_bank, self.sequ_len)
            return "".join(sequ)

    def generate_sequ_bank(self):
        for i in range(self.diff_sequ):
            sequ = self.generate_sequ()
            if sequ not in self.sequ_bank:
                self.sequ_bank.append(sequ)
        print(self.sequ_bank)

    #targets cannot be directly next to each other
    def generate_target_indices(self):
        first = r.randint(1, self.grid_size - 1)
        self.target_indices.append(first)
        while len(self.target_indices) < self.num_targets:
            next_ind = r.randint(1, self.grid_size - 1)
            if not any([(next_ind - 1) in self.target_indices, next_ind in self.target_indices,
                        (next_ind + 1) in self.target_indices, (next_ind + 2) in self.target_indices]):
                self.target_indices.append(next_ind)

    def pick_target_sequence_and_remove(self):
        self.target = r.choice(self.sequ_bank)
        self.sequ_bank_target_removed = self.sequ_bank.copy()  # make a copy of the original sequ_bank
        self.sequ_bank_target_removed.remove(self.target)  #

    def generate_2d_grid(self):
        if not self.letter_bank:
            self.generate_letter_bank()
        if not self.sequ_bank:
            self.generate_sequ_bank()
        if not self.target_indices:
            self.generate_target_indices()
        if not self.target:
            self.pick_target_sequence_and_remove()
        # Fill the grid list with targets at target indices or random sequences
        grid_list = []
        for i in range(self.grid_size):
            if i in self.target_indices:
                grid_list.append(self.target)
            else:
                rand_sequ = r.choice(self.sequ_bank_target_removed)
                grid_list.append(rand_sequ)
            grid_list.append('')

        # Convert the grid list into a 2D grid split by rows and columns
        self.grid = [grid_list[i:i + self.cols * 2] for i in range(0, len(grid_list), self.cols * 2)]
        # if self.random_spacing is False:
        self.space_btn_cols = " " * self.col_space
        self.space_btn_rows = "\n" * self.row_space
        # self.space_btn_cols = " " * r.choice([self.min_space, self.max_space])
        # self.space_btn_rows = "\n" * r.choice([self.min_space, self.max_space])
        self.grid = [self.space_btn_cols.join(row).rstrip(self.space_btn_cols) for row in self.grid]
        self.grid = self.space_btn_rows.join(self.grid)

        print(self.grid)

    def generate_2d_grid_cols_dont_line_up(self):
        if not self.letter_bank:
            self.generate_letter_bank()
        if not self.sequ_bank:
            self.generate_sequ_bank()
        if not self.target_indices:
            self.generate_target_indices()
        if not self.target:
            self.pick_target_sequence_and_remove()

        # Fill the grid list with targets at target indices or random sequences
        grid_list = []
        for i in range(self.grid_size):
            if i in self.target_indices:
                grid_list.append(self.target)
            else:
                rand_sequ = r.choice(self.sequ_bank_target_removed)
                grid_list.append(rand_sequ)
            grid_list.extend([''] * self.col_space)

        # Add new line character after each row
        grid_list.extend(['\n'] * self.row_space)

        # Convert the grid list into a 2D grid split by rows and columns
        self.grid = [grid_list[i:i + self.cols + self.space_btn_cols] for i in
                     range(0, len(grid_list), self.cols + self.space_btn_cols)]
        self.grid = [self.row_space.join(row).rstrip(self.row_space) for row in self.grid]
        self.grid = '\n'.join(self.grid)

        print(self.grid)


new_grid = Grid(rows = 4, cols = 5, sequ_len = 2, num_targets = 5, col_space = 10, row_space = 4)
new_grid.generate_letter_bank()
new_grid.generate_sequ_bank()
new_grid.generate_target_indices()
new_grid.pick_target_sequence_and_remove()
print("target:", new_grid.target, ", Number of Targets:", new_grid.num_targets)
new_grid.generate_2d_grid()
