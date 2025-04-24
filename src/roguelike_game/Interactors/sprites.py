class sprites: 
    # Data Attributes
    __character = "Error"
    __maps = "Error"
    __attacks = "Error"
    __basic_enemies = "Error"
    __villian = "Error"

    # Init
    def __init__(self, character, maps, attacks, basic_enemies, villian): 
        self.set_character(character)
        self.set_maps(maps)
        self.set_attacks(attacks)
        self.set_basic_enemies(basic_enemies)
        self.set_villian(villian)

    # Helpers

    # Getters
    def get_character(self): 
        return self.__character

    def get_maps(self): 
        return self.__maps

    def get_attacks(self): 
        return self.__attacks

    def get_basic_enemies(self): 
        return self.__basic_enemies

    def get_villian(self): 
        return self.__villian

    # Setters
    def set_character(self, character): 
        self.__character = character

    def set_maps(self, maps): 
        self.__maps = maps

    def set_attacks(self, attacks): 
        self.__attacks = attacks

    def set_basic_enemies(self, basic_enemies): 
        self.__basic_enemies = basic_enemies

    def set_villian(self, villian): 
        self.__villian = villian

    # ToString
    def __str__(self):
        sprites_string = ""
        sprites_string += (f"Sprites Data Attributes-->\n\t"    
            f"Character: {self.get_character()}\n\t"
            f"Maps: {self.get_maps()}\n\t"
            f"Attacks: {self.get_attacks()}\n\t"
            f"Basic_Enemies: {self.get_basic_enemies()}\n\t"
            f"Villian: {self.get_villian()}\n\t")
        return sprites_string
