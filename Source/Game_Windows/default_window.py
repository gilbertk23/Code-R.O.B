#Import Files/Modules

class default_window:
	# Data Attributes
	__game_name = "Error"
	__window_width = -1
	__window_height = -1
	__background = (-1, -1, -1)

	# Init
	def init(self, game_name="ROB", window_width=900, window_height=700, background=(0, 0, 0)):
		self.set_game_name(game_name)
		self.set_window_width(window_width)
		self.set_window_height(window_height)
		self.set_background(background)

	# Helpers

	# Getters
	def get_game_name(self):
		return self.__game_name

	def get_window_width(self):
		return self.__window_width

	def get_window_height(self):
		return self.__window_height

	def get_background(self):
		return self.__background

	# Setters
	def set_game_name(self, game_name):
		self.__game_name = game_name

	def set_window_width(self, window_width):
		self.__window_width = window_width

	def set_window_height(self, window_height):
		self.__window_height = window_height

	def set_background(self, background):
		self.__background = background

	# To String

