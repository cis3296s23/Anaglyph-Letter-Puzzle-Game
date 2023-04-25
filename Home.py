import pygame
import pygame_gui
from pygame_gui.elements import UIButton

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
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Anaglyph Letter Puzzle")
        self.manager = pygame_gui.UIManager((screen_width, screen_height))
        self.middle = (screen_width - button_width) / 2
        self.right = screen_width - button_width - 10
        self.top = 10
        self.font = pygame.font.SysFont(None, 100)

    def menu_page(self):
        x = self.middle
        y = 200
        self.manager = pygame_gui.UIManager((self.screen.get_width(), self.screen.get_height()))

        title_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((self.middle, 100), (200, 50)), text="Anaglyph Letter Puzzle", manager=self.manager)
        quick_play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y), (200, 50)), text="Quick Play", manager=self.manager)
        mode_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y + 100), (200, 50)), text="Mode Select", manager=self.manager)
        settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y + 200), (200, 50)), text="Settings", manager=self.manager)
        help_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y + 300), (200, 50)), text="Help", manager=self.manager)
        login_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y + 400), (200, 50)), text="Login", manager=self.manager)
        quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y + 500), (200, 50)), text="Quit", manager=self.manager)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == quick_play_button:
                            Game.run()
                            if Game.target_count == 0:
                                self.back_to_menu()
                        elif event.ui_element == mode_button:
                            self.mode_page()
                        elif event.ui_element == settings_button:
                            self.redirect_proof_of_concpt_page()
                        elif event.ui_element == help_button:
                            self.redirect_proof_of_concpt_page()
                        elif event.ui_element == login_button:
                            login_page()
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

def menu_page():
    global manager
    x = middle
    y = 200
    manager = pygame_gui.UIManager((screen_width, screen_height))

    title_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((middle, 100), (button_width, button_height)), text="Anaglyph Letter Puzzle", manager=manager)

    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y), (button_width, button_height)), text="Quick Play", manager=manager)
    mode_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y + 100), (button_width, button_height)), text="Mode Select", manager=manager)
    settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y + 200), (button_width, button_height)), text="Settings", manager=manager)
    help_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y + 300), (button_width, button_height)), text="Help", manager=manager)
    login_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y + 400), (button_width, button_height)), text="Login", manager=manager)
    quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y + 500), (button_width, button_height)), text="Quit", manager=manager)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == start_button:
                        Game.main()
                        if Game.target_count ==0:
                            back_to_menu()
                    elif event.ui_element == mode_button:
                        mode_page()
                    elif event.ui_element == settings_button:
                        settings_page()
                    elif event.ui_element == help_button:
                        redirect_proof_of_concpt_page()
                    elif event.ui_element == login_button:
                        login_page()
                    elif event.ui_element == quit_button:
                        running = False
            manager.process_events(event)
        manager.update(pygame.time.get_ticks() / 1000.0)
        screen.fill((0, 0, 0))
        manager.draw_ui(screen)
        pygame.display.update()
    pygame.quit()

def back_to_menu():
    global manager
    pygame.display.set_caption("Letter Puzzle")
    manager = pygame_gui.UIManager((screen_width, screen_height))
    menu_page()

def mode_page():
    global manager
    pygame.display.set_caption("Mode Select")
    manager = pygame_gui.UIManager((screen_width, screen_height))
    x = middle
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


    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((right, 10), (button_width, button_height)), text="Back", manager = manager)
    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((screen_width-200, screen_height-100), (button_width, button_height)), text="Start", manager = manager)

    num_grids_decrease_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((middle-arrow_gap, y), (50, 50)), text="<", manager = manager)
    num_grids_increase_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((middle+arrow_gap, y), (50, 50)), text=">", manager = manager)
    num_grids_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((middle - 300, y), (label_width, 50)), text="Number of Grids", manager=manager)
    num_grids_textbox = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((middle, y), (100, 50)), html_text= str(min_rows), manager=manager)
    y += 100

    rows_decrease_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((middle-arrow_gap, y), (50, 50)), text="<", manager = manager)
    rows_increase_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((middle+arrow_gap, y), (50, 50)), text=">", manager = manager)
    rows_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((middle - 300, y), (label_width, 50)), text="Rows", manager=manager)
    rows_textbox = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((middle, y), (100, 50)), html_text= str(min_rows), manager=manager)
    y += 100
    cols_decrease_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((middle-arrow_gap, y), (50, 50)), text="<", manager = manager)
    cols_increase_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((middle+arrow_gap, y), (50, 50)), text=">", manager = manager)
    cols_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((middle - 300, y), (label_width, 50)), text="Columns", manager=manager)
    cols_textbox = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((middle, y), (100, 50)), html_text= str(min_cols), manager=manager)
    y += 100
    sequ_len_decrease_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((middle-arrow_gap, y), (50, 50)), text="<", manager = manager)
    sequ_len_increase_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((middle+arrow_gap, y), (50, 50)), text=">", manager = manager)
    sequ_len_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((middle - 300, y), (label_width, 50)), text="Sequence Length", manager=manager)
    sequ_len_textbox = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((middle, y), (100, 50)), html_text = str(min_sequ_len), manager=manager)
    y += 100
    num_targets_decrease_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((middle-arrow_gap, y), (50, 50)), text="<", manager = manager)
    num_targets_increase_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((middle+arrow_gap, y), (50, 50)), text=">", manager = manager)
    num_targets_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((middle - 300, y), (label_width, 50)), text="Number of Targets", manager=manager)
    num_targets_textbox = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((middle, y), (100, 50)), html_text= str(min_num_targets), manager=manager)
    y += 100
    row_space_decrease_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((middle-arrow_gap, y), (50, 50)), text="<", manager = manager)
    row_space_increase_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((middle+arrow_gap, y), (50, 50)), text=">", manager = manager)
    row_space_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((middle - 300, y), (label_width, 50)), text="Space Between Rows", manager=manager)
    row_space_textbox = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((middle, y), (100, 50)), html_text= str(min_row_space), manager=manager)
    y += 100
    col_space_decrease_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((middle-arrow_gap, y), (50, 50)), text="<", manager = manager)
    col_space_increase_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((middle+arrow_gap, y), (50, 50)), text=">", manager = manager)
    col_space_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((middle - 300, y), (label_width, 50)), text="Space Between Columns", manager=manager)
    col_space_textbox = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((middle, y), (100, 50)), html_text= str(min_col_space), manager=manager)

    clock = pygame.time.Clock()
    running = True


    new_game = Game_With_Set_Params(min_rows, min_cols, min_sequ_len, min_num_targets, min_row_space, min_col_space, min_num_grids)

    while running:
        time_delta = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back_button:
                        back_to_menu()
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

            manager.process_events(event)
        manager.update(time_delta)
        screen.fill((0, 0, 0))
        manager.draw_ui(screen)
        pygame.display.update()


def color_picker_page():
    global manager, selected_colour
    manager = pygame_gui.UIManager((screen_width, screen_height))
    background = pygame.Surface((screen_width, screen_height))
    background.fill("#000000")
    # Create back button
    back_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (right, 10),
            (button_width, button_height)),
        text="Back",
        manager=manager)

    # Create color picker button
    colour_picker_button = UIButton(
        relative_rect=pygame.Rect(
            (middle, 100),
            (button_width, button_height)),
        text="Pick color",
        manager=manager)

    colour_picker = None
    current_colour = pygame.Color(255, 191, 0)
    picked_colour_surface = pygame.Surface((400, 400))
    picked_colour_surface.fill(current_colour)

    okay_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((middle, screen_height - 200), (button_width, button_height)),
        text="Okay",
        manager=manager)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Check for button clicks
            if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                # if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                # if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == colour_picker_button:
                if event.ui_element == back_button:
                    back_to_menu()
                if event.ui_element == colour_picker_button:
                    colour_picker = UIColourPickerDialog(pygame.Rect(260, 50, 420, 400),
                                                         manager,
                                                         window_title="Change Color...",
                                                         initial_colour=current_colour)

                    colour_picker_button.disable()
            if event.type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED:
                current_colour = event.colour
                picked_colour_surface.fill(current_colour)
                selected_colour = current_colour
            if event.type == pygame_gui.UI_WINDOW_CLOSE:
                colour_picker_button.enable()
                colour_picker = None
            if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == okay_button:
                print("now here")
                # redirect_proof_of_concpt_page()
                back_to_menu()

            manager.process_events(event)

        # Update UI
        manager.update(pygame.time.get_ticks() / 1000.0)
        screen.blit(background, (0, 0))
        screen.blit(picked_colour_surface, (200, 100))
        # screen.fill((0, 0, 0))
        manager.draw_ui(screen)
        pygame.display.update()

    return selected_colour
def display_text(surface, text, pos, font, color):
    collection = [word.split(' ') for word in text.splitlines() ]
    space = font.size(' ')[0]
    x,y = pos
    for lines in collection:
        for words in lines:
            word_surface = font.render(words, True, color)
            word_width , word_height = word_surface.get_size()
            if x + word_width >= 800:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x,y))
            x += word_width + space
        x = pos[0]
        y += word_height
def menu_loop(back_button, manager):
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
                        back_to_menu()
            manager.process_events(event)
        manager.update(time_delta)
        screen.fill((0, 0, 0))
        manager.draw_ui(screen)
        pygame.display.update()
    pygame.quit()

def login_page():
    global manager
    x = middle
    y = 200
    manager = pygame_gui.UIManager((screen_width, screen_height))

    username_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((x, y), (button_width, button_height)),
                                                       manager=manager)
    password_box = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((x, y + 100), (button_width, button_height)), manager=manager)

    submit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y + 200), (button_width, button_height)),
                                                 text="Submit", manager=manager)
    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((right, 10), (button_width, button_height)),
                                               text="Back", manager=manager)
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
                        back_to_menu()
                    elif event.ui_element == back_button:
                        back_to_menu()
            manager.process_events(event)
        manager.update(pygame.time.get_ticks() / 1000.0)
        screen.fill((0, 0, 0))
        manager.draw_ui(screen)
        pygame.display.update()
    pygame.quit()


def settings_page():
    global manager
    x = middle
    y = 200
    manager = pygame_gui.UIManager((screen_width, screen_height))
    back_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (right, 10),
            (button_width, button_height)),
        text="Back",
        manager=manager)
    F1_text = "Highlight Feature"
    toggle_button_on = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (x, y),
            (button_width, button_height)),
        text="ON",
        manager=manager)
    toggle_button_off = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (x, y),
            (button_width, button_height)),
        text="OFF",
        manager=manager)
    toggle_button_off.hide()
    F2_text = "Letter Reversal"
    toggle_button_on2 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (x, y + 150),
            (button_width, button_height)),
        text="ON",
        manager=manager)
    toggle_button_off2 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (x, y + 150),
            (button_width, button_height)),
        text="OFF",
        manager=manager)
    toggle_button_off2.hide()
    F3_text = "Timer"
    toggle_button_on3 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (x, y + 300),
            (button_width, button_height)),
        text="ON",
        manager=manager)
    toggle_button_off3 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (x, y + 300),
            (button_width, button_height)),
        text="OFF",
        manager=manager)
    toggle_button_off3.hide()
    running = True
    display_text(screen, F1_text, (middle, 80), font, 'gray')
    display_text(screen, F2_text, (middle, 140), font, 'gray')
    display_text(screen, F3_text, (middle, 280), font, 'gray')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back_button:
                        back_to_menu()
                    elif event.ui_element == toggle_button_on:
                        toggle_button_on.hide()
                        toggle_button_off.show()
                    elif event.ui_element == toggle_button_off:
                        toggle_button_off.hide()
                        toggle_button_on.show()
                    elif event.ui_element == toggle_button_on2:
                        toggle_button_on2.hide()
                        toggle_button_off2.show()
                    elif event.ui_element == toggle_button_off2:
                        toggle_button_off2.hide()
                        toggle_button_on2.show()
                    elif event.ui_element == toggle_button_on3:
                        toggle_button_on3.hide()
                        toggle_button_off3.show()
                    elif event.ui_element == toggle_button_off3:
                        toggle_button_off3.hide()
                        toggle_button_on3.show()
            manager.process_events(event)
        manager.update(pygame.time.get_ticks() / 1000.0)
        screen.fill((0, 0, 0))
        manager.draw_ui(screen)
        pygame.display.update()
    pygame.quit()

def redirect_proof_of_concpt_page():
    global manager
    manager = pygame_gui.UIManager((screen_width, screen_height))
    back_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (right, 10),
            (button_width, button_height)),
        text="Back",
        manager=manager)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back_button:
                        back_to_menu()
            manager.process_events(event)
        manager.update(pygame.time.get_ticks() / 1000.0)
        screen.fill((0, 0, 0))
        manager.draw_ui(screen)
        pygame.display.update()
    pygame.quit()

menu_page()

