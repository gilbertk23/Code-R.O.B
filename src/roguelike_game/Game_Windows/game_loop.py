from __future__ import annotations

# Import Files/Modules
# types: import-not-found error: Cannot find implementation or library stub for module named "pygame"
# types: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
# types: Another file has errors: '/home/samuel/Desktop/Github-Clones/Python-Roguelike-Fork/src/roguelike_game/game.py'
import pygame

from roguelike_game.Maps.game_world import World
from roguelike_game.Maps.map_generator import map_generator
from roguelike_game.Interactors.main_character import Player
from roguelike_game.Game_Windows.default_window import Window


class game_loop:
    # Data Attributes
    __slots__ = ("__fps", "window")

    # Init
    def __init__(self, fps: int = 60) -> None:
        self.set_fps(fps)

        self.window = Window()
        # TODO: This shouldn't be neccicery, for some reason
        # __init__ doesn't seem to be being run properly
        self.window.screen = pygame.display.set_mode((900, 600))
        self.window._Window__background = (0, 0, 0)

    # Helpers

    def draw_window(self, world: World, char: player) -> None:
        pygame.Surface.fill(self.window.screen, self.window.get_background())
        world.draw(self.window.screen)
        char.update(self.window.screen)

        pygame.display.update()

    # types: Error running mypy: Command 'suggest' is only valid after a 'check' command (that produces no parse errors)
    def run_game(self):
        char = Player(0, 0)
        world = World((map_generator().generate_map_array()))

        clock = pygame.time.Clock()  # Control time of main function
        run = True
        while run:
            clock.tick(self.get_fps())
            for event in pygame.event.get():  # For loop looks for events
                if event.type == pygame.QUIT:  # User quit window
                    run = False

            self.draw_window(world, char)  # Call function

    # Getters
    def get_fps(self) -> int:
        return self.__fps

    # Setters
    def set_fps(self, fps: int) -> None:
        self.__fps = fps

    # To String
