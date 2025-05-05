# Import Files/Modules
from Source.Game_Windows.default_window import default_window
from Source.Interactors.sprite import sprite
import pygame
import os

class character(sprite):
	# Data Attributes
	__health = "Error"
	__speed = "Error"
	__attack_range = "Error"
	__attack_damage = "Error"

	# Init
	def __init__(self, width, height, x_pos, y_pos, image, health, speed, attack_range, attack_damage):
		super().__init__(width, height, x_pos, y_pos, image)
		self.set_health(health)
		self.set_speed(speed)
		self.set_attack_range(attack_range)
		self.set_attack_damage(attack_damage)

		# Sets character
		self.character = pygame.image.load(os.path.join('Assets', image))
		self.image = pygame.transform.scale(self.character, (width, height))
		self.character_rect = self.image.get_rect() # Turns character into a rectangle

		# Sets window
		self.game_window = default_window().init_window()

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

	def track_player(self):
		pass

	def update_character(self):
		self.key_press()
		self.game_window.blit(self.image, (self.get_x_pos(), self.get_y_pos()))

	# Getters
	def get_health(self): 
		return self.__health

	def get_speed(self): 
		return self.__speed

	def get_attack_range(self): 
		return self.__attack_range

	def get_attack_damage(self): 
		return self.__attack_damage

	# Setters
	def set_health(self, health): 
		self.__health = health

	def set_speed(self, speed): 
		self.__speed = speed

	def set_attack_range(self, attack_range): 
		self.__attack_range = attack_range

	def set_attack_damage(self, attack_damage): 
		self.__attack_damage = attack_damage

	# ToString
	def __str__(self):
		character_string = ""
		character_string += (f"Character Data Attributes-->\n\t"	
			f"Health: {self.get_health()}\n\t"
			f"Speed: {self.get_speed()}\n\t"
			f"Attack_Range: {self.get_attack_range()}\n\t"
			f"Attack_Damage: {self.get_attack_damage()}\n\t")
		return character_string