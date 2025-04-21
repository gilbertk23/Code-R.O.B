class default_window: 
	# Data Attributes
	__WIDTH = "Error"
	__HEIGHT = "Error"
	__background = "Error"
	__game_name = "Error"

	# Init
	def __init__(self, WIDTH, HEIGHT, background, game_name): 
		self.set_WIDTH(WIDTH)
		self.set_HEIGHT(HEIGHT)
		self.set_background(background)
		self.set_game_name(game_name)

	# Helpers

	# Getters
	def get_WIDTH(self): 
		return self.__WIDTH

	def get_HEIGHT(self): 
		return self.__HEIGHT

	def get_background(self): 
		return self.__background

	def get_game_name(self): 
		return self.__game_name

	# Setters
	def set_WIDTH(self, WIDTH): 
		self.__WIDTH = WIDTH

	def set_HEIGHT(self, HEIGHT): 
		self.__HEIGHT = HEIGHT

	def set_background(self, background): 
		self.__background = background

	def set_game_name(self, game_name): 
		self.__game_name = game_name

	# ToString
	def __str__(self):
		default_window_string = ""
		default_window_string += (f"Default_Window Data Attributes-->\n\t"	
			f"Width: {self.get_WIDTH()}\n\t"
			f"Height: {self.get_HEIGHT()}\n\t"
			f"Background: {self.get_background()}\n\t"
			f"Game_Name: {self.get_game_name()}\n\t")
		return default_window_string