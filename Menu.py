import sys
import textwrap

import pygame
import pygame_gui
from pygame_gui.elements import UIButton
from pygame_gui.windows import UIColourPickerDialog
import random as r
from Game import Game





class Menu:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    
    '''
        The Menu class's purpose is to provide the menu page, allowing users to naviagate gameplay options in the game. Unbeknownst to the player, the menu class also doubles 
        as a space holding each entire function for all the menu options. Those menu options being: Mode_Page, Color_picker_page, Settings_Page, Login_Page, and lastly Help_Page.
        It has 2 global variables, BlACK and WHITE - which are used to label RGB colors.
    '''

    def __init__(self):
        
        
        '''
            The “_init_” constructor's purpose is to initialize the necessary variables needed for the pygame windows as well as grid variables that are used 
            in the game, and that would also be affected by  the Mode Select Page and Settings Page. 
        '''

        pygame.init()
        self.button_width, self.button_height = 200, 50
        self.info = pygame.display.Info()
        self.screen_width = self.info.current_w
        self.screen_height = self.info.current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Anaglyph Letter Puzzle")
        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height))
        self.middle = (self.screen_width - self.button_width) / 2
        self.right = self.screen_width - self.button_width - 10
        self.font = pygame.font.SysFont(None, 100)
        self.right_color = (255, 0, 0)
        self.left_color = (0, 0, 255)
        self.selected_colour = (255, 255, 255)
        self.prev_left = self.left_color
        self.prev_right = self.right_color
        self.min_num_grids, self.max_num_grids = 4, 32
        self.min_rows, self.max_rows = 5, 12
        self.min_cols, self.max_cols = 5, 12
        self.min_sequ_len, self.max_sequ_len = 1, 4
        self.min_num_targets, self.max_num_targets = 1, 5
        self.min_row_space, self.max_row_space = 1, 3
        self.min_col_space, self.max_col_space = 2, 5
        self.label_width = 150
        self.gap = 10
        self.arrow_width = self.textbox_width = 50
        self.label_width = 200
        self.widget_height = 50

    def create_button(self, pos, size, text):
        '''
            “Create_Button” function has the objective of producing a functional
            button that is proportionally the same size Takes in 4 parameters returns variable “button”  
        '''
        button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(pos, size), text=text, manager=self.manager)
        return button

    def render_back_button(self):
        
        '''
            “Render_back_button” is one of the methods that is very similar to the Create_button(). Doing as the name implies, it creates as a “back” button that when added functionality,
            will return you back to the menu page Takes in 1 parameter, returns a variable called “back_button” 
        '''
        back_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.right, 10), (self.button_width, self.button_height)),
            text="Back", manager=self.manager)
        return back_button

    def menu_page(self):
        
        '''
            The “Menu_Page” method is a large as it encompases all the buttons and functionality for the front end of the menu page.
            Showing each button for the options and making them have a purpose (which would be leading to their designated part of the game). Takes in 1 parameter and does not return anything.  
        '''
        x = self.middle
        y = 200
        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height))

        title_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((self.middle, 100),
                      (self.button_width, self.button_height)), text="Anaglyph Letter Puzzle", manager=self.manager)

        quick_play_button = self.create_button((x, y), (self.button_width, self.button_height), "Quick Play")
        mode_button = self.create_button((x, y + 100), (self.button_width, self.button_height), "Mode Select")
        settings_button = self.create_button((x, y + 200), (self.button_width, self.button_height), "Settings")
        help_button = self.create_button((x, y + 300), (self.button_width, self.button_height), "Help")
        login_button = self.create_button((x, y + 400), (self.button_width, self.button_height), "Login")
        quit_button = self.create_button((x, y + 500), (self.button_width, self.button_height), "Quit")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == quick_play_button:
                            quick_game = Game(self.min_rows, self.min_cols, self.min_sequ_len, self.min_num_targets,
                                              self.min_row_space, self.min_col_space, self.min_num_grids,
                                              self.right_color, self.left_color, True)
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

    def create_widget_group(self, x, y, label_text, initial_value):
        
        '''
            “Create_widget_group” is another method whose aim is to create buttons, but these specific buttons are for a special feature. These are located in the mode_select page, 
            and these will be used by the player to customize their game play experience. It has increase and decrease buttons, textboxes to show the current number, and labels to indicate what 
            each section is for. Unlike Menu_page, this takes in much more parameters, 5 to be exact. And in return, it gives the system the buttons, labels, and textboxes. 
        '''
        label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((x, y), (self.label_width, self.widget_height)), text=label_text,
            manager=self.manager)
        x += self.label_width + self.gap
        decrease_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((x, y), (self.arrow_width, self.widget_height)), text="<", manager=self.manager)
        x += self.arrow_width + self.gap
        textbox = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((x, y), (50, self.widget_height)), html_text=str(initial_value),
            manager=self.manager)
        x += self.textbox_width + self.gap
        increase_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((x, y), (self.arrow_width, self.widget_height)), text=">", manager=self.manager)
        return decrease_button, increase_button, label, textbox

    def mode_page(self):
        
        '''
            “mode_page” uses the variables returned from create_widget_group to provide the user with numerous
            options that they can select to get their preferable game experience. The amount of rows, grids, columns,
            space, targets, and even length of the sequences themselves are all sugject to change if the user wants to.
            This method in particular will show the user the updated numbers they have depending on if they clicked decrease or increase,
            and will ultimately send it to the game class where the variables chosen here will be updated in there. Only takes 1 param. Does not return anything.  
        '''
        pygame.display.set_caption("Mode Select")
        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height))
        x = self.middle - (self.label_width + (self.gap * 3) + (self.arrow_width * 2)) // 2
        y = 100
        back_button = self.render_back_button()
        start_button = self.create_button((self.right - self.button_width-self.gap, 10), (self.button_width, self.button_height), "Start")

        displacement = 100
        num_grids_decrease_button, num_grids_increase_button, num_grids_label, num_grids_textbox = \
            self.create_widget_group(x, y, "Number of Grids", self.min_num_grids)
        rows_decrease_button, rows_increase_button, rows_label, rows_textbox = \
            self.create_widget_group(x, y + displacement,"Number of Rows", self.min_rows)
        cols_decrease_button, cols_increase_button, cols_label, cols_textbox = \
            self.create_widget_group(x, y + displacement*2, "Number of Columns", self.min_cols)
        sequ_len_decrease_button, sequ_len_increase_button, sequ_len_label, sequ_len_textbox = \
            self.create_widget_group(x, y + displacement*3, "Sequence Length", self.min_sequ_len)
        num_targets_decrease_button, num_targets_increase_button, num_targets_label, num_targets_textbox = \
            self.create_widget_group(x, y + displacement * 4, "Number of Targets", self.min_num_targets)
        row_space_decrease_button, row_space_increase_button, row_space_label, row_space_textbox = \
            self.create_widget_group(x, y + displacement * 5, "Space Between Rows", self.min_row_space)
        col_space_decrease_button, col_space_increase_button, col_space_label, col_space_textbox = \
            self.create_widget_group(x, y + displacement * 6, "Space Between Columns", self.min_col_space)

        new_game = Game(self.min_rows, self.min_cols, self.min_sequ_len, self.min_num_targets, self.min_row_space,
                        self.min_col_space, self.min_num_grids, self.right_color, self.left_color, False)
        # maps UI elements to their corresponding attributes in new_game
        ui_element_to_attribute = {
            num_grids_increase_button: ('num_grids', 4, self.max_num_grids),
            num_grids_decrease_button: ('num_grids', -4, self.min_num_grids),
            rows_increase_button: ('rows', 1, self.max_rows),
            rows_decrease_button: ('rows', -1, self.min_rows),
            cols_increase_button: ('cols', 1, self.max_cols),
            cols_decrease_button: ('cols', -1, self.min_cols),
            sequ_len_increase_button: ('sequ_len', 1, self.max_sequ_len),
            sequ_len_decrease_button: ('sequ_len', -1, self.min_sequ_len),
            num_targets_increase_button: ('num_targets', 1, self.max_num_targets),
            num_targets_decrease_button: ('num_targets', -1, self.min_num_targets),
            row_space_increase_button: ('row_space', 1, self.max_row_space),
            row_space_decrease_button: ('row_space', -1, self.min_row_space),
            col_space_increase_button: ('col_space', 1, self.max_col_space),
            col_space_decrease_button: ('col_space', -1, self.min_col_space)
        }
        textboxes = {"num_grids": num_grids_textbox, "rows": rows_textbox, "cols": cols_textbox,
                     "sequ_len": sequ_len_textbox, "num_targets": num_targets_textbox, "row_space": row_space_textbox,
                     "col_space": col_space_textbox}
        clock = pygame.time.Clock()
        running = True
        while running:
            time_delta = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                elif event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == back_button:
                            self.menu_page()
                        elif event.ui_element == start_button:
                            new_game.run()

                        else:
                            # Check if the event's ui element is in the dictionary
                            if event.ui_element in ui_element_to_attribute:
                                # Get the corresponding attribute and update it in new_game
                                attr, val, limit = ui_element_to_attribute[event.ui_element]
                                new_val = int(getattr(new_game, attr)) + val
                                if limit >= new_val >= 0:
                                    setattr(new_game, attr, new_val)
                                    print(f"the new {attr} number is {new_val}")

                        for key, textbox in textboxes.items():
                            value = getattr(new_game, key)
                            textbox.html_text = str(value)
                            textbox.rebuild()

                self.manager.process_events(event)
            self.manager.update(time_delta)
            self.screen.fill((0, 0, 0))
            self.manager.draw_ui(self.screen)
            pygame.display.update()

    def color_picker_page(self, side):
        
        '''
            “color_picker_page” creates a new window that contains the color picker feature that players can choose to use. When on the page, a color
            selecting dialog box is present, and allows for the user to pick any color they want- and promptly save it once finished. Once this chosen
            color is saved, it will show up on the settings_page and will be displayed on either the left or right eye boxes.  It's purpose is to update
            the colors used for the characters in the game.It does not return anything, and it takes in 2 parameters.  
        '''
        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height))
        background = pygame.Surface((self.screen_width, self.screen_height))
        background.fill((0, 0, 0))

        x = self.right
        y = 10

        cancel_button = self.create_button((self.right, 10), (self.button_width, self.button_height), "Cancel")
        save_button = self.create_button((self.right - self.button_width-self.gap, 10), (self.button_width, self.button_height), "Save")
        # Create color picker button
        colour_picker_button = self.create_button((self.middle, 100), (self.button_width, self.button_height), "Pick color")

        colour_picker = None
        current_colour = pygame.Color(0, 0, 0)

        if side == "right":
            current_colour = pygame.Color(self.right_color)
            self.selected_colour = current_colour
        if side == "left":
            current_colour = pygame.Color(self.left_color)
            self.selected_colour = current_colour

        picked_colour_surface = pygame.Surface((400, 400))
        picked_colour_surface.fill(current_colour)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                # Check for button clicks
                if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == cancel_button:
                        self.settings_page()
                    if event.ui_element == colour_picker_button:
                        colour_picker = UIColourPickerDialog(pygame.Rect(260, 50, 420, 400), self.manager,
                                                             window_title="Change Color...",
                                                             initial_colour=current_colour)
                        colour_picker_button.disable()

                if event.type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED:
                    current_colour = event.colour
                    picked_colour_surface.fill(current_colour)
                    self.selected_colour = (current_colour[0], current_colour[1], current_colour[2])
                    print(self.selected_colour)
                if event.type == pygame_gui.UI_WINDOW_CLOSE:
                    colour_picker_button.enable()
                    colour_picker = None
                if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == save_button:
                    if side == "right":
                        self.right_color = self.selected_colour
                    if side == "left":
                        self.left_color = self.selected_colour

                    self.settings_page()
                self.manager.process_events(event)

            # Update UI
            self.manager.update(pygame.time.get_ticks() / 1000.0)
            self.screen.blit(background, (0, 0))
            self.screen.blit(picked_colour_surface, (200, 100))
            self.manager.draw_ui(self.screen)
            pygame.display.update()

    def reset_colors(self):
        
        '''
            “reset_colors” is a smaller function aimed at reseting the colors chosen by the player, and bringing back the original designated colors for the game.
            The colors in specific are what help make it an anaglyph. Only takes in one parameter, and it does not return anything. 
        '''
        self.left_color = self.prev_left
        self.right_color = self.prev_right

    def settings_page(self):
        
        '''
            The “settings_page” is similar to the mode selct page 
            in that they are both menu options that allow for the user to directly impact the grid they use to play.
            Where the two pages differ, is that one is for
            specifcs on the grid such as space and column amounts, the settings page includes 
            the color_picker and would also include other features. Takes in one parameter and returns nothing.  
        '''
        pygame.display.set_caption("Settings")
        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height))
        color_width = color_height = self.button_width
        label_gap = 10
        font = pygame.font.SysFont(None, 26)
        directions = ["With your anaglyph glasses on, cover one eye at a time and adjust the color. You should not "
                      "be able to see the color preview box against the background. Once you have calibrated "
                      "the colors for each eye, you are ready to play!"]

        cancel_button = self.create_button((self.right, 10), (self.button_width, self.button_height), "Cancel")
        save_button = self.create_button((self.right - self.button_width-self.gap, 10), (self.button_width, self.button_height), "Save")

        rect_y = 300
        button_y = rect_y + color_height + label_gap
        left_x, right_x = self.middle - color_width - self.gap, self.middle + color_width + self.gap
        left_eye_button = self.create_button((left_x, button_y), (self.button_width, self.button_height), "Left Eye")
        right_eye_button = self.create_button((right_x, button_y), (self.button_width, self.button_height),"Right Eye")

        clock = pygame.time.Clock()
        running = True

        while running:
            time_delta = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                elif event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == cancel_button:
                            self.reset_colors()
                            self.menu_page()

                        elif event.ui_element == cancel_button:
                            self.reset_colors()

                        elif event.ui_element == left_eye_button:
                            self.prev_left = self.left_color
                            self.color_picker_page("left")
                            self.left_color = self.selected_colour

                        elif event.ui_element == right_eye_button:
                            self.prev_left = self.left_color
                            self.color_picker_page("right")
                            self.right_color = self.selected_colour

                        elif event.ui_element == save_button:
                            self.menu_page()

                self.manager.process_events(event)
            self.manager.update(time_delta)
            self.screen.fill((0, 0, 0))
            self.display_text(self.screen, directions, (100, 100), font)
            self.manager.draw_ui(self.screen)
            left_rect = pygame.draw.rect(self.screen, self.left_color,
                                         pygame.Rect(left_x, rect_y, color_width, color_height))
            right_rect = pygame.draw.rect(self.screen, self.right_color,
                                          pygame.Rect(right_x, rect_y, color_width, color_height))

            pygame.display.update()

    def login_page(self):
        
        '''
            “login_page” is an important method because this is what connects the game to the database, and ultimately the
            website components of the system. The login page has a simple window, showing a back button,
            textboxes to enter username and password. Taking 1 parameter, this function also does not return anything.  
        '''
        pygame.display.set_caption("Login")
        x = self.middle
        y = 200
        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height))

        username_box = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((x, y), (self.button_width, self.button_height)),
            manager=self.manager)
        password_box = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((x, y + 100), (self.button_width, self.button_height)), manager=self.manager)

        submit_button = self.create_button((x, y + 200), (self.button_width, self.button_height), "Submit")

        back_button = self.render_back_button()
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
                            self.menu_page()
                        elif event.ui_element == back_button:
                            self.menu_page()
                self.manager.process_events(event)
            self.manager.update(pygame.time.get_ticks() / 1000.0)
            self.screen.fill((0, 0, 0))
            self.manager.draw_ui(self.screen)
            pygame.display.update()
        pygame.quit()

    def display_text(self, surface, texts, pos, font):
        
        '''
            The “display_text” method has the specifc purpose of printing lines in paragraph form. It is specifically 
            used in the help_page method.  Takes in 5 parameters, returns None.  
        '''
        global word_height
        x, y = pos
        for text in texts:
            # can write on mutiple lines, good for long sentences/descriptions
            collection = [word.split(' ') for word in text.splitlines()]
            space = font.size(' ')[0]
            for lines in collection:
                for words in lines:
                    word_surface = font.render(words, True, (255,255,255))
                    word_width, word_height = word_surface.get_size()
                    if x + word_width >= surface.get_width()-pos[0]:
                        x = pos[0]
                        y += word_height
                    surface.blit(word_surface, (x, y))
                    x += word_width + space
                x = pos[0]
                y += word_height
            y += word_height

    def help_page(self):
        
        '''
            Help_Page() is a simple window that explains the use of each menu option,
            the goal of the game, and it's purpose. No functions outside of calling the back button. 1 Parameter, nothing returned.  
        '''
        pygame.display.set_caption("Help Page")
        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height))
        back_button = self.render_back_button()

        font = pygame.font.SysFont(None, 26)
        texts = "Background:", \
                "The Anaglyph Letter Puzzle Game is a visual puzzle that challenges you,the player,to identify a target sequence among a grid of similar looking sequences.", \
                "How to Play:", \
                "To play, you must examine the grid closely to identify the target sequence(s). Once all target sequences are found and clicked, you will move on to the next grid. The game ends when all grids have been completed or you exit the game by pressing the escape key.", \
                "Mode Select:", \
                "Mode select allows you to adjust the size of the grid, length of sequence, number of targets to find, and spacing between the rows and columns of the grid. Use the arrow buttons to adjust grid settings, then click start to begin playing.", \
                "Settings:", \
                "With your anaglyph glasses on, cover one eye at a time and adjust the color. You should not be able to see the color preview box against the background.", \
                "Login:", \
                "To track your progress as a patient, enter your username and password. If you are a healthcare professional, please enter your username and work pin number."

        clock = pygame.time.Clock()
        running = True

        while running:
            time_delta = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == back_button:
                            self.menu_page()
                self.manager.process_events(event)

            self.manager.update(time_delta)
            self.screen.fill((0, 0, 0))
            self.display_text(self.screen, texts, (100, 100), font)
            self.manager.draw_ui(self.screen)
            pygame.display.update()


if __name__ == "__main__":
    menu = Menu()
    menu.menu_page()
