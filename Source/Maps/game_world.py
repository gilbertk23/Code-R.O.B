import pygame
from map_generator import map_generator

WIDTH, HEIGHT = 900, 600  # Pygame Window Width and Height
FPS = 60  # Sets the Frames Per Second for game
Py_Window = pygame.display.set_mode((WIDTH, HEIGHT))  # Create py window
pygame.display.set_caption("Game Platformer")  # Window Game Caption

def draw_window():  # Function for background arguments
	world.draw()
	pygame.display.update()  # Update game loop

class World:  # Create new class world
	def __init__(self, data):
		self.tile_list = []

		row_count = 0

		GRID_SIZE = 20  # Size of each grid
		for row in data:  # Iterate through each row
			col_count = 0
			for tile in row:  # Iterate through each tile
				if tile == 1:  # Tile 1 = Border Block
					map_generator().border_block(self.tile_list, GRID_SIZE, col_count, row_count)

				if tile == 2:  # Tile 2 = Portal Block
					map_generator().portal_block(self.tile_list, GRID_SIZE, col_count, row_count)

				if tile == 3:  # Tile 4 = Dirt block
					map_generator().floor_block(self.tile_list, GRID_SIZE, col_count, row_count)

				if tile == 4:  # Tile 3 = Clear Block
					map_generator().chest_block(self.tile_list, GRID_SIZE, col_count, row_count)

				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			Py_Window.blit(tile[0], tile[1])

test = map_generator()
world = World(test.generate_map_array())

test.print_array()

# Def main contains main game loop components only
def main():
	clock = pygame.time.Clock()  # Control time of main function
	run = True
	while run:
		clock.tick(FPS)  # Controls the speed of the while loop
		for event in pygame.event.get():  # For loop looks for events
			if event.type == pygame.QUIT:  # User quit window
				run = False

		draw_window()  # Call function

	pygame.quit()  # quits the game loop and exits window


if __name__ == "__main__":  # Ensures code only runs file in file
	main()