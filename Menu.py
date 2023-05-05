import pygame
import pygame_gui
from pygame_gui.elements import UIButton
from pygame_gui.windows import UIColourPickerDialog
import random as r
from Game import Game

class Menu:

    def __init__(self):

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
        self.right_color = (255, 0, 0)
        self.left_color = (0, 0, 255)
        self.selected_colour = (255, 255, 255)
        self.prev_left = self.left_color
        self.prev_right = self.right_color
        self.min_num_grids, self.max_num_grids = 4, 32
        self.min_rows, self.max_rows = 5, 15
        self.min_cols, self.max_cols = 5, 15
        self.min_sequ_len, self.max_sequ_len = 1, 3
        self.min_num_targets, self.max_num_targets = 1, 5
        self.label_width = 150
        self.gap = 10
        self.arrow_width = self.textbox_width = 50
        self.label_width = 200
        self.widget_height = 50

    def create_button(self, pos, size, text):
        button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(pos, size), text=text, manager=self.manager)
        return button

    def render_back_button(self):
        back_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.right, 10), (self.button_width, self.button_height)),
            text="Back", manager=self.manager)
        return back_button

    def menu_page(self):
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
                                              self.min_num_grids, self.right_color, self.left_color, True)
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

        new_game = Game(self.min_rows, self.min_cols, self.min_sequ_len, self.min_num_targets, self.min_num_grids, self.right_color, self.left_color, False)
        # maps UI elements to their corresponding attributes in new_game
        ui_element_to_attribute = {
            num_grids_increase_button: ('num_grids', 4, self.min_num_grids, self.max_num_grids),
            num_grids_decrease_button: ('num_grids', -4, self.min_num_grids, self.max_num_grids),
            rows_increase_button: ('rows', 1, self.min_rows, self.max_rows),
            rows_decrease_button: ('rows', -1, self.min_rows, self.max_rows),
            cols_increase_button: ('cols', 1, self.min_cols, self.max_cols),
            cols_decrease_button: ('cols', -1, self.min_cols, self.max_cols),
            sequ_len_increase_button: ('sequ_len', 1, self.min_sequ_len, self.max_sequ_len),
            sequ_len_decrease_button: ('sequ_len', -1, self.min_sequ_len, self.max_sequ_len),
            num_targets_increase_button: ('num_targets', 1, self.min_num_targets, self.max_num_targets),
            num_targets_decrease_button: ('num_targets', -1, self.min_num_targets, self.max_num_targets),
        }

        textboxes = {"num_grids": num_grids_textbox, "rows": rows_textbox, "cols": cols_textbox,
                     "sequ_len": sequ_len_textbox, "num_targets": num_targets_textbox}
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
                            if event.ui_element in ui_element_to_attribute:
                                # Get the corresponding attribute and update it in new_game
                                attr, val, min_val, max_val = ui_element_to_attribute[event.ui_element]
                                current_val = getattr(new_game, attr)
                                new_val = current_val + val
                                if min_val <= new_val <= max_val:
                                    setattr(new_game, attr, new_val)
                                    print(f"The new {attr} number is {new_val}")
                                else:
                                    print(f"Error: {attr} must be between {min_val} and {max_val}")

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
        self.left_color = self.prev_left
        self.right_color = self.prev_right

    def settings_page(self):
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
            left_rect = pygame.draw.rect(self.screen, self.left_color, pygame.Rect(left_x, rect_y, color_width, color_height))
            right_rect = pygame.draw.rect(self.screen, self.right_color, pygame.Rect(right_x, rect_y, color_width, color_height))
            pygame.display.update()

    def login_page(self):
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
