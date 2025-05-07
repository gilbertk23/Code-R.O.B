import pygame
from Interactors.config import *

class sprite_sheet:
    # Data Attributes
    __sprite_sheet_image = "Error"

    # Init
    def __init__(self, sprite_sheet_image):
        self.set_sprite_sheet_image(pygame.image.load(sprite_sheet_image).convert())

    # Helpers
    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.get_sprite_sheet_image(), (0,0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite

    # Getters
    def get_sprite_sheet_image(self):
        return self.__sprite_sheet_image

    # Setters
    def set_sprite_sheet_image(self, sprite_sheet_image):
        self.__sprite_sheet_image = sprite_sheet_image

    # To String