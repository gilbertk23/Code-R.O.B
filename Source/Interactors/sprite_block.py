# Import Data Attributes
from Source.Interactors.config import *
from Source.Interactors.sprite_assets import sprite_assets
import pygame

class sprite_block(pygame.sprite.Sprite):
	# Data Attributes
	__sprite_list = []  # This is the current list of all sprites not just tile_blocks
	__start_block_x = -1
	__start_block_y = -1
	__block_width = -1
	__block_height = -1
	__sprite_type = None

	# Init
	def __init__(self, sprite_list=[], start_block_x=TILE_SIZE, start_block_y=TILE_SIZE, sprite_type=None):
		super().__init__()
		self.set_sprite_list(sprite_list)
		self.set_start_block_x(start_block_x * TILE_SIZE)
		self.set_start_block_y(start_block_y * TILE_SIZE)
		self.set_block_width(TILE_SIZE)
		self.set_block_height(TILE_SIZE)

		self.sprite_sheet = sprite_assets(sprite_type)
		self.sprite_asset = self.sprite_sheet.get_sprite_image()
		self._layer = GROUND_LAYER
		self.groups = self.get_sprite_list().blocks
		pygame.sprite.Sprite.__init__(self, self.groups)

		self.image = self.sprite_asset.get_sprite(self.sprite_sheet.sprite_x(), self.sprite_sheet.sprite_y(), self.get_block_width(), self.get_block_height())

		self.rect = self.image.get_rect()
		self.rect.x = start_block_x + 100
		self.rect.y = start_block_y + 100

	# Getters
	def get_sprite_list(self):
		return self.__sprite_list

	def get_start_block_x(self): 
		return self.__start_block_x

	def get_start_block_y(self): 
		return self.__start_block_y

	def get_block_width(self): 
		return self.__block_width

	def get_block_height(self): 
		return self.__block_height

	def get_sprite_type(self):
		return self.__sprite_type

	# Setters
	def set_sprite_list(self, sprite_list):
		self.__sprite_list = sprite_list

	def set_start_block_x(self, start_block_x): 
		self.__start_block_x = start_block_x

	def set_start_block_y(self, start_block_y): 
		self.__start_block_y = start_block_y

	def set_block_width(self, block_width): 
		self.__block_width = block_width

	def set_block_height(self, block_height): 
		self.__block_height = block_height

	def set_sprite_type(self, sprite_type):
		self.__sprite_type = sprite_type

	# ToString
	def __str__(self):
		tile_block_string = ""
		tile_block_string += (f"Tile_Block Data Attributes-->\n\t"	
			f"Start_Block_X: {self.get_start_block_x()}\n\t"
			f"Start_Block_Y: {self.get_start_block_y()}\n\t"
			f"Block_Width: {self.get_block_width()}\n\t"
			f"Block_Height: {self.get_block_height()}\n\t")
		return tile_block_string