# Import Files/Modules
from Source.Interactors.character import character
import math


class enemy(character):
    # Data Attributes
    __target = None

    # Init
    def __init__(self, width, height, x_pos, y_pos, image, health, speed, attack_range, attack_damage, target):
        super().__init__(width, height, x_pos, y_pos, image, health, speed, attack_range, attack_damage)
        self.set_target(target)

    # Helpers
    def update_enemy(self, target_x_pos, target_y_pos):
        self.track_target(target_x_pos, target_y_pos)
        self.game_window.blit(self.image, (self.get_x_pos(), self.get_y_pos()))

    def get_new_x_pos(self, target_x_pos):
        if target_x_pos < self.get_x_pos():
            self.set_x_pos(self.get_x_pos() - self.get_speed())

        elif target_x_pos > self.get_x_pos():
            self.set_x_pos(self.get_x_pos() + self.get_speed())

    def get_new_y_pos(self, target_y_pos):
        if target_y_pos < self.get_y_pos():
            self.set_y_pos(self.get_y_pos() - self.get_speed())

        elif target_y_pos > self.get_y_pos():
            self.set_y_pos(self.get_y_pos() + self.get_speed())

    def is_awake(self, target_x_pos, target_y_pos):
        player_distance = math.sqrt((target_x_pos - self.get_x_pos())**2 + (target_y_pos - self.get_y_pos())**2)
        if player_distance <= self.get_attack_range():
            return True

        return False

    def track_target(self, target_x_pos, target_y_pos):
        if self.is_awake(target_x_pos, target_y_pos):
            self.get_new_x_pos(target_x_pos)
            self.get_new_y_pos(target_y_pos)

    # Getters
    def get_target(self):
        return self.__target

    # Setters
    def set_target(self, target):
        self.__target = target

    # To String