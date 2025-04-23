# Import Files/Modules
from Source.Maps.game_world import game_world
from Source.Maps.map_generator import map_generator
import pygame
pygame.init()

def main():
    test = map_generator()

    world = game_world()

    run = True
    while run:
        for event in pygame.event.get():  # For loop looks for events
            if event.type == pygame.QUIT:  # User quit window
                run = False

        world.draw_window()

    pygame.quit()  # quits the game loop and exits window

if __name__ == '__main__':
    main()

