import pygame
from Source.Maps.map_generator import map_generator

class World:
	# Data Attributes
	__game_map = []
	__width = -1
	__height = -1
	__game_name = "Error"
	__grid_size = -1

	# Init
	def __init__(self, game_map, width=900, height=700, game_name="ROB", grid_size=20):
		self.set_game_map(game_map)
		self.set_width(width)
		self.set_height(height)
		self.set_game_name(game_name)
		self.set_grid_size(grid_size)
		self.tile_list = []

		self.game_window = pygame.display.set_mode((width, height))
		pygame.display.set_caption(game_name)

		self.map = map_generator()

		self.generate_textures()

	# Helpers
	def map_textures(self, tile, row_count, col_count):
		if tile == 1:  # Tile 1 = Border Block
			map_generator().border_block(self.tile_list, self.get_grid_size(), col_count, row_count)
		if tile == 2:  # Tile 2 = Portal Block
			map_generator().portal_block(self.tile_list, self.get_grid_size(), col_count, row_count)
		if tile == 3:  # Tile 4 = Dirt block
			map_generator().floor_block(self.tile_list, self.get_grid_size(), col_count, row_count)
		if tile == 4:  # Tile 3 = Clear Block
			map_generator().chest_block(self.tile_list, self.get_grid_size(), col_count, row_count)

	def generate_textures(self):
		row_count = 0
		for row in self.get_game_map():  # Iterate through each row
			col_count = 0
			for tile in row:  # Iterate through each tile
				self.map_textures(tile, row_count, col_count)
				col_count += 1
			row_count += 1

	def reset_board(self):
		self.game_window.fill((0, 0, 0))
		map_generator().generate_map_array()
		self.draw()

	def draw(self):
		for tile in self.tile_list:
			self.game_window.blit(tile[0], tile[1])

	# Getters
	def get_game_map(self):
		return self.__game_map

	def get_width(self):
		return self.__width

	def get_height(self):
		return self.__height

	def get_game_name(self):
		return self.__game_name

	def get_grid_size(self):
		return self.__grid_size

	# Setters
	def set_game_map(self, game_map):
		self.__game_map = game_map

	def set_width(self, width):
		self.__width = width

	def set_height(self, height):
		self.__height = height

	def set_game_name(self, game_name):
		self.__game_name = game_name

	def set_grid_size(self, grid_size):
		self.__grid_size = grid_size
