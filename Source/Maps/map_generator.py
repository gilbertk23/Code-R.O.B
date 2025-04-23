# Import Files/Modules
import random
import pygame
import os

class map_generator:
	# Data Attributes
	__min_width = "Error"
	__max_width = "Error"
	__min_height = "Error"
	__max_height = "Error"
	__min_enemies = "Error"
	__max_enemies = "Error"
	__min_chests = "Error"
	__max_chests = "Error"
	__current_score = "Error"
	__map_count = "Error"

	# Init
	def __init__(self, min_width=10, max_width=20, min_height=10, max_height=20, min_enemies=0, max_enemies=30, min_chests=0, max_chests=10, current_score=0, map_count=0):
		self.set_min_width(min_width)
		self.set_max_width(max_width)
		self.set_min_height(min_height)
		self.set_max_height(max_height)
		self.set_min_enemies(min_enemies)
		self.set_max_enemies(max_enemies)
		self.set_min_chests(min_chests)
		self.set_max_chests(max_chests)
		self.set_current_score(current_score)
		self.set_map_count(map_count)

		self.set_row_size = random.randint(self.get_min_height(), self.get_max_height())
		self.set_col_size = random.randint(self.get_min_width(), self.get_max_width())
		self.set_chest_num = random.randint(self.get_min_chests(), self.get_max_chests())

	# Helpers
	def clear_block(self, tile_list, GRID_SIZE, col_count, row_count):  # Tile 0
		Dark_Block = pygame.image.load(os.path.join('Assets', 'Clear Block.png'))
		img = pygame.transform.scale(Dark_Block, (GRID_SIZE, GRID_SIZE))  # Tranforming tile to size of grid
		img_rect = img.get_rect()  # Convert image to rectangle
		img_rect.x = col_count * GRID_SIZE  # Find x value of image
		img_rect.y = row_count * GRID_SIZE  # Find y value of image
		tile = (img, img_rect)  # Save tile as tuple
		tile_list.append(tile)  # Adding tile to list

	def border_block(self, tile_list, GRID_SIZE, col_count, row_count):  # Tile 1
		Dark_Block = pygame.image.load(os.path.join('Assets', 'Dark Block.jpg'))
		img = pygame.transform.scale(Dark_Block, (GRID_SIZE, GRID_SIZE))  # Tranforming tile to size of grid
		img_rect = img.get_rect()  # Convert image to rectangle
		img_rect.x = col_count * GRID_SIZE  # Find x value of image
		img_rect.y = row_count * GRID_SIZE  # Find y value of image
		tile = (img, img_rect)  # Save tile as tuple
		tile_list.append(tile)  # Adding tile to list

	def portal_block(self, tile_list, GRID_SIZE, col_count, row_count):  # Tile 2
		Grey_Block = pygame.image.load(os.path.join('Assets', 'Grey Block.jpg'))
		img = pygame.transform.scale(Grey_Block, (GRID_SIZE, GRID_SIZE))  # Tranforming tile to size of grid
		img_rect = img.get_rect()  # Convert image to rectangle
		img_rect.x = col_count * GRID_SIZE  # Find x value of image
		img_rect.y = row_count * GRID_SIZE  # Find y value of imag
		tile = (img, img_rect)  # Save tile as tuple
		tile_list.append(tile)  # Adding tile to list

	def floor_block(self, tile_list, GRID_SIZE, col_count, row_count):  # Tile 3
		Grass_Block = pygame.image.load(os.path.join('Assets', 'grass.png'))
		img = pygame.transform.scale(Grass_Block, (GRID_SIZE, GRID_SIZE))  # Tranforming tile to size of grid
		img_rect = img.get_rect()  # Convert image to rectangle
		img_rect.x = col_count * GRID_SIZE  # Find x value of image
		img_rect.y = row_count * GRID_SIZE  # Find y value of image
		tile = (img, img_rect)  # Save tile as tuple
		tile_list.append(tile)  # Adding tile to list
		return tile_list

	def chest_block(self, tile_list, GRID_SIZE, col_count, row_count):  # Tile 4
		Clear_Block = pygame.image.load(os.path.join('Assets', 'Clear Block.png'))
		img = pygame.transform.scale(Clear_Block, (GRID_SIZE, GRID_SIZE))  # Tranforming tile to size of grid
		img_rect = img.get_rect()  # Convert image to rectangle
		img_rect.x = col_count * GRID_SIZE  # Find x value of image
		img_rect.y = row_count * GRID_SIZE  # Find y value of image
		tile = (img, img_rect)  # Save tile as tuple
		tile_list.append(tile)  # Adding tile to list
		return tile_list

	def get_row_size(self):
		return self.set_row_size  # Returns the size of the map row size

	def get_col_size(self):
		return self.set_col_size  # Returns the size of the map column size

	def get_row_portal(self):
		row_portal = int(self.get_row_size()/2)  # Set position of the portal on the row
		return row_portal  # Return position

	def get_col_portal(self):
		col_portal = int(self.get_col_size()/2)  # Set position of the portal on the column
		return col_portal  # Return position

	def get_chest_pos(self):
		total_chests = self.set_chest_num  # Get the total number of chests per map
		chest_list = []  # Create empty chest list

		for items in range(total_chests):  # Iterate through the range of total chests
			column = random.randint(1, self.get_col_size() - 1)  # Set random column value
			row = random.randint(1, self.get_row_size() - 1)  # Set random row value
			chest_list.append([column, row])  # Chest instance set to row and column

		return chest_list  # Return chest list

	def generate_chests(self, map_array):
		for columns in self.get_chest_pos():  # Iterate through columns on the chest positions
			map_array[columns[1]][columns[0]] = 4  # If available set position to chest block

		return map_array  # Return map array

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

			self.generate_chests(map_array)  # Plot Chests onto map array

			return map_array  # Return middle map

	# Function to print viewable array
	def print_array(self):
		for items in self.generate_map_array():
			print(items)

	# Getters
	def get_min_width(self): 
		return self.__min_width

	def get_max_width(self): 
		return self.__max_width

	def get_min_height(self): 
		return self.__min_height

	def get_max_height(self): 
		return self.__max_height

	def get_min_enemies(self): 
		return self.__min_enemies

	def get_max_enemies(self): 
		return self.__max_enemies

	def get_min_chests(self): 
		return self.__min_chests

	def get_max_chests(self): 
		return self.__max_chests

	def get_current_score(self): 
		return self.__current_score

	def get_map_count(self): 
		return self.__map_count

	# Setters
	def set_min_width(self, min_width): 
		self.__min_width = min_width

	def set_max_width(self, max_width): 
		self.__max_width = max_width

	def set_min_height(self, min_height): 
		self.__min_height = min_height

	def set_max_height(self, max_height): 
		self.__max_height = max_height

	def set_min_enemies(self, min_enemies): 
		self.__min_enemies = min_enemies

	def set_max_enemies(self, max_enemies): 
		self.__max_enemies = max_enemies

	def set_min_chests(self, min_chests): 
		self.__min_chests = min_chests

	def set_max_chests(self, max_chests): 
		self.__max_chests = max_chests

	def set_current_score(self, current_score): 
		self.__current_score = current_score

	def set_map_count(self, map_count): 
		self.__map_count = map_count

	# ToString
	def __str__(self):
		map_generator_string = ""
		map_generator_string += (f"Map_Generator Data Attributes-->\n\t"	
			f"Min_Width: {self.get_min_width()}\n\t"
			f"Max_Width: {self.get_max_width()}\n\t"
			f"Min_Height: {self.get_min_height()}\n\t"
			f"Max_Height: {self.get_max_height()}\n\t"
			f"Min_Enemies: {self.get_min_enemies()}\n\t"
			f"Max_Enemies: {self.get_max_enemies()}\n\t"
			f"Min_Chests: {self.get_min_chests()}\n\t"
			f"Max_Chests: {self.get_max_chests()}\n\t"
			f"Current_Score: {self.get_current_score()}\n\t"
			f"Map_Count: {self.get_map_count()}\n\t")
		return map_generator_string