import random
import sys

import pygame
import pygame_gui
from pygame_gui.elements import UIButton
from pygame_gui.windows import UIColourPickerDialog

from Game_With_Set_Params import Game_With_Set_Params
import Game


class Home:
    def __init__(self):

        pygame.init()

        self.button_width = 200
        self.button_height = 50
        self.info = pygame.display.Info()
        self.screen_width = self.info.current_w
        self.screen_height = self.info.current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Anaglyph Letter Puzzle")
        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height))
        self.middle = (self.screen_width - self.button_width) / 2
        self.right = self.screen_width - self.button_width - 10
        self.top = 10
        self.font = pygame.font.SysFont(None, 100)
        self.right_color = (255,0,0)
        self.left_color = (0,0,255)
        self.selected_colour = (255,255,255)
        self.prev_left = self.left_color
        self.prev_right = self.right_color

    def back_to_menu(self):
        pygame.display.set_caption("Letter Puzzle")
        self.manager = pygame_gui.UIManager((self.screen.get_width(), self.screen.get_height()))
        self.menu_page()


    pygame.init()

    button_width = 200
    button_height = 50
    info = pygame.display.Info()

    screen_width = info.current_w
    screen_height = info.current_h
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Anaglyph Letter Puzzle")
    manager = pygame_gui.UIManager((screen_width, screen_height))
    middle = (screen_width - button_width) / 2
    right = screen_width - button_width - 10
    top = 10
    font = pygame.font.SysFont(None, 100)


    def menu_page(self):
        x = self.middle
        y = 200
        min_num_grids = 4
        max_num_grids = 32
        min_rows = 4
        max_rows = 8
        min_cols = 4
        max_cols = 8
        min_sequ_len = 1
        max_sequ_len = 3
        min_num_targets = 1
        max_num_targets = 5
        min_row_space= 1
        max_row_space = 3
        min_col_space = 1
        max_col_space = 5

        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height))

        title_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((self.middle, 100), (self.button_width, self.button_height)),
                                                  text="Anaglyph Letter Puzzle", manager=self.manager)

        start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y), (self.button_width, self.button_height)), text="Quick Play", manager=self.manager)
        mode_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y + 100), (self.button_width, self.button_height)), text="Mode Select", manager=self.manager)
        settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y + 200), (self.button_width, self.button_height)), text="Settings", manager=self.manager)
        help_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y + 300), (self.button_width, self.button_height)), text="Help", manager=self.manager)
        login_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y + 400), (self.button_width, self.button_height)), text="Login", manager=self.manager)
        quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y + 500), (self.button_width, self.button_height)), text="Quit", manager=self.manager)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == start_button:
                            quick_game = Game_With_Set_Params(random.randint(4,6), random.randint(4,6), random.randint(min_sequ_len, 2), random.randint(min_num_targets, 3), min_row_space, min_col_space, 3, self.right_color, self.left_color, False)
                            quick_game.run()
                            quick_game = Game_With_Set_Params(random.randint(5,6), random.randint(5,6), random.randint(min_sequ_len, 2), random.randint(min_num_targets, 3), min_row_space, min_col_space, 3, self.right_color, self.left_color, False)
                            quick_game.run()
                            quick_game = Game_With_Set_Params(random.randint(6,7), random.randint(6,7), random.randint(min_sequ_len, 3), random.randint(min_num_targets, 2), min_row_space, min_col_space, 3, self.right_color, self.left_color, False)
                            quick_game.run()
                            quick_game = Game_With_Set_Params(random.randint(7,8), random.randint(7,8), random.randint(min_sequ_len, 3), random.randint(min_num_targets, 2), min_row_space, min_col_space, 3, self.right_color, self.left_color, False)
                            quick_game.run()

                        elif event.ui_element == mode_button:
                            self.mode_page()
                        elif event.ui_element == settings_button:
                            self.settings_page()
                        elif event.ui_element == help_button:
                            self.help_page()
                        elif event.ui_element == login_button:
                            self.login_page()
                        elif event.ui_element == quit_button:
                            running = False
                self.manager.process_events(event)
            self.manager.update(pygame.time.get_ticks() / 1000.0)
            self.screen.fill((0, 0, 0))
            self.manager.draw_ui(self.screen)
            pygame.display.update()
        pygame.quit()

    def back_to_menu(self):
        pygame.display.set_caption("Letter Puzzle")
        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height))
        self.menu_page()

    def back_to_settings_page(self):
        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height))
        self.settings_page()
    def mode_page(self):
        pygame.display.set_caption("Mode Select")
        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height))
        x = self.middle
        y = 150
        min_num_grids = 4
        max_num_grids = 32
        min_rows = 4
        max_rows = 10
        min_cols = 4
        max_cols = 12
        min_sequ_len = 1
        max_sequ_len = 4
        min_num_targets = 1
        max_num_targets = 5
        min_row_space= 1
        max_row_space = 3
        min_col_space = 1
        max_col_space = 5
        arrow_gap = 100
        label_width = 150


        back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.right, 10), (self.button_width, self.button_height)), text="Back", manager = self.manager)
        start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.screen_width-200, self.screen_height-100), (self.button_width, self.button_height)), text="Start", manager = self.manager)

        num_grids_decrease_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.middle-arrow_gap, y), (50, 50)), text="<", manager = self.manager)
        num_grids_increase_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.middle+arrow_gap, y), (50, 50)), text=">", manager = self.manager)
        num_grids_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((self.middle - 300, y), (label_width, 50)), text="Number of Grids", manager=self.manager)
        num_grids_textbox = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((self.middle, y), (100, 50)), html_text= str(min_rows), manager=self.manager)
        y += 100

        rows_decrease_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.middle-arrow_gap, y), (50, 50)), text="<", manager = self.manager)
        rows_increase_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.middle+arrow_gap, y), (50, 50)), text=">", manager = self.manager)
        rows_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((self.middle - 300, y), (label_width, 50)), text="Rows", manager= self.manager)
        rows_textbox = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((self.middle, y), (100, 50)), html_text= str(min_rows), manager= self.manager)
        y += 100
        cols_decrease_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.middle-arrow_gap, y), (50, 50)), text="<", manager = self.manager)
        cols_increase_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.middle+arrow_gap, y), (50, 50)), text=">", manager = self.manager)
        cols_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((self.middle - 300, y), (label_width, 50)), text="Columns", manager = self.manager)
        cols_textbox = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((self.middle, y), (100, 50)), html_text= str(min_cols), manager = self.manager)
        y += 100
        sequ_len_decrease_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.middle-arrow_gap, y), (50, 50)), text="<", manager = self.manager)
        sequ_len_increase_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.middle+arrow_gap, y), (50, 50)), text=">", manager = self.manager)
        sequ_len_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((self.middle - 300, y), (label_width, 50)), text="Sequence Length", manager=self.manager)
        sequ_len_textbox = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((self.middle, y), (100, 50)), html_text = str(min_sequ_len), manager=self.manager)
        y += 100
        num_targets_decrease_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.middle-arrow_gap, y), (50, 50)), text="<", manager = self.manager)
        num_targets_increase_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.middle+arrow_gap, y), (50, 50)), text=">", manager = self.manager)
        num_targets_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((self.middle - 300, y), (label_width, 50)), text="Number of Targets", manager = self.manager)
        num_targets_textbox = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((self.middle, y), (100, 50)), html_text= str(min_num_targets), manager= self.manager)
        y += 100
        row_space_decrease_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.middle-arrow_gap, y), (50, 50)), text="<", manager = self.manager)
        row_space_increase_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.middle+arrow_gap, y), (50, 50)), text=">", manager = self.manager)
        row_space_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((self.middle - 300, y), (label_width, 50)), text="Space Between Rows", manager=self.manager)
        row_space_textbox = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((self.middle, y), (100, 50)), html_text= str(min_row_space), manager=self.manager)
        y += 100
        col_space_decrease_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.middle-arrow_gap, y), (50, 50)), text="<", manager = self.manager)
        col_space_increase_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.middle+arrow_gap, y), (50, 50)), text=">", manager = self.manager)
        col_space_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((self.middle - 300, y), (label_width, 50)), text="Space Between Columns", manager=self.manager)
        col_space_textbox = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((self.middle, y), (100, 50)), html_text= str(min_col_space), manager=self.manager)

        clock = pygame.time.Clock()
        running = True

        new_game = Game_With_Set_Params(min_rows, min_cols, min_sequ_len, min_num_targets, min_row_space, min_col_space, min_num_grids, self.right_color, self.left_color, False)
        new_game.left_color = self.left_color
        new_game.right_color = self.right_color

        while running:
            time_delta = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == back_button:
                            self.back_to_menu()
                        elif event.ui_element == start_button:
                            new_game.run()

                        elif event.ui_element == num_grids_increase_button:
                            if int(num_grids_textbox.html_text) < max_num_grids:
                                new_game.num_grids = int(num_grids_textbox.html_text) + 4
                                print("the new grid number is ", new_game.num_grids)
                        elif event.ui_element == num_grids_decrease_button:
                            if int(num_grids_textbox.html_text) >= min_num_grids:
                                new_game.num_grids = int(num_grids_textbox.html_text) - 4

                        elif event.ui_element == rows_increase_button:
                            if int(rows_textbox.html_text) < max_rows:
                                new_game.rows = int(rows_textbox.html_text) + 1
                                print("the new row number is ", new_game.rows)
                        elif event.ui_element == rows_decrease_button:
                            if int(rows_textbox.html_text) >= min_rows:
                                new_game.rows = int(rows_textbox.html_text) - 1
                                print("the new row number is ", new_game.rows)

                        elif event.ui_element == cols_increase_button:
                            if int(cols_textbox.html_text) < max_cols:
                                new_game.cols = int(cols_textbox.html_text) + 1
                        elif event.ui_element == cols_decrease_button:
                            if int(cols_textbox.html_text) >= min_cols:
                                new_game.cols = int(cols_textbox.html_text) - 1
                            print("the new col number is ", new_game.cols)


                        elif event.ui_element == sequ_len_increase_button:
                            if int(sequ_len_textbox.html_text) < max_sequ_len:
                                new_game.sequ_len = int(sequ_len_textbox.html_text) + 1
                        elif event.ui_element == sequ_len_decrease_button:
                            if int(sequ_len_textbox.html_text) >= min_sequ_len:
                                new_game.sequ_len = int(sequ_len_textbox.html_text) - 1

                        elif event.ui_element == num_targets_increase_button:
                            if int(num_targets_textbox.html_text) < max_num_targets:
                                new_game.num_targets = int(num_targets_textbox.html_text) + 1
                        elif event.ui_element == num_targets_decrease_button:
                            if int(num_targets_textbox.html_text) >= min_num_targets:
                                new_game.num_targets = int(num_targets_textbox.html_text) - 1

                        elif event.ui_element == row_space_increase_button:
                            if int(row_space_textbox.html_text) < max_row_space:
                                new_game.row_space = int(row_space_textbox.html_text) + 1
                        elif event.ui_element == row_space_decrease_button:
                            if int(row_space_textbox.html_text) >= min_row_space:
                                new_game.row_space = int(row_space_textbox.html_text) - 1

                        elif event.ui_element == col_space_increase_button:
                            if int(col_space_textbox.html_text) < max_col_space:
                                new_game.col_space = int(col_space_textbox.html_text) + 1
                        elif event.ui_element == col_space_decrease_button:
                            if int(col_space_textbox.html_text) >= min_col_space:
                                new_game.col_space = int(col_space_textbox.html_text) - 1

                        num_grids_textbox.html_text = str(new_game.num_grids)
                        num_grids_textbox.rebuild()
                        rows_textbox.html_text = str(new_game.rows)
                        rows_textbox.rebuild()
                        cols_textbox.html_text = str(new_game.cols)
                        cols_textbox.rebuild()
                        sequ_len_textbox.html_text = str(new_game.sequ_len)
                        sequ_len_textbox.rebuild()
                        num_targets_textbox.html_text = str(new_game.num_targets)
                        num_targets_textbox.rebuild()
                        row_space_textbox.html_text = str(new_game.row_space)
                        row_space_textbox.rebuild()
                        col_space_textbox.html_text = str(new_game.col_space)
                        col_space_textbox.rebuild()

                self.manager.process_events(event)
            self.manager.update(time_delta)
            self.screen.fill((0, 0, 0))
            self.manager.draw_ui(self.screen)
            pygame.display.update()

    def color_picker_page(self, side):
        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height))
        background = pygame.Surface((self.screen_width, self.screen_height))
        background.fill((0,0,0))
        # Create back button
        x = self.right
        y = 10
        back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y),(self.button_width, self.button_height)),text="Cancel", manager=self.manager)
        x = x - self.button_width - 10
        save_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y),(self.button_width, self.button_height)),text="Save", manager=self.manager)

        # Create color picker button
        colour_picker_button = UIButton(relative_rect=pygame.Rect((self.middle, 100),(self.button_width, self.button_height)),text="Pick color", manager=self.manager)
        colour_picker = None
        current_colour = pygame.Color(0, 0, 0)
        print(current_colour)
        print(current_colour[0])
        if side == "right":
            current_colour = pygame.Color(self.right_color)
            self.selected_colour = current_colour
            # self.prev_right = current_colour
        if side == "left":
            current_colour = pygame.Color(self.left_color)
            self.selected_colour = current_colour
            # self.prev_left= current_colour
        picked_colour_surface = pygame.Surface((400, 400))
        picked_colour_surface.fill(current_colour)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                # Check for button clicks
                if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back_button:
                        self.back_to_settings_page()
                    if event.ui_element == colour_picker_button:
                        colour_picker = UIColourPickerDialog(pygame.Rect(260, 50, 420, 400),self.manager,window_title="Change Color...",initial_colour=current_colour)
                        colour_picker_button.disable()
                if event.type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED:
                    current_colour = event.colour
                    picked_colour_surface.fill(current_colour)
                    self.selected_colour = (current_colour[0],current_colour[1],current_colour[2])
                    print(self.selected_colour)
                if event.type == pygame_gui.UI_WINDOW_CLOSE:
                    colour_picker_button.enable()
                    colour_picker = None
                if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == save_button:
                    print("now here")
                    if side == "right":
                        self.right_color = self.selected_colour
                    if side == "left":
                        self.left_color = self.selected_colour

                    self.back_to_settings_page()
                self.manager.process_events(event)

            # Update UI
            self.manager.update(pygame.time.get_ticks() / 1000.0)
            self.screen.blit(background, (0, 0))
            self.screen.blit(picked_colour_surface, (200, 100))
            # screen.fill((0, 0, 0))
            self.manager.draw_ui(self.screen)
            pygame.display.update()

    def reset_colors(self):
        self.left_color = self.prev_left
        self.right_color = self.prev_right
    def settings_page(self):
        global left_color, right_color, right_clicked, left_clicked
        pygame.display.set_caption("Settings")
        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height))
        x = self.middle
        y = 150

        cancel_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.right, 10),(self.button_width, self.button_height)),
            text="Cancel",manager=self.manager)
        save_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.right-200, 10),(self.button_width, self.button_height)),
            text="Save",manager=self.manager)


        color = (255, 0, 0)

        # color picker:
        left_eye_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.middle - 200, 150), (100, 50)),text="Left Eye",manager=self.manager)

        right_eye_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.middle + 200, 150), (100, 50)),text="Right Eye",manager=self.manager)

        clock = pygame.time.Clock()
        running = True
        self.screen.fill((0, 0, 0))

        self.manager.draw_ui(self.screen)
        rect1 = pygame.draw.rect(self.screen, self.left_color, pygame.Rect(585, 150, 60, 60))
        rect2 = pygame.draw.rect(self.screen, self.right_color, pygame.Rect(700, 150, 60, 60))
        pygame.display.flip()
        pygame.display.update()

        while running:
            time_delta = clock.tick(60) / 1000
            rect1 = pygame.draw.rect(self.screen, self.left_color, pygame.Rect(585, 150, 60, 60))
            rect2 = pygame.draw.rect(self.screen, self.right_color, pygame.Rect(700, 150, 60, 60))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == cancel_button:
                            self.reset_colors()
                            # self.left_color = self.prev_color
                            # self.right_color = self.selected_colour
                            #
                            self.back_to_menu()
                        elif event.ui_element == cancel_button:
                            self.reset_colors()
                        elif event.ui_element == left_eye_button:
                            self.prev_left = self.left_color
                            self.color_picker_page("left")
                            self.left_color = self.selected_colour

                            # variable that equals current
                            # create rectangle = to the left_color array
                        elif event.ui_element == right_eye_button:
                            self.prev_left = self.left_color
                            self.color_picker_page("right")
                            self.right_color = self.selected_colour
                            print(self.right_color)


                            # create rectangle = to the right_color array
                        elif event.ui_element == save_button:

                            self.back_to_menu()

                self.manager.process_events(event)
            self.manager.update(time_delta)
            self.screen.fill((0, 0, 0))
            self.manager.draw_ui(self.screen)

            rect1 = pygame.draw.rect(self.screen, self.left_color, pygame.Rect(585, 150, 60, 60))
            rect2 = pygame.draw.rect(self.screen, self.right_color, pygame.Rect(700, 150, 60, 60))
            pygame.display.flip()

    def menu_loop(self, back_button, manager):
        running = True
        clock = pygame.time.Clock()
        while running:
            time_delta = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == back_button:
                            self.back_to_menu()
                manager.process_events(event)
            manager.update(time_delta)
            self.screen.fill((0, 0, 0))
            manager.draw_ui(self.screen)
            pygame.display.update()
        pygame.quit()

    def login_page(self):
        x = self.middle
        y = 200
        manager = pygame_gui.UIManager((self.screen_width, self.screen_height))

        username_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((x, y), (self.button_width, self.button_height)),
                                                           manager=self.manager)
        password_box = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((x, y + 100), (self.button_width, self.button_height)), manager=self.manager)

        submit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y + 200), (self.button_width, self.button_height)),
                                                     text="Submit", manager=manager)
        back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.right, 10), (self.button_width, self.button_height)),
                                                   text="Back", manager=self.manager)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == submit_button:
                            username = username_box.get_text()
                            password = password_box.get_text()
                            print(f"Login attempted with username '{username}' and password '{password}'")
                            logged_in = True
                            self.back_to_menu()
                        elif event.ui_element == back_button:
                            self.back_to_menu()
                manager.process_events(event)
            manager.update(pygame.time.get_ticks() / 1000.0)
            self.screen.fill((0, 0, 0))
            manager.draw_ui(self.screen)
            pygame.display.update()
        pygame.quit()

    def display_text(self, surface, text, pos, font):
        # can write on mutiple lines, good for long sentences/descriptions
        collection = [word.split(' ') for word in text.splitlines()]
        space = font.size(' ')[0]
        x, y = pos
        for lines in collection:
            for words in lines:
                word_surface = font.render(words, True, (255,255,255))
                word_width, word_height = word_surface.get_size()
                if x + word_width >= 1240:
                    x = pos[0]
                    y += word_height
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]
            y += word_height

    def help_page(self):
        pygame.display.set_caption("Help Page")
        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height))
        back_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (self.right, 10),
                (self.button_width, self.button_height)),
            text="Back",
            manager=self.manager)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == back_button:
                            self.back_to_menu()
                self.manager.process_events(event)
            self.manager.update(pygame.time.get_ticks() / 1000.0)
            text = "Background:"
            text1 = "The Anaglyph Letter Puzzle Game is a visual puzzle that challenges you,the player,to identify a single letter that is different from the others in a grid of identical letters."
            text2 = "How to Play:"
            text3 = "To play, you must examine the grid closely and identify the unique letter, which may be a different size, color, or orientation than the other letters in the grid."
            text4 = "Mode Select:"
            text5 = "In Mode Select, the level of difficulty can be altered to your liking. Use the buttons to decrease or increase the level of your grid."
            text6 = "Settings:"
            text7 = "The are different parameters that you change to personalize your game experience. You can change the time allotted, the colors for the grid, and size of the characters."
            text8 = "Login:"
            text9 = "To track your progress as a patient, enter your username and password. If you are a healthcare professional, please enter your username and work pin number."
            font = pygame.font.SysFont(None, 26)
            self.screen.fill((0, 0, 0))
            self.manager.draw_ui(self.screen)
            self.display_text(self.screen, text, (350, 45), font)
            # the space between title and expl: 40 , from past exp to new title: 95
            self.display_text(self.screen, text1, (350, 85), font)
            self.display_text(self.screen, text2, (350, 180), font)
            self.display_text(self.screen, text3, (350, 220), font)
            self.display_text(self.screen, text4, (350, 315), font)
            self.display_text(self.screen, text5, (350, 355), font)
            self.display_text(self.screen, text6, (350, 450), font)
            self.display_text(self.screen, text7, (350, 490), font)
            self.display_text(self.screen, text8, (350, 585), font)
            self.display_text(self.screen, text9, (350, 625), font)

            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    home = Home()
    home.menu_page()

