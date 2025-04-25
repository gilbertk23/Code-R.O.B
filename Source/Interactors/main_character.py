import pygame
import os

from Source.Game_Windows.default_window import default_window

class player:
	# Data Attributes
	__x_pos = -1
	__y_pos = -1
	__player_pos = -1
	__char_width = -1
	__char_height = -1
	__char_speed = -1
	__char_health = -1

	# Init
	def __init__(self, x_pos=10, y_pos=10, player_pos=(10, 10), char_width=10, char_height=10, char_speed=3, char_health=100, game_map=[]):
		self.set_x_pos(x_pos)
		self.set_y_pos(y_pos)
		self.set_player_pos(player_pos)
		self.set_char_width(char_width)
		self.set_char_height(char_height)
		self.set_char_speed(char_speed)
		self.set_char_health(char_health)
		self.game_map = game_map

		# Set Player
		self.character = pygame.image.load(os.path.join('Assets', 'Player Sprite.png'))
		self.image = pygame.transform.scale(self.character, (char_width, char_height))
		self.char_rect = self.image.get_rect()  # Turn character into rectangle

		# Get Window
		self.game_window = default_window().run_window()

		self.portal_active = False

	# Helpers
	def key_press(self):
		key = pygame.key.get_pressed()
		if key[pygame.K_a]:
			self.set_x_pos(self.get_x_pos() - 1)
		if key[pygame.K_d]:
			self.set_x_pos(self.get_x_pos() + 1)
		if key[pygame.K_w]:
			self.set_y_pos(self.get_y_pos() - 1)
		if key[pygame.K_s]:
			self.set_y_pos(self.get_y_pos() + 1)

	def update_player(self, tile_list):
		self.key_press()
		self.detect_collision(tile_list)
		self.set_player_pos((self.get_x_pos(), self.get_y_pos()))
		self.game_window.blit(self.image, (self.get_player_pos()))

	def detect_collision(self, tile_list):
		for tile in tile_list:
			if self.get_x_pos() <= tile[1][0] / 20:
				self.portal_active = True

	# Getters
	def get_x_pos(self):
		return self.__x_pos

	def get_y_pos(self):
		return self.__y_pos

	def get_player_pos(self):
		return self.__player_pos

	def get_char_width(self):
		return self.__char_width

	def get_char_height(self):
		return self.__char_height

	def get_char_speed(self):
		return self.__char_speed

	def get_char_health(self):
		return self.__char_health

	# Setters
	def set_x_pos(self, x_pos):
		self.__x_pos = x_pos

	def set_y_pos(self, y_pos):
		self.__y_pos = y_pos

	def set_player_pos(self, player_pos):
		self.__player_pos = player_pos

	def set_char_width(self, char_width):
		self.__char_width = char_width

	def set_char_height(self, char_height):
		self.__char_height = char_height

	def set_char_speed(self, char_speed):
		self.__char_speed = char_speed

	def set_char_health(self, char_health):
		self.__char_health = char_health

	# To String