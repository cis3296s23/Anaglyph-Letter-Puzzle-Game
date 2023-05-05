import math as m
import string as s
import random as r
import pygame as pg

class Grid:
    def __init__(self, rows, cols, sequ_len, num_targets):
        self.rows = rows
        self.cols = cols
        self.grid_size = self.rows * self.cols
        self.sequ_len = sequ_len
        self.num_targets = num_targets
        self.letter_bank = []
        self.sequ_bank = []
        self.diff_sequ = m.ceil(self.grid_size // 2)
        self.letter_bank_size = m.ceil(self.sequ_len * 1.5)
        self.similar_pairs = ['bd', 'pq', 'oe', 'co', 'mn', 'ec', 'il', 'wv', 'gq', ]
        self.target_indices = []
        self.sim_pair = ''
        self.target = ''
        self.other = ''
        self.sequ_bank_target_removed = []
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.font = pg.font.SysFont(None, 30)  # choose a font and font size
        self.grid_list = []
        self.targets_left = self.num_targets
        self.generate_letter_bank()
        self.generate_sequ_bank()
        self.generate_target_indices()
        self.pick_target_sequence_and_remove()
        self.generate_grid()


    def generate_letter_bank(self):
        sim_pair = r.choice(self.similar_pairs)
        if self.sequ_len == 1 or self.sequ_len == 2:
            self.letter_bank = [str(c) for c in sim_pair]
        else:
            vowels = ['a', 'e', 'i', 'o', 'u']
            for i in range(self.letter_bank_size):
                letter = (r.choice(s.ascii_lowercase))
                while letter in vowels or letter in self.letter_bank:
                    letter = (r.choice(s.ascii_lowercase))
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
        print(self.grid)

    def generate_grid(self):
        if not self.letter_bank:
            self.generate_letter_bank()
        if not self.sequ_bank:
            self.generate_sequ_bank()
        if not self.target_indices:
            self.generate_target_indices()
        if not self.target:
            self.pick_target_sequence_and_remove()
        # Fill the grid list with targets at target indices or random sequences
        for i in range(self.grid_size):
            if i in self.target_indices:
                self.grid_list.append(self.target)
            else:
                rand_sequ = r.choice(self.sequ_bank_target_removed)
                self.grid_list.append(rand_sequ)
        print(self.grid_list)


