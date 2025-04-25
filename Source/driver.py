# Import Files/Modules
from Source.Maps.game_world import World
from Source.Maps.map_generator import map_generator
from Source.Interactors.main_character import player
from Source.Game_Windows.default_window import default_window
import pygame
import os

window = default_window().run_window()


def draw_window(window: window, world: World, char: player) -> None:
    pygame.Surface.fill(window, (0, 0, 0))
    world.draw(window)
    char.update()

    pygame.display.update()

# Def main contains main game loop components only
def main() -> None:
    pygame.init()

    char = player()
    world = World((map_generator().generate_map_array()))

    clock = pygame.time.Clock()  # Control time of main function
    run = True
    while run:
        for event in pygame.event.get():  # For loop looks for events
            if event.type == pygame.QUIT:  # User quit window
                run = False

        draw_window(window, world, char)  # Call function

    pygame.quit()  # quits the game loop and exits window


if __name__ == "__main__":  # Ensures code only runs file in file
    main()
