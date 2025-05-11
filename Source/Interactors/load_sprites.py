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
        self.map_count = 0
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
        self.tile_map = tile_map

        try:
            self.main_character = self.load_character(window, 'character_left.png')
            print("Main character has loaded successfully!")
        except ImportError:
            print("Source or pygame has not been imported correctly, please make sure to import the packages.")
        except Exception as e:
            print("Error: ", e)

        try:
            self.find_enemies(enemy_num)
            print("Enemies have loaded successfully!")
        except ImportError:
            print("Source or pygame has not been imported correctly, please make sure to import the packages.")
        except Exception as e:
            print("Error: ", e)

        self.create_tilemap(tile_map)

    # Helpers
    def update(self, game_window):
        if self.map_count < 6:
            if self.main_character.get_x_pos() == 120 and self.main_character.get_y_pos() == 130:
                for mobs in self.enemy_list:
                    enemy.kill(mobs)
                self.update_player()

                if self.map_count == 5:
                    self.create_boss()


                else:
                    self.find_enemies(self.enemy_num)

                self.map_count = self.update_map_information()
            self.draw_sprites(game_window)

            self.map_collision()
            self.all_sprites.update(game_window, self.main_character.get_x_pos(), self.main_character.get_y_pos())



    def update_player(self):
        self.main_character.set_x_pos(200)
        self.main_character.set_y_pos(300)

    def update_map_information(self):
        # Update Map Count
        self.map_count += 1
        return self.map_count

    def map_collision(self):

        # Left
        if self.main_character.get_x_pos() < 115:
            self.main_character.set_x_pos(self.main_character.get_x_pos() + 10)
            self.main_character.set_speed(0)

        # Right border collision
        elif self.main_character.get_x_pos() > 755:
            self.main_character.set_x_pos(self.main_character.get_x_pos() - 10)
            self.main_character.set_speed(0)

        # Top border collision
        elif self.main_character.get_y_pos() < 125:
            self.main_character.set_y_pos(self.main_character.get_y_pos() + 10)
            self.main_character.set_speed(0)

        elif self.main_character.get_y_pos() > 560:
            self.main_character.set_y_pos(self.main_character.get_y_pos() - 10)
            self.main_character.set_speed(0)
        else:
            self.main_character.set_speed(2)

    def load_character(self, window, image):
        character = main_character(self, window=window, width=32, height=32, x_pos=200, y_pos=300, image=image,
                                   speed=2,
                                   tile_map=self.tile_map)
        return character

    def find_enemies(self, enemy_num):
        random_list = ['enemy_1.png', 'enemy_3.png']
        speed = 0
        for enemies in range(enemy_num):
            random_choice = random.choice(random_list)
            if random_choice == 'enemy_1.png':
                speed = 1
            else:
                speed = 0.5
            rand_x = random.randint(115,
                                    755)
            rand_y = random.randint(125,
                                    560)
            new_enemy = enemy(self, 32, 32, rand_x, rand_y, random_choice, 50, speed, 150, 10, 10)
            self.enemy_list.append(new_enemy)

    def create_boss(self):
        boss = enemy(self, 100, 100, 385, 200, 'boss.png', 300, 0, 300, 10, 10)
        self.enemy_list.append(boss)

    def draw_sprites(self, game_window):
        self.blocks.draw(game_window)
        self.all_sprites.draw(game_window)

    def create_tilemap(self, tile_map):
        for x, row in enumerate(tile_map):
            for y, column in enumerate(row):
                sprite_block(self, y * 16, x * 16, "GROUND")
                if column == 1:
                    sprite_block(self, y * 16, x * 16, "WALL")
                    pass

    # Getters
    def get_sprite_list(self):
        return self.__sprite_list

    # Setters
    def set_sprite_list(self, sprite_list):
        self.__sprite_list = sprite_list

    # To String
