# Import Files/Modules
from Source.Interactors.sprite_sheet import sprite_sheet
import random

class sprite_assets:
    # Data Attributes
    __sprite_type = None
    __random_list = []

    # Init
    def __init__(self, sprite_type, random_list):
        self.set_sprite_type(sprite_type)
        self.set_random_list(random_list)

    # Helpers
    def get_sprite_sheet(self):
        asset_sheet = None
        if self.get_sprite_type() == "GROUND":
            asset_sheet = [sprite_sheet("Assets/FD_Dungeon.png"), random.choice(self.get_random_list()), 352, "GROUND_LAYER", 1]

        elif self.get_sprite_type() == "WALL":
            asset_sheet = [sprite_sheet("Assets/FD_Dungeon.png"), 14, 17, "BLOCK_LAYER", 2]

        elif self.get_sprite_type() == "MAIN_CHARACTER":
            asset_sheet = [sprite_sheet("Assets/FD_Ground_Tiles.png"), 200, 200, "PLAYER_LAYER", 3]

        return asset_sheet

    # Getters
    def get_sprite_image(self):
        return self.get_sprite_sheet()[0]

    def sprite_x(self):
        return self.get_sprite_sheet()[1]

    def sprite_y(self):
        return self.get_sprite_sheet()[2]

    def get_sprite_layer(self):
        return self.get_sprite_sheet()[3]

    def get_random_list(self):
        return self.__random_list

    def get_sprite_type(self):
        return self.__sprite_type

    # Setters
    def set_sprite_type(self, sprite_type):
        self.__sprite_type = sprite_type

    def set_random_list(self, random_list):
        self.__random_list = random_list

    # To String