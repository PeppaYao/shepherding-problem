import pygame
import random

# importing functions that are used in the software

pygame.init()
# initiate pygame for a visual interface of the ECA

white = (255, 255, 255)
black = (0, 0, 0)
c_color = black
d_color = white
# Define colors

height = 600
width = 900
# Define screen size

cell_size = 2
n_of_cells = int(width / cell_size)
# define size and n of cells

n_of_gens = int(height/cell_size)
#defines how many generations are simulated


one_gen = []
current_gen = []
#variables for the loop creating the population

for s in range(n_of_gens+1):
    for i in range(n_of_cells+1):
        one_gen = one_gen + [bool(random.getrandbits(1))]
#produces one generation

    current_gen = current_gen + [one_gen]
    one_gen = []

next_gen = current_gen[:]
#adds every new generation to the nested list that works as our 2d grid


def conway(to_change, b, k, r):
    changing_gen = to_change[s][:]
    changing_gen.pop(k)
    changing_gen.insert(k, b)
    to_change.pop(r)
    to_change.insert(r, changing_gen)
    return
#Function that substitutes the old cell's state with the offspring state for the next_gen variable

running = True


# Variable for Main loop

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2 Dimensional Cellular Automaton")
# creates screen and sets caption


while running:
# Main Loop starts

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#option for quitting

    pygame.image.save(screen, "2dimensional.jpeg")
    current_gen = next_gen[:]
    pygame.display.update()
#updates generation and display

    for s in range(n_of_gens):
        for i in range(n_of_cells):
            neighbors = current_gen[s][i - 1] + current_gen[s][i + 1] + \
                        + current_gen[s + 1][i - 1] + current_gen[s + 1][i] + \
                        + current_gen[s + 1][i + 1] + current_gen[s - 1][i - 1] + \
                        +current_gen[s - 1][i] + current_gen[s - 1][i + 1]
#determines the neighborhood

            if current_gen[s][i]:
               pygame.draw.rect(screen, white, ((i * cell_size), (s * cell_size), cell_size, cell_size))
               if neighbors != 2 and neighbors != 3:
                   conway(next_gen, False, i, s)
               else:
                   pass
            else:
                pygame.draw.rect(screen, black, ((i * cell_size), (s * cell_size), cell_size, cell_size))
                if neighbors == 3:
                    conway(next_gen, True, i, s)
                else:
                    pass
#Draws the cell and compiles the new generation

pygame.quit
# halts software

