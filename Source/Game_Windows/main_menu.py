# Import Files/Modules
from Source.Game_Windows.default_window import default_window
import pygame

class Main_Menu(default_window):
	# Data Attributes
	__font = None
	__border_color = None
	__start_game_rect_color = None
	__settings_rect_color = None
	__credits_rect_color = None
	__box_start = -1
	__box_end = -1

	# Init
	def __init__(self, WIDTH=900, HEIGHT=700, background=(100, 100, 255), game_name="Rob", font="none", border_color=(0, 0, 0), start_game_rect_color=(50, 50, 255), settings_rect_color=(100, 100, 255), credits_rect_color=(100, 100, 255), box_start=0, box_end=0):
		super().__init__(WIDTH, HEIGHT, background, game_name)
		self.set_font(font)
		self.set_border_color(border_color)
		self.set_start_game_rect_color(start_game_rect_color)
		self.set_settings_rect_color(settings_rect_color)
		self.set_credits_rect_color(credits_rect_color)
		self.set_box_start(box_start)
		self.set_box_end(box_end)

		self.title_font = pygame.font.SysFont('C:\Windows\Fonts\CALISTBI.TTF', 50)
		self.option_font = pygame.font.SysFont('Comic Sans MS', 40)
		self.background = pygame.display.set_mode((super().get_WIDTH(), super().get_HEIGHT()))
		self.background.fill(self.get_background())
		pygame.display.set_caption(self.get_game_name())

	# Helpers
	def main_menu(self):
		# Title Box
		pygame.draw.rect(self.background, (50, 50, 255), pygame.Rect(50, 20, 800, 100), 5, 5, 5, 5, 5, 5)
		game_title = self.title_font.render("ROB", True, (0, 0, 0), (100, 100, 255))
		self.background.blit(game_title, (450, self.get_HEIGHT()/10))

		# Start Game Box
		pygame.draw.rect(self.background, self.get_start_game_rect_color(), pygame.Rect(300, 175, 300, 90))
		pygame.draw.rect(self.background, self.get_border_color(), pygame.Rect(300, 175, 300, 90), 1, 1, 1, 1, 1, 1)
		start_game_title = self.option_font.render("Start Game", True, (0, 0, 0), self.get_start_game_rect_color())
		self.background.blit(start_game_title, (340, 200))

		# Settings Box
		pygame.draw.rect(self.background, self.get_settings_rect_color(), pygame.Rect(300, 300, 300, 90))
		pygame.draw.rect(self.background, self.get_border_color(), pygame.Rect(300, 300, 300, 90), 1, 1, 1, 1, 1, 1)
		start_game_title = self.option_font.render("Settings", True, (0, 0, 0), self.get_settings_rect_color())
		self.background.blit(start_game_title, (370, 325))

		# Credits Box
		pygame.draw.rect(self.background, self.get_credits_rect_color(), pygame.Rect(300, 425, 300, 90))
		pygame.draw.rect(self.background, self.get_border_color(), pygame.Rect(300, 425, 300, 90), 1, 1, 1, 1, 1, 1)
		start_game_title = self.option_font.render("Credits", True, (0, 0, 0), self.get_credits_rect_color())
		self.background.blit(start_game_title, (380, 450))

	def get_hover(self):
		x, y = pygame.mouse.get_pos()
		print(x, y)
		# detect mouse hover over start game button
		if 300 <= x <= 600 and 177 <= y <= 265:
			self.set_start_game_rect_color((0, 0, 255))

		# detect mouse hover over settings button
		elif 300 <= x <= 600 and 300 <= y <= 390:
			self.set_settings_rect_color((0, 0, 255))

		# detect mouse hover over credits button
		elif 300 <= x <= 600 and 425 <= y <= 515:
			self.set_credits_rect_color((0, 0, 255))

		else:
			self.set_start_game_rect_color((75, 75, 255))
			self.set_settings_rect_color((75, 75, 255))
			self.set_credits_rect_color((75, 75, 255))

	def get_click(self):
		x, y = pygame.mouse.get_pos()

		# detect mouse click on start game button
		if 300 <= x <= 600 and 177 <= y <= 265:
			print("Hel0o")

		# detect mouse click on settings button
		elif 300 <= x <= 600 and 300 <= y <= 390:
			print('gsdf=')

		# detect mouse click on credits button
		elif 300 <= x <= 600 and 425 <= y <= 515:
			print('sdfj=')
			self.close_menu()

	def close_menu(self):
		pygame.quit()

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