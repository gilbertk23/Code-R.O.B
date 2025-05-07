#Import Files/Modules
import pygame
from Interactors.config import *

class default_window:
	# Data Attributes
	__window_width = -1
	__window_height = -1
	__background = (-1, -1, -1)
	__game_name = "Error"
	__font = "Error"

	# Init
	def __init__(self, window_width=WIDTH, window_height=HEIGHT, background=WHITE, game_name=GAME_NAME, font=FONT1):
		self.set_window_width(window_width)
		self.set_window_height(window_height)
		self.set_background(background)
		self.set_game_name(game_name)
		self.set_font(pygame.font.Font(font, 30))

		# Title Font
		self.title_text = self.get_font().render('CODE: ROB', True, (255, 0, 0))

	# Helpers
	def init_window(self):
		game_window = pygame.display.set_mode((self.get_window_width(), self.get_window_height()))  # Init window
		game_window.fill(self.get_background())  # Set background
		self.draw_title(game_window)
		return game_window  # Return game_window

	def draw_title(self, game_window):
		pygame.draw.rect(game_window, (255, 0, 0),(50, 50, self.get_window_width() - 250, self.get_window_height() - 250))
		game_window.blit(self.title_text, (self.get_window_width() / 2.7, self.get_window_height() / 20))
		pygame.display.set_caption(self.get_game_name())  # Set the name

	# Getters
	def get_window_width(self):
		return self.__window_width

	def get_window_height(self):
		return self.__window_height

	def get_background(self):
		return self.__background

	def get_game_name(self):
		return self.__game_name

	def get_font(self):
		return self.__font

	# Setters
	def set_window_width(self, window_width):
		self.__window_width = window_width

	def set_window_height(self, window_height):
		self.__window_height = window_height

	def set_background(self, background):
		self.__background = background

	def set_game_name(self, game_name):
		self.__game_name = game_name

	def set_font(self, font):
		self.__font = font

	# To String

