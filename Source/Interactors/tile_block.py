# Import Data Attributes
from Source.Interactors.config import *
from Source.Interactors.sprite_sheet import sprite_sheet
import pygame

class tile_block(pygame.sprite.Sprite):
	# Data Attributes
	__start_block_x = -1
	__start_block_y = -1
	__block_width = -1
	__block_height = -1

	# Init
	def __init__(self, sprite_list, blocks_group, start_block_x=TILE_SIZE, start_block_y=TILE_SIZE):
		super().__init__()
		self.set_start_block_x(start_block_x * TILE_SIZE)
		self.set_start_block_y(start_block_y * TILE_SIZE)
		self.set_block_width(TILE_SIZE)
		self.set_block_height(TILE_SIZE)

		self.sprite_list = sprite_list
		self.terrain_sprite_sheet = sprite_sheet("Assets/FD_Ground_Tiles.png")
		self._layer = BLOCK_LAYER
		self.groups = self.sprite_list.all_sprites, blocks_group
		pygame.sprite.Sprite.__init__(self, self.groups)

		self.image = self.terrain_sprite_sheet.get_sprite(100, 448, self.get_block_width(), self.get_block_height())

		self.rect = self.image.get_rect()
		self.rect.x = start_block_x + 100
		self.rect.y = start_block_y + 100

	# Helpers
	def return_blocks(self, block_type):
		if block_type == 0:
			self.image = self.terrain_sprite_sheet.get_sprite(100, 400, self.get_block_width(), self.get_block_height())
		if block_type == 3:
			self.image = self.terrain_sprite_sheet.get_sprite(100, 200, self.get_block_width(), self.get_block_height())

	# Getters
	def get_start_block_x(self): 
		return self.__start_block_x

	def get_start_block_y(self): 
		return self.__start_block_y

	def get_block_width(self): 
		return self.__block_width

	def get_block_height(self): 
		return self.__block_height

	# Setters
	def set_start_block_x(self, start_block_x): 
		self.__start_block_x = start_block_x

	def set_start_block_y(self, start_block_y): 
		self.__start_block_y = start_block_y

	def set_block_width(self, block_width): 
		self.__block_width = block_width

	def set_block_height(self, block_height): 
		self.__block_height = block_height

	# ToString
	def __str__(self):
		tile_block_string = ""
		tile_block_string += (f"Tile_Block Data Attributes-->\n\t"	
			f"Start_Block_X: {self.get_start_block_x()}\n\t"
			f"Start_Block_Y: {self.get_start_block_y()}\n\t"
			f"Block_Width: {self.get_block_width()}\n\t"
			f"Block_Height: {self.get_block_height()}\n\t")
		return tile_block_string