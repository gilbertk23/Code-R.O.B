# Import Files/Modules
from Source.Game_Windows.default_window import default_window
from Source.Interactors.sprite import sprite
import pygame
import os

class coin(sprite):
    # Data Attributes
    __value = -1

    # Init
    def __init__(self, width, height, x_pos, y_pos, image, value):
        super().__init__(width, height, x_pos, y_pos, image)
        self.set_value(value)

        # Sets window
        self.character = pygame.image.load(os.path.join('Assets', image))
        self.image = pygame.transform.scale(self.character, (width, height))
        self.game_window = default_window().init_window()

    # Helpers
    def update_coin(self):
        self.game_window.blit(self.image, (self.get_x_pos(), self.get_y_pos()))

    # Getters
    def get_value(self):
        return self.__value

    # Setters
    def set_value(self, value):
        self.__value = value

    # To String