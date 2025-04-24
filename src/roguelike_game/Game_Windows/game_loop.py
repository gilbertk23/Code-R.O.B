# Import Files/Modules
from Source.Maps.map_generator import map_generator
from Source.Maps.game_world import World
from Source.Interactors.main_character import Player
import pygame

class game_loop:
    # Data Attributes
    __window_width = -1
    __window_height = -1
    __background = -1
    __game_name = -1
    __fps = -1

    # Init
    def __init__(self, window_width=900, window_height=700, background=(0, 0, 0), game_name="ROB", fps=60):
        self.set_window_width(window_width)
        self.set_window_height(window_height)
        self.set_background(background)
        self.set_game_name(game_name)
        self.set_fps(fps)

        self.game_window = pygame.display.set_mode((self.get_window_width(), self.get_window_height()))
        self.game_window.fill(self.get_background())
        pygame.display.set_caption(self.get_game_name())

        self.game_world = World(map_generator().generate_map_array())
        self.player1 = Player(10, 10)

    # Getters
    def get_window_width(self):
        return self.__window_width

    def get_window_height(self):
        return self.__window_height

    def get_background(self):
        return self.__background

    def get_game_name(self):
        return self.__game_name

    def get_fps(self):
        return self.__fps

    # Setters
    def set_window_width(self, window_width):
        self.__window_width = window_width

    def set_window_height(self, window_height):
        self.__window_height = window_height

    def set_background(self, background):
        self.__background = background

    def set_game_name(self, game_name):
        self.__game_name = game_name

    def set_fps(self, fps):
        self.__fps = fps
    # To String
