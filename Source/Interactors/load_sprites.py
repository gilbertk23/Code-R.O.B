from Source.Interactors.main_character import main_character
from Source.Interactors.enemy import enemy
from Source.Interactors.sprite_block import sprite_block
import random
import pygame


class load_sprites:
    # Data Attributes
    __sprite_list = []

    # Init
    def __init__(self, window, world_array, enemy_num, tile_map, sprite_list=[]):
        self.set_sprite_list(sprite_list)
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.ground = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.enemy_num = enemy_num
        self.enemy_list = []

        # World Information
        self.game_window = window
        self.world_array = world_array

        self.main_character = self.load_character(window)
        self.find_enemies(enemy_num)

        self.create_tilemap(tile_map)

    # Helpers
    def update(self, game_window):
        self.draw_sprites(game_window)
        self.all_sprites.update(game_window, self.main_character.get_x_pos(), self.main_character.get_y_pos())

    def load_character(self, window):
        character = main_character(self, window=window, x_pos=200, y_pos=300, image='Player Sprite.png')
        return character

    def find_enemies(self, enemy_num):
        for enemies in range(enemy_num):
            rand_x = random.randint(self.world_array.get_left_portal_pos()[0] + 10, self.world_array.get_right_portal_pos()[0] - 10)
            rand_y = random.randint(self.world_array.get_top_portal_pos()[1] + 10, self.world_array.get_bottom_portal_pos()[1] - 10)
            new_enemy = enemy(self, 20, 20, rand_x, rand_y, 'enemy.png', 10, 2, 150, 10, 10)
            self.enemy_list.append(new_enemy)

    def draw_sprites(self, game_window):
        self.all_sprites.draw(game_window)

    def create_tilemap(self, tile_map):
        for x, row in enumerate(tile_map):
            for y, column in enumerate(row):
             #   sprite_block(self, y * 20, x * 20, "BLOCKS")
                if column == 1:
                    sprite_block(self,y * 20, x * 20, "GROUND")
                    pass

    # Getters
    def get_sprite_list(self):
        return self.__sprite_list

    # Setters
    def set_sprite_list(self, sprite_list):
        self.__sprite_list = sprite_list

    # To String