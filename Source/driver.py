# Import Files/Modules
from Source.Maps.game_world import World
from Source.Maps.map_generator import map_generator
from Source.Interactors.main_character import Player
import pygame
pygame.init()

FPS = 60  # Sets the Frames Per Second for game

test = map_generator()
player = Player(10, 10)
world = World(test.generate_map_array())

def draw_window():  # Function for background arguments
    world.draw()
    player.update()
    pygame.display.update()  # Update game loop

# Def main contains main game loop components only
def main():
    clock = pygame.time.Clock()  # Control time of main function
    run = True
    while run:
        clock.tick(FPS)  # Controls the speed of the while loop
        for event in pygame.event.get():  # For loop looks for events
            if event.type == pygame.QUIT:  # User quit window
                run = False


        draw_window()  # Call function

    pygame.quit()  # quits the game loop and exits window


if __name__ == "__main__":  # Ensures code only runs file in file
    main()
