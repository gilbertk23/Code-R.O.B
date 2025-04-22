class buttons: 
	# Data Attributes
	__width = "Error"
	__height = "Error"
	__startx = "Error"
	__starty = "Error"
	__background_color = "Error"
	__border_color = "Error"

	# Init
	def __init__(self, width, height, startx, starty, background_color, border_color): 
		self.set_width(width)
		self.set_height(height)
		self.set_startx(startx)
		self.set_starty(starty)
		self.set_background_color(background_color)
		self.set_border_color(border_color)

	# Helpers

	# Getters
	def get_width(self): 
		return self.__width

	def get_height(self): 
		return self.__height

	def get_startx(self): 
		return self.__startx

	def get_starty(self): 
		return self.__starty

	def get_background_color(self): 
		return self.__background_color

	def get_border_color(self): 
		return self.__border_color

	# Setters
	def set_width(self, width): 
		self.__width = width

	def set_height(self, height): 
		self.__height = height

	def set_startx(self, startx): 
		self.__startx = startx

	def set_starty(self, starty): 
		self.__starty = starty

	def set_background_color(self, background_color): 
		self.__background_color = background_color

	def set_border_color(self, border_color): 
		self.__border_color = border_color

	# ToString
	def __str__(self):
		buttons_string = ""
		buttons_string += (f"Buttons Data Attributes-->\n\t"	
			f"Width: {self.get_width()}\n\t"
			f"Height: {self.get_height()}\n\t"
			f"Startx: {self.get_startx()}\n\t"
			f"Starty: {self.get_starty()}\n\t"
			f"Background_Color: {self.get_background_color()}\n\t"
			f"Border_Color: {self.get_border_color()}\n\t")
		return buttons_string