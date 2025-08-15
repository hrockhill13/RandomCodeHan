# Henk Rockhill
# Falling Sand Game
# particle states N= None S= Sand particle R= Rock particle

import pygame
from simulation import Simulation

pygame.init()
pygame.mouse.set_visible(False)

#define a display surface and other variables
win_H: int= 600
win_W: int= 600
FPS: int= 120
gry: tuple[int, int, int]= (29, 29, 29)
c_size: int=4
brush_size = 2


# draw the window using the dimensions above
window = pygame.display.set_mode((win_H, win_W))
pygame.display.set_caption('Falling Sand')

#set up the clock
clock = pygame.time.Clock()

#actually create the window or grid
simulation = Simulation(win_W, win_H, c_size)


#simulation loop
while True:
    # event handling (keys, controls, mouse)
    simulation.handle_controls()

    # updating state
    simulation.update()

    # drawing
    window.fill(gry)
    simulation.draw(window)

    # update the screen by redrawing the whole screen
    pygame.display.flip()

    # set the frame rate of the game
    clock.tick(FPS)







