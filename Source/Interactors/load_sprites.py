from Source.Interactors.main_character import main_character
from Source.Interactors.enemy import enemy
from Source.Interactors.sprite_block import sprite_block
import random
import pygame
import time


class load_sprites:
    # Data Attributes
    __sprite_list = []

    # Init
    def __init__(self, window, world_array, enemy_num, tile_map, sprite_list=[]):
        self.counter = -1
        self.boss = -1
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

    # Holds all of the logic to every helper
    def update(self, game_window):
        # Removes the main character when you get below 0 hp
        if self.main_character.get_health() < 0:
            self.main_character.kill()

        self.boss_room_control()
        self.mob_logic()
        self.draw_sprites(game_window)
        self.map_collision()
        self.all_sprites.update(game_window, self.main_character.get_x_pos(), self.main_character.get_y_pos())

    # The function that just spawns the mobs itself
    def spawn_boss_mobs(self):
        self.find_enemies(random.randint(0, 30))

    # Logic that spawns the mobs every 300 ticks
    def boss_room_control(self):
        if self.map_count < 6:
            self.boss = self.get_to_boss()
        if self.map_count == 6:
            if self.boss.get_health() >= 0:
                self.counter = self.counter + 1
                if self.counter % 300 == 0:
                    self.spawn_boss_mobs()

    # Function that holds all the collision logic with the mobs / character
    def mob_logic(self):
        for mobs in self.enemy_list:
            if enemy.character_hit(mobs, self.main_character.get_x_pos(), self.main_character.get_y_pos()):
                self.main_character.set_health(self.main_character.get_health() - enemy.get_attack_damage(mobs))
        for index, mobs in enumerate(self.enemy_list):
            if enemy.get_health(mobs) < 0:
                enemy.kill(mobs)
                enemy.set_health(mobs, (enemy.get_health(mobs), - self.main_character.get_attack_damage()))
                del self.enemy_list[index]

    # Function that resets the map when the portals are hit, kills the enemies, respawns the enemies and holds the logic to tp to the boss
    def get_to_boss(self):
        if self.map_count <= 5:
            self.mob_logic()

            if self.main_character.get_x_pos() in range(116, 124) and self.main_character.get_y_pos() in range(360,
                                                                                                               364) or self.main_character.get_x_pos() in range(
                438, 442) and self.main_character.get_y_pos() in range(124,
                                                                       132) or self.main_character.get_x_pos() in range(
                748, 752) and self.main_character.get_y_pos() in range(362,
                                                                       366) or self.main_character.get_x_pos() in range(
                444, 452) and self.main_character.get_y_pos() in range(554, 562):

                for mobs in self.enemy_list:
                    enemy.kill(mobs)
                self.enemy_list.clear()
                self.update_player()

                if self.map_count == 5:
                    self.boss = self.create_boss()
                    self.map_count = self.map_count + 1
                    return self.boss
                else:
                    self.find_enemies(self.enemy_num)

                self.map_count = self.update_map_information()

    # This sets the player to a random location in the map
    def update_player(self):
        self.main_character.set_x_pos(random.randint(120, 730))
        self.main_character.set_y_pos(random.randint(130, 550))

    # This counts the portal count
    def update_map_information(self):
        # Update Map Count
        self.map_count += 1
        return self.map_count


    # This is so that the character cant get out of the main map
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

    # Loads the character
    def load_character(self, window, image):
        character = main_character(self, window=window, width=32, height=32, x_pos=200, y_pos=300, image=image,
                                   speed=2,
                                   tile_map=self.tile_map)
        return character

    # Creates the enemies
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
            new_enemy = enemy(self, 32, 32, rand_x, rand_y, random_choice, 50, speed, 150, 1, 10)
            self.enemy_list.append(new_enemy)

    # Creates Boss
    def create_boss(self):
        self.boss = enemy(self, 100, 100, 385, 200, 'boss.png', 300, 0, 300, 10, 10)
        return self.boss

    def draw_sprites(self, game_window):
        self.blocks.draw(game_window)
        self.all_sprites.draw(game_window)

    # Creates the map
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
