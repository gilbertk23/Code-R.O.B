import pygame
import json

class Spritesheet:
	__spritesheet_file = "NONE" # filename.png
	__spritesheet_image = "NONE"
	__metadata_file = "NONE" # filename.json
	__data = "NONE" # JSON object contaning metadata
	__tile_size = -1

	### Constructor ###
	def __init__(self, spritesheet_file, metadata_file, tile_size):
		self.set_spritesheet_file(spritesheet_file)
		self.set_metadata_file(metadata_file)
		self.set_tile_size(tile_size)
		self.set_spritesheet_image(pygame.image.load(self.get_spritesheet_file()))

	### Helpers ###
	def parse(self):
		"""
		@return: dict containing separated sprites
		"""
		with open(self.get_metadata_file()) as f:
			self.set_data(json.load(f))
		f.close()
		data_dict = self.get_data()
		image_dict = {}
		
		tile_size = self.get_tile_size()

		for key in data_dict.keys():
			print(key)
			width = data_dict[key]["width"]
			height = data_dict[key]["height"]
			pos_x = data_dict[key]["pos_x"]
			pos_y = data_dict[key]["pos_y"]

			new_sprite = pygame.Surface((width, height))
			new_sprite.blit(self.get_spritesheet_image(), (0,0), (pos_x, pos_y, width, height))
			new_sprite = pygame.transform.scale(new_sprite, (tile_size, tile_size))

			image_dict[key] = new_sprite
			print()
		return image_dict

	### Getters ###
	def get_spritesheet_file(self):
		return self.__spritesheet_file
	def get_metadata_file(self):
		return self.__metadata_file
	def get_data(self):
		return self.__data
	def get_spritesheet_image(self):
		return self.__spritesheet_image
	def get_tile_size(self):
		return self.__tile_size

	### Setters ###
	def set_spritesheet_file(self, file):
		 self.__spritesheet_file = file
	def set_metadata_file(self, file):
		 self.__metadata_file = file
	def set_data(self, data):
		self.__data = data
	def set_spritesheet_image(self, image):
		 self.__spritesheet_image = image
	def set_tile_size(self, tile_size):
		self.__tile_size = tile_size

	### __str___ ###
	def __str__(self):
		txt = ""
		txt += "Spritesheet info:\n"
		txt += "\tspritesheet_file: " + str(self.get_spritesheet_file()) + "\n"
		txt += "\tmetadata_file: " + str(self.get_metadata_file()) + "\n"
		txt += "\ttile size: " + str(self.get_tile_size()) + "\n"
		return txt