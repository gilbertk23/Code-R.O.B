# Import Files/Modules
from Source.Interactors.character import character
from Source.Interactors.config import *
import pygame
import os

class main_character(character):
    # Data Attributes
    __player_controlled = None

    # Init
    def __init__(self, sprite_sheet, window, width=CHAR_WIDTH, height=CHAR_HEIGHT, x_pos=CENTER_X, y_pos=CENTER_Y, image=DEFAULT_IMAGE, tile_map=[], health=100, speed=2, attack_range=10, attack_damage=10, player_controlled=True):
        # Super Init of the Character class
        super().__init__(sprite_sheet, width, height, x_pos, y_pos, image, health, speed, attack_range, attack_damage)
        self.set_player_controlled(player_controlled)

        self._layer = PLAYER_LAYER  # Set Player Layer

        # World Information
        self.game_window = window
        self.tile_map = tile_map

    # Helpers
    def update(self, world, target_x_pos, target_y_pos):
        self.key_press()  # Detect key presses
        self.rect.topleft = (self.get_x_pos(), self.get_y_pos())  # Update character to window


    def key_press(self):
        key = pygame.key.get_pressed()
        key_press = None
        print(self.get_speed())
        if key[pygame.K_a]:
            self.set_x_pos(self.get_x_pos() - self.get_speed())
            key_press = 'a'
        if key[pygame.K_d]:
            self.set_x_pos(self.get_x_pos() + self.get_speed())
            key_press = 'd'
        if key[pygame.K_w]:
            self.set_y_pos(self.get_y_pos() - self.get_speed())
            key_press = 'w'
        if key[pygame.K_s]:
            self.set_y_pos(self.get_y_pos() + self.get_speed())
            key_press = 's'
        return key_press



    # Getters
    def get_player_controlled(self):
        return self.__player_controlled

    # Setters
    def set_player_controlled(self, player_controlled):
        self.__player_controlled = player_controlled

    # To String