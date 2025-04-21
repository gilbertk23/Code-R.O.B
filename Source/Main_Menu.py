# Import Files/Modules
from default_window import default_window


class Main_Menu(default_window):
	# Data Attributes
	__font = "Error"
	__border_color = "Error"
	__start_game_rect_color = "Error"
	__settings_rect_color = "Error"
	__credits_rect_color = "Error"
	__box_start = "Error"
	__box_end = "Error"

	# Init
	def __init__(self, WIDTH, HEIGHT, background, game_name, font, border_color, start_game_rect_color, settings_rect_color, credits_rect_color, box_start, box_end):
		super().__init__(WIDTH, HEIGHT, background, game_name)
		self.set_font(font)
		self.set_border_color(border_color)
		self.set_start_game_rect_color(start_game_rect_color)
		self.set_settings_rect_color(settings_rect_color)
		self.set_credits_rect_color(credits_rect_color)
		self.set_box_start(box_start)
		self.set_box_end(box_end)

	# Helpers

	# Getters
	def get_font(self): 
		return self.__font

	def get_border_color(self): 
		return self.__border_color

	def get_start_game_rect_color(self): 
		return self.__start_game_rect_color

	def get_settings_rect_color(self): 
		return self.__settings_rect_color

	def get_credits_rect_color(self): 
		return self.__credits_rect_color

	def get_box_start(self): 
		return self.__box_start

	def get_box_end(self): 
		return self.__box_end

	# Setters
	def set_font(self, font): 
		self.__font = font

	def set_border_color(self, border_color): 
		self.__border_color = border_color

	def set_start_game_rect_color(self, start_game_rect_color): 
		self.__start_game_rect_color = start_game_rect_color

	def set_settings_rect_color(self, settings_rect_color): 
		self.__settings_rect_color = settings_rect_color

	def set_credits_rect_color(self, credits_rect_color): 
		self.__credits_rect_color = credits_rect_color

	def set_box_start(self, box_start): 
		self.__box_start = box_start

	def set_box_end(self, box_end): 
		self.__box_end = box_end

	# ToString
	def __str__(self):
		Main_Menu_string = ""
		Main_Menu_string += (f"Main Menu Data Attributes-->\n\t"
			f"{super().__str__}\n\t"
			f"Font: {self.get_font()}\n\t"
			f"Border_Color: {self.get_border_color()}\n\t"
			f"Start_Game_Rect_Color: {self.get_start_game_rect_color()}\n\t"
			f"Settings_Rect_Color: {self.get_settings_rect_color()}\n\t"
			f"Credits_Rect_Color: {self.get_credits_rect_color()}\n\t"
			f"Box_Start: {self.get_box_start()}\n\t"
			f"Box_End: {self.get_box_end()}\n\t")
		return Main_Menu_string