import pygame
import json
from Spritesheet import Spritesheet

# version: 0.2

def main():
	### user input ###
	grid_size_input = int(input("Grid size (square, enter one integer):"))

	### pygame initialization ###
	pygame.init()
	pygame.display.set_caption("R.O.B game")

	### constants ###
	SCALE = 3 # factor to scale all assets by
	PLAYER_SCALE = 1 # in case we decide we want the player to be bigger/smaller in the future
	TILE_SIZE = 16*SCALE # scale images by a factor SCALE (source image sizes are all 16x16 px)
	MARGIN = TILE_SIZE*2 # margin = border around play area
	GRID_SIZE = grid_size_input # how many cells in rows & columns
	SCREEN_HEIGHT = (TILE_SIZE*GRID_SIZE)+(MARGIN*2) 
	SCREEN_WIDTH = (TILE_SIZE*GRID_SIZE)+(MARGIN*2)
	UI_FONT = pygame.font.Font('Assets/Minecraftia-Regular.ttf', 35)
	COLORS = {
	    # pre-set colors for reduced duplication
	    "black": (0, 0, 0),
	    "white": (255, 255, 255),
	    "red": (255, 0, 0),
	    "green": (0, 255, 0),
	    "blue": (0, 0, 255),
	}
	screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
	game_canvas = pygame.Surface((SCREEN_HEIGHT,SCREEN_WIDTH))

	### load tile images from disk ###
	player_32x = pygame.image.load("Assets/player-idle-1-32x.png")

	### scale tiles ###
	player_32x = pygame.transform.scale(player_32x, (TILE_SIZE*PLAYER_SCALE,TILE_SIZE*PLAYER_SCALE))

	# tile catalogue dict used in game loop for asset rendering
	spritesheet_file = "tile_assets/test_spritesheet.png"
	spritesheet_metadata_file = "tile_assets/test_spritesheet.json"
	spritesheet = Spritesheet(spritesheet_file, spritesheet_metadata_file, TILE_SIZE)
	tile_catalogue = spritesheet.parse()

	### construct void grid ###
	grid_instance = []
	for R in range(grid_size_input):
		grid_instance.append([])
		for C in range(grid_size_input):
			grid_instance[R].append("0")

	# print grid struct
	print("@@ Initial Grid: @@")
	print_grid_log(grid_instance)


	### game loop ###
		# player_pos = (100,100)
		# player_dimensions = (player_32x.get_rect()[2], player_32x.get_rect()[3])
		## get offset to center of player
		# player_offset_x = player_dimensions[0]/2
		# player_offset_y = player_dimensions[1]/2
	selected_tile = "0"
	running = True
	while running:
		# store the (x,y) coordinates of mouse position (as a tuple)
		mouse_pos = pygame.mouse.get_pos()

		### event handling ###
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				# tile selection -> 1,2,3,4,5,6,7,8,9,0
				match(event.key):
					case pygame.K_0:
						print("SELECTION: void_tile")
						selected_tile = "0"
					case pygame.K_1:
						print("SELECTION: floor_tile")
						selected_tile = "1"
					case pygame.K_2:
						print("SELECTION: door_tile")
						selected_tile = "2"
					case pygame.K_3:
						print("SELECTION: wall_tile")
						selected_tile = "3"
					case pygame.K_s:
						print("¡¡SAVE MAP!!")
						save_map(grid_instance)
					case pygame.K_l:
						print("¡¡LOAD MAP (wip)!!")
						save_map(grid_instance)
					case _:
						print("¡¡¡UNKNOWN SELECTION!!!")
			if event.type == pygame.MOUSEBUTTONDOWN:
				print("MOUSE CLICK:: X:" + str(mouse_pos[0]) + " Y:" + str(mouse_pos[1]))
				for row in range(GRID_SIZE):
					for column in range(GRID_SIZE):
						if mouse_pos[0] >= ((TILE_SIZE*column)+MARGIN) and mouse_pos[0] <= ((TILE_SIZE*column)+MARGIN+TILE_SIZE):
							if mouse_pos[1] >= ((TILE_SIZE*row)+MARGIN) and mouse_pos[1] <= ((TILE_SIZE*row)+MARGIN+TILE_SIZE):
								grid_instance[row][column] = selected_tile
				# print grid struct
				print("new Grid:")
				print_grid_log(grid_instance)

		### clear previous frame ###
		screen.fill(COLORS["white"])

		### render map ###
		i = 0
		new_tile = ""
		for row in range(GRID_SIZE):
			for column in range(GRID_SIZE):
				game_canvas.blit(tile_catalogue[grid_instance[row][column]], ((TILE_SIZE*column)+MARGIN,(TILE_SIZE*row)+MARGIN))
				i += 1

		### display game_canvas (map) ###
		screen.blit(game_canvas, (0,0))

		### display player ###
		# screen.blit(player_32x, ((player_pos[0]-player_offset_x),(player_pos[1]-player_offset_y)))

		### game logic ###
		# < game logic goes here! >

		### push frame to screen ###
		pygame.display.update()

	### no longer running, quit application ###
	pygame.quit()
	exit()


def print_grid_log(grid_instance):
	for r in grid_instance:
		print()
		for c in r:
			print(c, end="")
	print()

def save_map(grid_instance, spritesheet_file):
	# TODO:
		# get user input for level name
		# save spritesheet reference (filename)

	new_map = {
		"name": "test_level",
		"tile_map": grid_instance,
		"tile_spritesheet": spritesheet_file
	}
	file = json.dumps(new_map, indent=4)
	with open("test_level.json", "w") as f:
		f.write(file)

def load_map()
	# TODO:
		# select what map to load (filesystem dialogue?)
		# parse selected json file
		# load data into variables and pass back to main()
	pass

### conditional execution of main() ###
if __name__ == '__main__':
	main()
