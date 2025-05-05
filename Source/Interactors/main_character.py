# Import Files/Modules
from Source.Interactors.character import character
import pygame

class main_character(character):
    # Data Attributes
    __player_controlled = None

    # Init
    def __init__(self, width, height, x_pos, y_pos, image, health, speed, attack_range, attack_damage, player_controlled):
        super().__init__(width, height, x_pos, y_pos, image, health, speed, attack_range, attack_damage)
        self.set_player_controlled(player_controlled)

    # Helpers
    def key_press(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.set_x_pos(self.get_x_pos() - self.get_speed())
        if key[pygame.K_d]:
            self.set_x_pos(self.get_x_pos() + self.get_speed())
        if key[pygame.K_w]:
            self.set_y_pos(self.get_y_pos() - self.get_speed())
        if key[pygame.K_s]:
            self.set_y_pos(self.get_y_pos() + self.get_speed())

    def update_main_character(self):
        self.key_press()
        self.game_window.blit(self.image, (self.get_x_pos(), self.get_y_pos()))

    # Getters
    def get_player_controlled(self):
        return self.__player_controlled

    # Setters
    def set_player_controlled(self, player_controlled):
        self.__player_controlled = player_controlled

    # To String