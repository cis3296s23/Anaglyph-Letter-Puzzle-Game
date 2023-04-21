
import pygame
import pygame_gui
import Game
import sys
from pygame_gui.windows import UIColourPickerDialog
from pygame_gui.elements import UIButton
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
selected_colour = None
#THIS IS THE CURRENT COLOR VARIABLES FOR LEFT AND RIGHT, HAVE GAME CLASS USE THESE:
okay_left = (200, 0, 0) 
okay_right = (0, 0, 200)
right_clicked = 0 
left_clicked = 0
 

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
                        help_page()
                    elif event.ui_element == login_button:
                        redirect_proof_of_concpt_page()
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






def back_to_mode_page(color): 
    global okay_right,okay_left,right_clicked,left_clicked
    if right_clicked == 1:  
        okay_right = color #okay_left is current color
        right_clicked == 0
        mode_page()
    elif left_clicked == 1: 
        okay_left = color
        left_clicked == 0
        mode_page()




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
        relative_rect=pygame.Rect((middle, screen_height-200), (button_width, button_height)),
        text="Okay",
        manager=manager)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Check for button clicks
            if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                #if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    #if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == colour_picker_button: 
                if event.ui_element == back_button:
                    back_to_menu()
                if event.ui_element == colour_picker_button: 
                    colour_picker = UIColourPickerDialog(pygame.Rect(260,50,420,400), 
                                                        manager, 
                                                        window_title = "Change Color...", 
                                                        initial_colour = current_colour)
    
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
                #redirect_proof_of_concpt_page()
                back_to_mode_page(selected_colour)
                                  
            manager.process_events(event)
        
        # Update UI
        manager.update(pygame.time.get_ticks() / 1000.0)
        screen.blit(background, (0, 0))
        screen.blit(picked_colour_surface, (200, 100))
        #screen.fill((0, 0, 0))
        manager.draw_ui(screen)
        pygame.display.update()
        
    return selected_colour


def reset_colors(): 
    global okay_left, okay_right, right_clicked, left_clicked
    okay_left = (200, 0, 0) 
    okay_right = (0, 0, 200)
    right_clicked = 0 
    left_clicked = 0
    mode_page()





#need to fix positioning of buttons
#definitely need to refactor
#add number of grids increment/decrement, sequence length increment/decrement
def mode_page():
    global manager, left_color, right_color, right_clicked, left_clicked
    left_color = [] 
    right_color = []
    pygame.display.set_caption("Mode Select")
    manager = pygame_gui.UIManager((screen_width, screen_height))
    x = middle
    y = 150
    
    back_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (right, 10),
            (button_width, button_height)),
        text="Back",
        manager=manager)
    start_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((middle, screen_height-200), (button_width, button_height)),
        text="Start",
        manager=manager)
    # Create the arrow buttons
    decrease_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((middle-200, 300), (50, 50)),
        text="<",
        manager=manager)

    increase_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((middle+200, 300), (50, 50)),
        text=">",
        manager=manager)

    targets_decrease_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((middle-200, 455), (50, 50)),
        text="<",
        manager=manager)

    targets_increase_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((middle+200, 455), (50, 50)),
        text=">",
        manager=manager)
        
    
    color = (255,0,0)
            
        #color picker: 
    left_eye_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((middle-200, 150), (100, 50)),
        text="Left Eye",
        manager=manager)
        
    right_eye_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((middle+200, 150), (100, 50)),
        text="Right Eye",
        manager=manager)    
        
    grid_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((middle - 300, 300), (80, 50)),
        text="Grid Size",
        manager=manager)

    size_textbox = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect((middle, 300), (100, 50)),
        html_text="3",
        manager=manager)

    targets_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((middle - 300, 455), (80, 50)),
        text="Number of Targets:",
        manager=manager)

    targets_textbox = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect((middle, 455), (100, 50)),
        html_text="1",
        manager=manager)

    clock = pygame.time.Clock()
    running = True
    size = 3
    targets = 1
    while running:
        time_delta = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back_button:
                        back_to_menu()
                    elif event.ui_element == targets_increase_button:
                        targets = int(targets_textbox.html_text) + 1
                        if targets <= 4:
                            targets_textbox.html_text = str(targets)
                    elif event.ui_element == targets_decrease_button:
                        targets = int(targets_textbox.html_text) - 1
                        if targets >= 1:
                            targets_textbox.html_text = str(targets)
                    elif event.ui_element == increase_button:
                        size = int(size_textbox.html_text) + 1
                        if size <= 12:
                            size_textbox.html_text = str(size)
                    elif event.ui_element == decrease_button:
                        size = int(size_textbox.html_text) - 1
                        if size >= 3:
                            size_textbox.html_text = str(size)
                    elif event.ui_element == left_eye_button: 
                        left_clicked = 1
                        color_picker_page()
                        print("look here")
                        #variable that equals current 
                            #create rectangle = to the left_color array 
                    elif event.ui_element == right_eye_button: 
                        right_clicked = 1
                        color_picker_page()
                            #create rectangle = to the right_color array          
                    elif event.ui_element == start_button:
                        Game.grid_size = size
                        Game.num_targets = targets
                        Game.left_chosen = okay_left 
                        Game.right_chosen = okay_right
                        Game.main() 
                        reset_colors()
                        

            manager.process_events(event)
        manager.update(time_delta)
        screen.fill((0, 0, 0))
        manager.draw_ui(screen)
        
        rect1 = pygame.draw.rect(screen, okay_left, pygame.Rect(585, 150, 60, 60))
        rect2 = pygame.draw.rect(screen, okay_right, pygame.Rect(700, 150, 60, 60))
        pygame.display.flip()  

        size_textbox.rebuild()
        targets_textbox.rebuild()

        pygame.display.update()
    



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
    F1_text= "Highlight Feature"
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
            (x, y+150),
            (button_width, button_height)),
        text="ON",
        manager=manager)
    toggle_button_off2 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (x, y+150),
            (button_width, button_height)),
        text="OFF",
        manager=manager)
    toggle_button_off2.hide()
    F3_text = "Timer"
    toggle_button_on3 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (x, y+300),
            (button_width, button_height)),
        text="ON",
        manager=manager)
    toggle_button_off3 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(
            (x, y+300),
            (button_width, button_height)),
        text="OFF",
        manager=manager)
    toggle_button_off3.hide()
    running = True
    display_text(screen, F1_text, (middle,80), font, 'gray')
    display_text(screen, F2_text, (middle,140), font, 'gray')
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





def help_page():
    global manager
    pygame.display.set_caption("Help Page")
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
        screen.fill((0, 0, 0))
        manager.draw_ui(screen)
        display_text(screen,text, (350,45), font, 'gray') 
        #the space between title and expl: 40 , from past exp to new title: 95
        display_text(screen, text1, (350,85), font, 'gray')
        display_text(screen, text2, (350,180), font, 'gray')
        display_text(screen, text3, (350, 220), font, 'gray')
        display_text(screen, text4, (350,315), font, 'gray')
        display_text(screen, text5, (350,355), font, 'gray')
        display_text(screen, text6, (350,450), font, 'gray')
        display_text(screen, text7, (350,490), font, 'gray')
        display_text(screen, text8, (350,585), font, 'gray')
        display_text(screen, text9, (350,625), font, 'gray')
        
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


menu_page()