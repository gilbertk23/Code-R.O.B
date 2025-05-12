# Import Files/Modules
from Source.Interactors.character import character
from Source.Interactors.config import *
import math


class enemy(character):
    # Data Attributes
    __target = None

    # Init
    def __init__(self, sprite_sheet, width=CHAR_WIDTH, height=CHAR_HEIGHT, x_pos=CENTER_X, y_pos=CENTER_Y, image=DEFAULT_IMAGE, health=100, speed=3, attack_range=10, attack_damage=1, target=None):
        super().__init__(sprite_sheet, width, height, x_pos, y_pos, image, health, speed, attack_range, attack_damage)
        self.set_target(target)

        self._layer = ENEMY_LAYER # Set Enemy Layer

    # Helpers
    def update(self, world, target_x_pos, target_y_pos):
        self.track_target(target_x_pos, target_y_pos)
        self.enemy_collide(target_x_pos, target_y_pos)
        self.rect.topleft = (self.get_x_pos(), self.get_y_pos())  # Update character to window

    def character_hit(self, target_x_pos, target_y_pos):
        if self.get_x_pos() in range(target_x_pos-13, target_x_pos+13) and self.get_y_pos() in range(target_y_pos-13, target_y_pos+13):
            return True

    def enemy_collide(self, target_x_pos, target_y_pos):
        if self.get_x_pos() in range(target_x_pos-35, target_x_pos+45) and self.get_y_pos() in range(target_y_pos-35, target_y_pos+45):
            self.set_health(self.get_health()-1)

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