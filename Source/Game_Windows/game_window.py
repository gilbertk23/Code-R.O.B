# Import Files/Modules
from Source.Maps.map_generator import map_generator
import pygame
import os

class game_window:
    # Data Attributes
    __width = -1
    __height = -1
    __fps = -1
    __game_name = "Error"

    # Init
    def __init__(self, width=900, height=600, fps=60, game_name="ROB"):
        self.set_width(width)
        self.set_height(height)
        self.set_fps(fps)
        self.set_game_name(game_name)

        # Instantiate pywindow
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(game_name)

    # Helpers
    def draw_window(self):



    # Getters
    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_fps(self):
        return self.__fps

    def get_game_name(self):
        return self.__game_name

    # Setters
    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_fps(self, fps):
        self.__fps = fps

    def set_game_name(self, game_name):
        self.__game_name = game_name

    # To String
