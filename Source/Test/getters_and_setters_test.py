from Source.Maps.map_generator import map_generator
from Source.Maps.game_world import world
from Source.Interactors.main_character import player
from Source.Game_Windows.game_loop import game_loop
from Source.Game_Windows.default_window import default_window

import unittest


class map_generator_setters_getters_tester(unittest.TestCase):

    # Example Setup
    def setUp(self):
        self.world = map_generator()

    # Getters Testers
    def test_get_min_width(self):
        self.assertEqual(self.world.get_min_width(), 10)

    def test_get_max_width(self):
        self.assertEqual(self.world.get_max_width(), 20)

    def test_get_min_height(self):
        self.assertEqual(self.world.get_min_height(), 10)

    def test_get_max_height(self):
        self.assertEqual(self.world.get_max_height(), 20)

    def test_get_min_enemies(self):
        self.assertEqual(self.world.get_min_enemies(), 0)

    def test_get_max_enemies(self):
        self.assertEqual(self.world.get_max_enemies(), 30)

    def test_get_min_chest(self):
        self.assertEqual(self.world.get_min_chests(), 0)

    def test_get_max_chest(self):
        self.assertEqual(self.world.get_max_chests(), 10)

    def test_get_current_score(self):
        self.assertEqual(self.world.get_current_score(), 0)

    def test_get_map_count(self):
        self.assertEqual(self.world.get_map_count(), 0)

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

    def test_set_min_chest(self):
        self.world.set_min_chests(20)
        self.assertEqual(self.world.get_min_chests(), 20)

    def test_set_max_chest(self):
        self.world.set_max_chests(40)
        self.assertEqual(self.world.get_max_chests(), 40)

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

    def test_get_width(self):
        self.assertEqual(self.world.get_width(), 900)

    def test_get_height(self):
        self.assertEqual(self.world.get_height(), 700)

    def test_get_game_name(self):
        self.assertEqual(self.world.get_game_name(), "ROB")

    def test_get_grid_size(self):
        self.assertEqual(self.world.get_grid_size(), 20)

    # Setters Testers
    def test_set_game_world(self):
        self.world.set_game_map([1, 2, 3, 4])
        self.assertEqual(self.world.get_game_map(), [1, 2, 3, 4])

    def test_set_width(self):
        self.world.set_width(500)
        self.assertEqual(self.world.get_width(), 500)

    def test_set_height(self):
        self.world.set_height(1000)
        self.assertEqual(self.world.get_height(), 1000)

    def test_set_game_name(self):
        self.world.set_game_name("LEBRON JAMES")
        self.assertEqual(self.world.get_game_name(), "LEBRON JAMES")

    def test_set_grid_size(self):
        self.world.set_grid_size(25)
        self.assertEqual(self.world.get_grid_size(), 25)


class main_character_setters_getters_tester(unittest.TestCase):

    # Example Setup
    def setUp(self):
        self.player = player()

    # Getters Testers
    def test_get_x_pos(self):
        self.assertEqual(self.player.get_x_pos(), 10)

    def test_get_y_pos(self):
        self.assertEqual(self.player.get_y_pos(), 10)

    def test_get_char_width(self):
        self.assertEqual(self.player.get_char_width(), 10)

    def test_get_char_height(self):
        self.assertEqual(self.player.get_char_height(), 10)

    def test_get_char_speed(self):
        self.assertEqual(self.player.get_char_speed(), 3)

    def test_get_char_health(self):
        self.assertEqual(self.player.get_char_health(), 100)

    # Setters Tester
    def test_set_x_pos(self):
        self.player.set_x_pos(100)
        self.assertEqual(self.player.get_x_pos(), 100)

    def test_set_y_pos(self):
        self.player.set_y_pos(100)
        self.assertEqual(self.player.get_y_pos(), 100)

    def test_set_char_width(self):
        self.player.set_char_width(100)
        self.assertEqual(self.player.get_char_width(), 100)

    def test_set_char_height(self):
        self.player.set_char_height(100)
        self.assertEqual(self.player.get_char_height(), 100)

    def test_set_char_speed(self):
        self.player.set_char_speed(10)
        self.assertEqual(self.player.get_char_speed(), 10)

    def test_set_char_health(self):
        self.player.set_char_health(1000)
        self.assertEqual(self.player.get_char_health(), 1000)


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
