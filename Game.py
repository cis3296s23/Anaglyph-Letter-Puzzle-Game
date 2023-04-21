import math
import pygame
import random
pygame.init()

# set up the display
#12 doesn't fit 11 is max for grid_size
grid_size = 8
#cellsize 75, gridsize 8
# cell_size seems to make text larger, not nesecarily the cell itself - or space between the cell.
#does affect the space between cells but def makes text larger - both at same time
cell_size = 75
info = pygame.display.Info()

width = info.current_w
height = info.current_h
font_size = math.ceil(cell_size // 1.25)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Letter Grid")

# set up the font
font = pygame.font.Font(None, font_size)
standard = 'b'
target = 'd'
num_targets = 3
left_chosen = (200, 0, 0) #red
right_chosen = (0, 0, 200) #blue
def gen_grid():
    global running, target_count, grid

    # set up the grid
    grid = []
    target_indices = set()
    for row in range(grid_size):
        grid.append([standard] * grid_size)

    # add target letters to grid
    for i in range(num_targets):
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        while (row, col) in target_indices:
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - 1)
        grid[row][col] = target
        target_indices.add((row, col))

    target_count = num_targets
    return grid

running = True

def main():
    global running, target_count, grid
    grid = gen_grid()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                row = y // cell_size
                col = x // cell_size
                if grid[row][col] == target:
                    grid[row][col] = ""
                    target_count -= 1
                    if target_count == 0:
                        # running = False
                        return

        screen.fill((0, 0, 0))

        for row in range(grid_size):
            for col in range(grid_size):
                letter = grid[row][col]
                color = left_chosen if (row + col) % 2 == 0 else right_chosen
                text = font.render(letter, True, color)
                lw = text.get_width() 
                lh = text.get_height() 
                x = col * cell_size + (cell_size - text.get_width()) // 2
                y = row * cell_size + (cell_size - text.get_height()) // 2
                screen.blit(text, (x, y))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()



