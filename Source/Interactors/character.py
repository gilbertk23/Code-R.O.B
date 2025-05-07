# Import Files/Modules
from Interactors.sprite import sprite
import pygame
import os

class character(sprite, pygame.sprite.Sprite):
	# Data Attributes
	__health = "Error"
	__speed = "Error"
	__attack_range = "Error"
	__attack_damage = "Error"

	# Init
	def __init__(self, sprite_sheet, width, height, x_pos, y_pos, image, health, speed, attack_range, attack_damage):
		super().__init__(width, height, x_pos, y_pos, image)
		self.set_health(health)
		self.set_speed(speed)
		self.set_attack_range(attack_range)
		self.set_attack_damage(attack_damage)

		self.sprite_sheet = sprite_sheet
		self.groups = self.sprite_sheet.all_sprites  # Get all sprites group
		pygame.sprite.Sprite.__init__(self, self.groups)

		self.character = pygame.image.load(os.path.join('Assets', image))
		self.image = pygame.transform.scale(self.character, (width, height))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x_pos, y_pos)

	# Helpers

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