# Import Files/Modules
from Source.Interactors.config import *
import random
import pygame
import os


class map_generator:
	# Data Attributes
	__row_size = "Error"
	__col_size = "Error"
	__min_enemies = "Error"
	__max_enemies = "Error"
	__current_score = "Error"
	__map_count = "Error"

	# Init
	def __init__(self, row_size=ROW_SIZE, col_size=COL_SIZE, min_enemies= 30, max_enemies= 30, current_score=0, map_count=1):
		self.set_row_size(row_size)
		self.set_col_size(col_size)
		self.set_min_enemies(min_enemies)
		self.set_max_enemies(max_enemies)
		self.set_current_score(current_score)
		self.set_map_count(map_count)


	# Helpers
	def get_map_blocks(self, block_type):
		map_blocks = {0: 'Clear Block.png',
					  1: 'Dark Block.jpg',
					  2: 'Grey Block.jpg',
					  3: 'grass.png',
					  4: 'Clear Block.png'}

		return map_blocks[block_type]

	def set_blocks(self, tile_type, tile_list, grid_size, col_count, row_count):
		block_type = pygame.image.load(os.path.join('Assets', self.get_map_blocks(tile_type)))
		self.set_image_block(block_type, tile_list, grid_size, col_count, row_count)

	def set_image_block(self, block_type, tile_list, grid_size, col_count, row_count):
		img = pygame.transform.scale(block_type, (grid_size, grid_size))
		img_rect = img.get_rect()  # Convert image to rectangle
		img_rect.x = col_count * grid_size  # Find x value of image
		img_rect.y = row_count * grid_size  # Find y value of image
		tile = (img, img_rect)  # Save tile as tuple
		tile_list.append(tile)  # Adding tile to list

	def get_num_enemies(self):
		enemy_num = random.randint(self.get_min_enemies(), self.get_max_enemies())
		return enemy_num

	def get_row_portal(self):
		row_portal = int(self.get_row_size()/2)  # Set position of the portal on the row
		return row_portal  # Return position

	def get_col_portal(self):
		col_portal = int(self.get_col_size()/2)  # Set position of the portal on the column
		return col_portal  # Return position

	def get_left_portal_pos(self):
		left_pos = [(self.get_col_size() + 100) - 30, (self.get_row_size() * 20 + 200) / 2 + 15]
		return left_pos

	def get_right_portal_pos(self):
		right_pos = [(self.get_col_size() * 20 + 100) - 15, (self.get_row_size() * 20 + 200) / 2 + 15]
		return right_pos

	def get_top_portal_pos(self):
		top_pos = [(self.get_col_size() * 11 + 80), (self.get_row_size() + 80)]
		return top_pos

	def get_bottom_portal_pos(self):
		bottom_pos = [(self.get_col_size() * 11 + 80), ((self.get_row_size() * 20) + 85)]
		return bottom_pos

	def generate_column_border(self):
		left_distance = self.get_col_size() - self.get_col_portal()  # Left distance value of portal position

		top_border = [1] * left_distance  # Create top_border list
		top_border.append(2)  # Append portal block

		right_distance = self.get_col_size() - len(top_border)  # Right distance value of portal position

		for list in range(right_distance):  # Iterate through range of right_distance
			top_border.append(1)  # Append border walls

		return top_border  # Return top border

	def detect_left_row_portal(self, row, middle_map):
		if row == self.get_row_portal():  # If the row value is equal to portal position
			middle_map.append(2)  # border wall set to portal block

		else:
			middle_map.append(1)  # If not equal set border wall to border block

		return middle_map  # Return middle map

	def detect_right_row_portal(self, row, middle_map):
		if row == self.get_row_portal():  # If the row value is equal to portal position
			middle_map.append(2)  # border wall set to portal block

		else:
			middle_map.append(1) # If not equal set border wall to border block

		return middle_map  # Return middle map

	def generate_middle_map(self, row):
		middle_map = []  # Instantiate middle map list
		self.detect_left_row_portal(row, middle_map)  # Call detect_left_row_portal

		if row != self.get_row_size() - 2:
			for rows in range(self.get_col_size() - 2):
				middle_map.append(3)  # Append floor to middle map list

			self.detect_right_row_portal(row, middle_map)  # Call detect_right_row_portal

		else:
			middle_map = self.generate_column_border()  # Make bottom map border

		return middle_map  # Return middle map

	def generate_map_array(self):
		map_array = []  # Instantiate map_array
		for columns in range(self.get_col_size()):  # Iterate through the range of column size
			map_array.append(self.generate_column_border())  # Append column border
			for rows in range(self.get_row_size() - 1):  # Iterate through range of border size
				map_array.append(self.generate_middle_map(rows))  # Append middle map
			return map_array  # Return middle map

	# Function to print viewable array
	def print_array(self):
		for items in self.generate_map_array():
			print(items)

	# Getters
	def get_row_size(self):
		return self.__row_size

	def get_col_size(self):
		return self.__col_size

	def get_min_enemies(self): 
		return self.__min_enemies

	def get_max_enemies(self): 
		return self.__max_enemies

	def get_current_score(self): 
		return self.__current_score

	def get_map_count(self): 
		return self.__map_count

	# Setters
	def set_row_size(self, row_size):
		self.__row_size = row_size

	def set_col_size(self, col_size):
		self.__col_size = col_size

	def set_min_enemies(self, min_enemies): 
		self.__min_enemies = min_enemies

	def set_max_enemies(self, max_enemies): 
		self.__max_enemies = max_enemies

	def set_current_score(self, current_score): 
		self.__current_score = current_score

	def set_map_count(self, map_count): 
		self.__map_count = map_count

	# ToString
	def __str__(self):
		map_generator_string = ""
		map_generator_string += (f"Map_Generator Data Attributes-->\n\t"	
			f"Row_Size: {self.get_row_size()}\n\t"
			f"Col_Size: {self.get_col_size()}\n\t"
			f"Min_Enemies: {self.get_min_enemies()}\n\t"
			f"Max_Enemies: {self.get_max_enemies()}\n\t"
			f"Current_Score: {self.get_current_score()}\n\t"
			f"Map_Count: {self.get_map_count()}\n\t")
		return map_generator_string