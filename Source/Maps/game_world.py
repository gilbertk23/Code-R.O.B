import pygame
from Source.Maps.map_generator import map_generator

class world:
	# Data Attributes
	__game_map = []
	__tile_size = -1

	# Init
	def __init__(self, game_map=[], tile_size=20):
		self.set_game_map(game_map)

		self.set_tile_size(tile_size)
		self.tile_list = []

		self.map = map_generator()

		self.generate_textures()

	# Helpers
	def map_textures(self, tile, row_count, col_count):
		map_generator().set_blocks(tile, self.tile_list, self.get_tile_size(), col_count, row_count)

	def generate_textures(self):
		row_count = 0
		for row in self.get_game_map():  # Iterate through each row
			col_count = 0
			for tile in row:  # Iterate through each tile
				self.map_textures(tile, row_count, col_count)
				col_count += 1
			row_count += 1

	def draw(self, screen: pygame.Surface) -> None:
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])

	# Getters
	def get_game_map(self):
		return self.__game_map

	def get_tile_size(self):
		return self.__tile_size

	# Setters
	def set_game_map(self, game_map):
		self.__game_map = game_map

	def set_tile_size(self, tile_size):
		self.__tile_size = tile_size