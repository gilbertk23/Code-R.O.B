# Import Files/Modules
from Interactors.config import *

class sprite:
	# Data Attributes
	__width = -1
	__height = -1
	__x_pos = -1
	__y_pos = -1
	__image = "Error"
	__sprite_char = "Error"

	# Init
	def __init__(self, width=CHAR_WIDTH, height=CHAR_HEIGHT, x_pos=CENTER_X, y_pos=CENTER_Y, image=DEFAULT_IMAGE):

		self.set_width(width)
		self.set_height(height)
		self.set_x_pos(x_pos)
		self.set_y_pos(y_pos)
		self.set_image(image)

	# Helpers

	# Getters
	def get_width(self):
		return self.__width

	def get_height(self):
		return self.__height

	def get_x_pos(self):
		return self.__x_pos

	def get_y_pos(self):
		return self.__y_pos

	def get_image(self):
		return self.__image

	def get_sprite_char(self):
		return self.__sprite_char

	# Setters
	def set_width(self, width):
		self.__width = width

	def set_height(self, height):
		self.__height = height

	def set_x_pos(self, x_pos):
		self.__x_pos = x_pos

	def set_y_pos(self, y_pos):
		self.__y_pos = y_pos

	def set_image(self, image):
		self.__image = image

	def set_sprite_char(self, sprite_char):
		self.__sprite_char = sprite_char

	# ToString
	def __str__(self):
		sprite_string = ""
		sprite_string += (f"Sprite Data Attributes-->\n\t"	
			f"Width: {self.get_width()}\n\t"
			f"Height: {self.get_height()}\n\t"
			f"X_Pos: {self.get_x_pos()}\n\t"
			f"Y_Pos: {self.get_y_pos()}\n\t"
			f"Image: {self.get_image()}\n\t")
		return sprite_string