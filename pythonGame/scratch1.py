import pygame
import sys

pygame.init()

# Create the screen window
screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Pygame Test")
clock = pygame.time.Clock()
# Create a blue surface
test_surface = pygame.Surface((100, 200))
test_surface.fill((0, 0, 255))  # RGB for blue
test_rect = test_surface.get_rect(center = (200,250))

# Main game loop
running = True
while running:
    pygame.time.delay(10)  # helps with stability on macOS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((175, 215, 70))  # Gold background
    screen.blit(test_surface, test_rect)  # Position the blue surface more centrally
    pygame.display.flip()  # Use flip() instead of update() for full redraw
    clock.tick(60)

pygame.quit()
sys.exit()