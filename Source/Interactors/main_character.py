class main_character: 
	# Data Attributes
	__texture = "Error"
	__height = "Error"
	__width = "Error"
	__movement_speed = "Error"

	# Init
	def __init__(self, texture, height, width, movement_speed): 
		self.set_texture(texture)
		self.set_height(height)
		self.set_width(width)
		self.set_movement_speed(movement_speed)

	# Helpers

	# Getters
	def get_texture(self): 
		return self.__texture

	def get_height(self): 
		return self.__height

	def get_width(self): 
		return self.__width

	def get_movement_speed(self): 
		return self.__movement_speed

	# Setters
	def set_texture(self, texture): 
		self.__texture = texture

	def set_height(self, height): 
		self.__height = height

	def set_width(self, width): 
		self.__width = width

	def set_movement_speed(self, movement_speed): 
		self.__movement_speed = movement_speed

	# ToString
	def __str__(self):
		main_character_string = ""
		main_character_string += (f"Main_Character Data Attributes-->\n\t"	
			f"Texture: {self.get_texture()}\n\t"
			f"Height: {self.get_height()}\n\t"
			f"Width: {self.get_width()}\n\t"
			f"Movement_Speed: {self.get_movement_speed()}\n\t")
		return main_character_string