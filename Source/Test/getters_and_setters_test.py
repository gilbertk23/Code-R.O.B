from Source.Maps.map_generator import map_generator
from Source.Maps.game_world import World

import unittest


class MapGeneratorSettersGettersTester(unittest.TestCase):\

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


class GameWorldGeneratorSettersGettersTester(unittest.TestCase):

    # Example Setup
    def setUp(self):
        self.test = map_generator()
        self.test_array = self.test.generate_map_array()
        self.world = World(self.test_array)


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
