import pygame
import pygame_gui
import Game
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
                        redirect_proof_of_concpt_page()
                    elif event.ui_element == help_button:
                        help_page()
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






def mode_page():
    global manager
    pygame.display.set_caption("Mode Select")
    
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
        
        # Clear the screen and draw the UI
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
    pygame.display.set_caption("Login Page")
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
        text = "Login:"
        font = pygame.font.SysFont(None, 26)
        screen.fill((0, 0, 0))
        manager.draw_ui(screen)
        display_text(screen, text, (350,20), font, 'gray')
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
