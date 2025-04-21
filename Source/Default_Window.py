class Default_Window: 
	# Data Attributes
	__WIDTH = "Error"
	__HEIGHT = "Error"
	__Background = "Error"
	__Game_Name = "Error"

	# Init
	def __init__(self, WIDTH, HEIGHT, Background, Game_Name): 
		self.set_WIDTH(WIDTH)
		self.set_HEIGHT(HEIGHT)
		self.set_Background(Background)
		self.set_Game_Name(Game_Name)

	# Helpers

	# Getters
	def get_WIDTH(self): 
		return self.__WIDTH

	def get_HEIGHT(self): 
		return self.__HEIGHT

	def get_Background(self): 
		return self.__Background

	def get_Game_Name(self): 
		return self.__Game_Name

	# Setters
	def set_WIDTH(self, WIDTH): 
		self.__WIDTH = WIDTH

	def set_HEIGHT(self, HEIGHT): 
		self.__HEIGHT = HEIGHT

	def set_Background(self, Background): 
		self.__Background = Background

	def set_Game_Name(self, Game_Name): 
		self.__Game_Name = Game_Name

	# ToString
	def __str__(self):
		Default_Window_string = ""
		Default_Window_string += (f"Default_Window Data Attributes-->\n\t"	
			f"Width: {self.get_WIDTH()}\n\t"
			f"Height: {self.get_HEIGHT()}\n\t"
			f"Background: {self.get_Background()}\n\t"
			f"Game_Name: {self.get_Game_Name()}\n\t")
		return Default_Window_string