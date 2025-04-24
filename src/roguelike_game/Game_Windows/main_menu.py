# Import Files/Modules
import pygame

class main_menu:
    # Data Attributes
    __game_name = None
    __screen_width = -1
    __screen_height = -1
    __background = None

    # Init
    def __init__(self, game_name, screen_width=900, screen_height=500, background=(0, 0, 0)):
        self.set_game_name(game_name)
        self.set_screen_width(screen_width)
        self.set_screen_height(screen_height)
        self.set_background(background)

        self.window = pygame.display.set_mode((screen_width, screen_height))
        self.window.fill(background)
        pygame.display.set_caption("Rob")

    # Helpers


    # Getters
    def get_game_name(self):
        return self.__game_name

    def get_screen_width(self):
        return self.__screen_width

    def get_screen_height(self):
        return self.__screen_height

    def get_background(self):
        return self.__background

    # Setters
    def set_game_name(self, game_name):
        self.__game_name = game_name

    def set_screen_width(self, screen_width):
        self.__screen_width = screen_width

    def set_screen_height(self, screen_height):
        self.__screen_height = screen_height

    def set_background(self, background):
        self.__background = background

    # To String
