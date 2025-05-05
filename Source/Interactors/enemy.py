# Import Files/Modules
from Source.Interactors.character import character


class enemy(character):
    # Data Attributes
    __target = None

    # Init
    def __init__(self, width, height, x_pos, y_pos, image, health, speed, attack_range, attack_damage, target):
        super().__init__(width, height, x_pos, y_pos, image, health, speed, attack_range, attack_damage)
        self.set_target(target)

    # Helpers
    def update_enemy(self):
        self.game_window.blit(self.image, (self.get_x_pos(), self.get_y_pos()))

    def track_target(self, target):
        self.set_target(target)

    # Getters
    def get_target(self):
        return self.__target

    # Setters
    def set_target(self, target):
        self.__target = target

    # To String