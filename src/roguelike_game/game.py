from __future__ import annotations

__title__ = "Game Platformer"
__version__ = "0.0.0"

# Import Files/Modules
from roguelike_game.Maps.game_world import World
from roguelike_game.Maps.map_generator import map_generator
from roguelike_game.Interactors.main_character import Player
import pygame
import os

WIDTH, HEIGHT = 900, 600  # Pygame Window Width and Height
FPS = 60  # Sets the Frames Per Second for game


def draw_window(screen: pygame.Surface, world: World, player: Player) -> None:
    pygame.Surface.fill(screen, (0, 0, 0))
    world.draw(screen)
    player.update()

    pygame.display.update()

# Def main contains main game loop components only
def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create py window
    pygame.display.set_caption(__title__)  # Window Game Caption


    player = Player(10, 10)
    world = World((map_generator().generate_map_array()))


    clock = pygame.time.Clock()  # Control time of main function
    run = True
    while run:
        for event in pygame.event.get():  # For loop looks for events
            if event.type == pygame.QUIT:  # User quit window
                run = False

        draw_window(screen, world, player)  # Call function
        clock.tick(FPS)  # Controls the speed of the while loop

    pygame.quit()  # quits the game loop and exits window


if __name__ == "__main__":  # Ensures code only runs file in file
    main()
