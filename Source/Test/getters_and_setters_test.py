import pygame
import pygame.font

from Source.Maps.map_generator import map_generator
from Source.Maps.game_world import world
from Source.Interactors.sprite import sprite
from Source.Interactors.character import character
from Source.Interactors.button import button
from Source.Interactors.main_character import main_character
from Source.Interactors.enemy import enemy
from Source.Game_Windows.game_loop import game_loop
from Source.Game_Windows.default_window import default_window
from Source.Game_Windows.windows import windows

import unittest


# Maps Directory
class map_generator_setters_getters_tester(unittest.TestCase):

    # Example Setup
    def setUp(self):
        self.world = map_generator()

    # Getters Testers
    def test_get_min_width(self):
        self.assertEqual(self.world.get_min_width(), 35)

    def test_get_max_width(self):
        self.assertEqual(self.world.get_max_width(), 35)

    def test_get_min_height(self):
        self.assertEqual(self.world.get_min_height(), 25)

    def test_get_max_height(self):
        self.assertEqual(self.world.get_max_height(), 25)

    def test_get_min_enemies(self):
        self.assertEqual(self.world.get_min_enemies(), 10)

    def test_get_max_enemies(self):
        self.assertEqual(self.world.get_max_enemies(), 40)

    def test_get_current_score(self):
        self.assertEqual(self.world.get_current_score(), 0)

    def test_get_map_count(self):
        self.assertEqual(self.world.get_map_count(), 1)

    # Setters Testers
    def test_set_min_width(self):
        self.world.set_min_width(20)
        self.assertEqual(self.world.get_min_width(), 20)

    def test_set_max_width(self):
        self.world.set_max_width(40)
        self.assertEqual(self.world.get_max_width(), 40)

    def test_set_min_height(self):
        self.world.set_min_height(20)
        self.assertEqual(self.world.get_min_height(), 20)

    def test_set_max_height(self):
        self.world.set_max_height(40)
        self.assertEqual(self.world.get_max_height(), 40)

    def test_set_min_enemies(self):
        self.world.set_min_enemies(20)
        self.assertEqual(self.world.get_min_enemies(), 20)

    def test_set_max_enemies(self):
        self.world.set_max_enemies(40)
        self.assertEqual(self.world.get_max_enemies(), 40)

    def test_set_current_score(self):
        self.world.set_current_score(5)
        self.assertEqual(self.world.get_current_score(), 5)

    def test_set_map_count(self):
        self.world.set_map_count(10)
        self.assertEqual(self.world.get_map_count(), 10)


class game_world_generator_setters_getters_tester(unittest.TestCase):

    # Example Setup
    def setUp(self):
        self.test = map_generator()
        self.test_array = self.test.generate_map_array()
        self.world = world(self.test_array)

    # Getters Testers
    def test_get_game_map(self):
        self.assertEqual(self.world.get_game_map(), self.test_array)

    def test_get_tile_size(self):
        self.assertEqual(self.world.get_tile_size(), 20)

    # Setters Testers
    def test_set_game_world(self):
        self.world.set_game_map([1, 2, 3, 4])
        self.assertEqual(self.world.get_game_map(), [1, 2, 3, 4])

    def test_set_get_tile_size(self):
        self.world.set_tile_size(50)
        self.assertEqual(self.world.get_tile_size(), 50)


# Interactors Directory
class button_setters_getters_testers(unittest.TestCase):

    # Example Setup
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((800, 600))
        win_box_img = pygame.image.load("Assets/win_box.png").convert_alpha()
        self.button = button(image=win_box_img)

    # Getter Testers
    def test_get_width(self):
        self.assertEqual(self.button.get_width(), 200)

    def test_get_height(self):
        self.assertEqual(self.button.get_height(), 100)

    def test_get_x_pos(self):
        self.assertEqual(self.button.get_x_pos(), 10)

    def test_get_y_pos(self):
        self.assertEqual(self.button.get_y_pos(), 10)

    def test_get_is_hover(self):
        self.assertEqual(self.button.get_is_hover(), False)

    def test_get_is_clicked(self):
        self.assertEqual(self.button.get_is_clicked(), False)

    # Setter Testers
    def test_set_width(self):
        self.button.set_width(20)
        self.assertEqual(self.button.get_width(), 20)

    def test_set_height(self):
        self.button.set_height(20)
        self.assertEqual(self.button.get_height(), 20)

    def test_set_x_pos(self):
        self.button.set_x_pos(20)
        self.assertEqual(self.button.get_x_pos(), 20)

    def test_set_y_pos(self):
        self.button.set_y_pos(20)
        self.assertEqual(self.button.get_y_pos(), 20)

    def test_set_image(self):
        self.button.set_image("Source/Assets/Dark Block.png")
        self.assertEqual(self.button.get_image(), "Source/Assets/Dark Block.png")

    def test_set_is_hover(self):
        self.button.set_is_hover(True)
        self.assertEqual(self.button.get_is_hover(), True)

    def test_set_is_clicked(self):
        self.button.set_is_clicked(True)
        self.assertEqual(self.button.get_is_clicked(), True)


class sprite_setters_getters_testers(unittest.TestCase):

    # Example Setup
    def setUp(self):
        self.sprite = sprite()

    # Getter Testers
    def test_get_width(self):
        self.assertEqual(self.sprite.get_width(), 10)

    def test_get_height(self):
        self.assertEqual(self.sprite.get_height(), 10)

    def test_get_x_pos(self):
        self.assertEqual(self.sprite.get_x_pos(), 10)

    def test_get_y_pos(self):
        self.assertEqual(self.sprite.get_y_pos(), 10)

    def test_get_image(self):
        self.assertEqual(self.sprite.get_image(), "Source/Assets/Clear Block.png")

    # Setter Testers
    def test_set_width(self):
        self.sprite.set_width(20)
        self.assertEqual(self.sprite.get_width(), 20)

    def test_set_height(self):
        self.sprite.set_height(20)
        self.assertEqual(self.sprite.get_height(), 20)

    def test_set_x_pos(self):
        self.sprite.set_x_pos(20)
        self.assertEqual(self.sprite.get_x_pos(), 20)

    def test_set_y_pos(self):
        self.sprite.set_y_pos(20)
        self.assertEqual(self.sprite.get_y_pos(), 20)

    def test_set_image(self):
        self.sprite.set_image("Source/Assets/Dark Block.png")
        self.assertEqual(self.sprite.get_image(), "Source/Assets/Dark Block.png")


class main_character_setters_getters_tester(unittest.TestCase):

    # Example Setup
    def setUp(self):
        self.main_character = main_character(10, 10, 400, 560, 'Player Sprite.png', 100, 5, 2, 10, True)

    # Getters Testers
    def test_get_x_pos(self):
        self.assertEqual(self.main_character.get_x_pos(), 400)

    def test_get_y_pos(self):
        self.assertEqual(self.main_character.get_y_pos(), 560)

    def test_get_width(self):
        self.assertEqual(self.main_character.get_width(), 10)

    def test_get_height(self):
        self.assertEqual(self.main_character.get_height(), 10)

    def test_get_image(self):
        self.assertEqual(self.main_character.get_image(), 'Player Sprite.png')

    def test_get_speed(self):
        self.assertEqual(self.main_character.get_speed(), 5)

    def test_get_health(self):
        self.assertEqual(self.main_character.get_health(), 100)

    def test_get_attack_range(self):
        self.assertEqual(self.main_character.get_attack_range(), 2)

    def test_get_attack_damage(self):
        self.assertEqual(self.main_character.get_attack_damage(), 10)

    def test_get_player_controlled(self):
        self.assertEqual(self.main_character.get_player_controlled(), True)

    # Setters Tester
    def test_set_x_pos(self):
        self.main_character.set_x_pos(100)
        self.assertEqual(self.main_character.get_x_pos(), 100)

    def test_set_y_pos(self):
        self.main_character.set_y_pos(100)
        self.assertEqual(self.main_character.get_y_pos(), 100)

    def test_set_width(self):
        self.main_character.set_width(100)
        self.assertEqual(self.main_character.get_width(), 100)

    def test_set_height(self):
        self.main_character.set_height(100)
        self.assertEqual(self.main_character.get_height(), 100)

    def test_set_image(self):
        self.main_character.set_image(None)
        self.assertEqual(self.main_character.get_image(), None)

    def test_set_speed(self):
        self.main_character.set_speed(10)
        self.assertEqual(self.main_character.get_speed(), 10)

    def test_set_health(self):
        self.main_character.set_health(1000)
        self.assertEqual(self.main_character.get_health(), 1000)

    def test_set_attack_range(self):
        self.main_character.set_attack_range(10)
        self.assertEqual(self.main_character.get_attack_range(), 10)

    def test_set_attack_damage(self):
        self.main_character.set_attack_damage(10)
        self.assertEqual(self.main_character.get_attack_damage(), 10)

    def test_set_player_controlled(self):
        self.main_character.set_player_controlled(False)
        self.assertEqual(self.main_character.get_player_controlled(), False)


class enemy_setters_getters_testers(unittest.TestCase):

    # Example Setup
    def setUp(self):
        self.enemy = enemy(10, 10, 0, 0, 'enemy.png', 10, 2, 200, 10, 10)

    # Getters Testers
    def test_get_x_pos(self):
        self.assertEqual(self.enemy.get_x_pos(), 0)

    def test_get_y_pos(self):
        self.assertEqual(self.enemy.get_y_pos(), 0)

    def test_get_width(self):
        self.assertEqual(self.enemy.get_width(), 10)

    def test_get_height(self):
        self.assertEqual(self.enemy.get_height(), 10)

    def test_get_image(self):
        self.assertEqual(self.enemy.get_image(), 'enemy.png')

    def test_get_speed(self):
        self.assertEqual(self.enemy.get_speed(), 2)

    def test_get_health(self):
        self.assertEqual(self.enemy.get_health(), 10)

    def test_get_attack_range(self):
        self.assertEqual(self.enemy.get_attack_range(), 200)

    def test_get_attack_damage(self):
        self.assertEqual(self.enemy.get_attack_damage(), 10)

    def test_get_target(self):
        self.assertEqual(self.enemy.get_target(), 10)

    # Setters Tester
    def test_set_x_pos(self):
        self.enemy.set_x_pos(100)
        self.assertEqual(self.enemy.get_x_pos(), 100)

    def test_set_y_pos(self):
        self.enemy.set_y_pos(100)
        self.assertEqual(self.enemy.get_y_pos(), 100)

    def test_set_width(self):
        self.enemy.set_width(100)
        self.assertEqual(self.enemy.get_width(), 100)

    def test_set_height(self):
        self.enemy.set_height(100)
        self.assertEqual(self.enemy.get_height(), 100)

    def test_set_image(self):
        self.enemy.set_image(None)
        self.assertEqual(self.enemy.get_image(), None)

    def test_set_speed(self):
        self.enemy.set_speed(10)
        self.assertEqual(self.enemy.get_speed(), 10)

    def test_set_health(self):
        self.enemy.set_health(1000)
        self.assertEqual(self.enemy.get_health(), 1000)

    def test_set_attack_range(self):
        self.enemy.set_attack_range(10)
        self.assertEqual(self.enemy.get_attack_range(), 10)

    def test_set_attack_damage(self):
        self.enemy.set_attack_damage(10)
        self.assertEqual(self.enemy.get_attack_damage(), 10)

    def test_set_target(self):
        self.enemy.set_target(20)
        self.assertEqual(self.enemy.get_target(), 20)


# Game Windows Directory
class game_loop_setters_getters_tester(unittest.TestCase):

    # Example Setup
    def setUp(self):
        self.game_loop = game_loop()

    # Getters Testers
    def test_get_fps(self):
        self.assertEqual(self.game_loop.get_fps(), 60)

    # Setters Testers
    def test_set_fps(self):
        self.game_loop.set_fps(30)
        self.assertEqual(self.game_loop.get_fps(), 30)


class default_window_setters_getters_tester(unittest.TestCase):

    # Example Setup
    def setUp(self):
        self.default_window = default_window()

    # Getters Testers
    def test_get_game_name(self):
        self.assertEqual(self.default_window.get_game_name(), "ROB")

    def test_get_window_width(self):
        self.assertEqual(self.default_window.get_window_width(), 900)

    def test_get_window_height(self):
        self.assertEqual(self.default_window.get_window_height(), 700)

    def test_get_background(self):
        self.assertEqual(self.default_window.get_background(), (0, 0, 0))

    # Setters Testers
    def test_set_game_name(self):
        self.default_window.set_game_name("LEBRON JAMES")
        self.assertEqual(self.default_window.get_game_name(), "LEBRON JAMES")

    def test_set_window_width(self):
        self.default_window.set_window_width(500)
        self.assertEqual(self.default_window.get_window_width(), 500)

    def test_set_window_height(self):
        self.default_window.set_window_height(1000)
        self.assertEqual(self.default_window.get_window_height(), 1000)

    def test_set_grid_size(self):
        self.default_window.set_background((0, 1, 2))
        self.assertEqual(self.default_window.get_background(), (0, 1, 2))


class windows_setters_getters_testers(unittest.TestCase):

    # Example Setup
    def setUp(self):
        self.windows = windows()
        self.font = (pygame.font.SysFont(None, 30))

    # Getters Testers
    def test_get_windows(self):
        self.assertEqual(self.windows.get_menu_state(), "main_menu")

    # Setters Testers
    def test_set_windows(self):
        self.windows.set_menu_state("settings")
        self.assertEqual(self.windows.get_menu_state(), "settings")

    def test_set_font(self):
        self.windows.set_font(self.font)
        self.assertEqual(self.windows.get_font(), self.font)

    # Note: With this one, Gavin uses the Font in-built function from Pygame which returns an object.
    # Therefore, I can't really test the getter at the start because it has a certain address that changes.
