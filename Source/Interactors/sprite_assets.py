# Import Files/Modules
from Source.Interactors.sprite_sheet import sprite_sheet

class sprite_assets:
    # Data Attributes
    __sprite_type = None

    # Init
    def __init__(self, sprite_type):
        self.set_sprite_type(sprite_type)

    # Helpers
    def get_sprite_sheet(self):
        asset_sheet = None
        if self.get_sprite_type() == "GROUND":
            asset_sheet = [sprite_sheet("Assets/FD_Ground_Tiles.png"), 463, 335, "GROUND_LAYER", 1]

        elif self.get_sprite_type() == "BLOCKS":
            asset_sheet = [sprite_sheet("Assets/FD_Ground_Tiles.png"), 100, 100, "BLOCK_LAYER", 2]

        elif self.get_sprite_type() == "MAIN_CHARACTER":
            asset_sheet = [sprite_sheet("Assets/FD_Ground_Tiles.png"), 200, 200, "PLAYER_LAYER", 3]

        return asset_sheet

    def get_sprite_image(self):
        return self.get_sprite_sheet()[0]

    def sprite_x(self):
        return self.get_sprite_sheet()[1]

    def sprite_y(self):
        return self.get_sprite_sheet()[2]

    def get_sprite_layer(self):
        return self.get_sprite_sheet()[3]



    # Getters
    def get_sprite_type(self):
        return self.__sprite_type

    # Setters
    def set_sprite_type(self, sprite_type):
        self.__sprite_type = sprite_type

    # To String
