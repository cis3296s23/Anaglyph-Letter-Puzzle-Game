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
