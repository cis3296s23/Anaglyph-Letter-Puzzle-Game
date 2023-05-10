import math as m
import string as s
import random as r
import pygame as pg
class Grid:
    '''
        The Grid Class is what generates the grid that is actually used for the game. It contains 8 methods, all pertaining to creating the letters used,
        the letters that can be paired together, the sequence amount, the amount of targets and more. It is an essential class to
        the gaming application. It's methods are: _init_(self, rows, cols, sequ_len, num_targets, row_space, col_space),
        generate_letter_bank(self), generate_sequ(self), generate_sequ_bank(self), generate_target_indicies(self),
        pick_target_sequence_and_remove(self),generate_2d_grid(self), and lastly generate_grid(self). There are no global variables 
    '''
    
    def __init__(self, rows, cols, sequ_len, num_targets, row_space, col_space):
        
        '''
            The “_init_” constructor's purpose is to initialize the necessary variables needed for the 
            pygame windows as well as grid variables. These variables can also be affected in the Mode Select and Settings Page.
            Initializes rows, columns, space, pairs, sequences, targets, and the other functions used in the class.  
        '''
        self.rows = rows
        self.cols = cols
        self.grid_size = self.rows * self.cols
        self.sequ_len = sequ_len
        self.num_targets = num_targets
        self.row_space = row_space
        self.col_space = col_space
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
        self.rect = pg.Rect(0, 0, cols * col_space, rows * row_space)
        self.font = pg.font.SysFont(None, 30)  # choose a font and font size
        self.grid_list = []
        self.targets_left = self.num_targets
        self.generate_letter_bank()
        self.generate_sequ_bank()
        self.generate_target_indices()
        self.pick_target_sequence_and_remove()
        self.generate_grid()


    def generate_letter_bank(self):
        '''
            The method generate_letter_bank() has the task of figuring out which letters to
            use for the current grid shown on the screen. Depending on sequence length it will add in certain letters such as vowels.
            It later appends the randomly selected letter. Takes in 1 parameter, self, and does not return anything.  
        '''
        
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
        
        '''
            “generate_sequ()” is another function in the class and it works closely with the generate_letter_bank() method above it.
            The purpose of this function is to create the sequence length that will be shown on the
            screeen. The lowest amount being 1, and the highest being 4. Takes in 1 parameter, self, does not return anything.  
        '''
        if self.sequ_len == 1:
            return r.choice(self.letter_bank)
        elif self.sequ_len == 2:
            sequ = [r.choice(self.letter_bank) for i in range(self.sequ_len)]
            return "".join(sequ)
        else:
            sequ = r.sample(self.letter_bank, self.sequ_len)
            return "".join(sequ)

    def generate_sequ_bank(self):
        
        '''
            This method uses the generate_sequ() function to create a bank that stores each possible sequence we can
            use. This comes in handy when having to make numerous grids, especially if in a harder difficulty level or specifically chosen in Mode Select Page
        '''
        
        for i in range(self.diff_sequ):
            sequ = self.generate_sequ()
            if sequ not in self.sequ_bank:
                self.sequ_bank.append(sequ)
        print(self.sequ_bank)

    #targets cannot be directly next to each other
    def generate_target_indices(self):
        
        '''
            The function “generate_target_indicies()” focuses solely on the target characters that
            must be clicked on in order to make progress and thus moving to the next grid. Creates a variable named first
            that takes a random integer from a range of 1 to the grid_size minus 1. Keeps track
            if the number of indices ever matches the number of targets. Takes in 1 parameter, self, and does not return anything.  
        '''
        first = r.randint(1, self.grid_size - 1)
        self.target_indices.append(first)
        while len(self.target_indices) < self.num_targets:
            next_ind = r.randint(1, self.grid_size - 1)
            if not any([(next_ind - 1) in self.target_indices, next_ind in self.target_indices,
                        (next_ind + 1) in self.target_indices, (next_ind + 2) in self.target_indices]):
                self.target_indices.append(next_ind)

    def pick_target_sequence_and_remove(self):
        
        '''
            This function, “pick_target_sequence_and_remove()” has the job of removing the correctly chosen target
            from the grid, and keeping it removed until all the targets have been found. Using the sequence bank,
            it uses the built-in python remove function to remove the specific target. Takes in 1 parameter, self, and it does not return anything.  
        '''
        
        self.target = r.choice(self.sequ_bank)
        self.sequ_bank_target_removed = self.sequ_bank.copy()  # make a copy of the original sequ_bank
        self.sequ_bank_target_removed.remove(self.target)  #

    def generate_2d_grid(self):
        
        '''
            The method “generate_2d_grid()” calls the methods described above in a specific order in order to achieve
            an actual grid. When running each of the methods, different and equally important components of the grid are produced or established.
            It later, fills in the list that it has made, going through each index and  appending the correct amount of targets.
            Lastly splitting the list to create rows and columns. Takes in 1 parameter, self, and does not return anything, the output is a 2d grid 
        '''
        
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
        
        '''
            Generate_grid(): calls the methods described above in a specific order in order to achieve an actual grid.
            When running each of the methods, different and equally important components of the grid are produced or established.
            It later fills in the list that it has made, going through each index and appending the correct number of
            targets. Almost the exact same as generate_2d_grid() method, however it does not split the lists, thus not
            creating a 2d affect to the output. Takes in 1 parameter, self, and does not return anything, the output is a list.  
        '''
        
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


