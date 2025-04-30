import pygame
import json
from Spritesheet import Spritesheet

def main():
	### user input ###
	# how many cells in rows & columns
	grid_size = int(input("Grid size (square, enter one integer):"))

	### constants ###
	SCALE = 3 # factor to scale all assets by
	PLAYER_SCALE = 1 # in case we decide we want the player to be bigger/smaller in the future
	TILE_SIZE = 16*SCALE # scale images by a factor SCALE (source image sizes are all 16x16 px)
	MARGIN = TILE_SIZE*2 # margin = border around play area
	SCREEN_HEIGHT = (TILE_SIZE*grid_size)+(MARGIN*2) 
	SCREEN_WIDTH = (TILE_SIZE*grid_size)+(MARGIN*2)
	# UI_FONT = pygame.font.Font('Assets/Minecraftia-Regular.ttf', 35)

	### pygame initialization ###
	pygame.init()
	pygame.display.set_caption("R.O.B game")
	screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
	game_canvas = pygame.Surface((SCREEN_HEIGHT,SCREEN_WIDTH))

		### load player assets ###
		# player_32x = pygame.image.load("Assets/player-idle-1-32x.png")
		# player_32x = pygame.transform.scale(player_32x, (TILE_SIZE*PLAYER_SCALE,TILE_SIZE*PLAYER_SCALE))

	# tile catalogue dict used in game loop for asset rendering
	spritesheet_file = "Assets/tile_spritesheet.png"
	tile_catalogue = load_sprites(spritesheet_file, TILE_SIZE)

	### construct void grid ###
	grid_instance = []
	for R in range(grid_size):
		grid_instance.append([])
		for C in range(grid_size):
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
	paint_tile = "0"
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
				# load / save -> l / s
				match(event.key):
					case pygame.K_0:
						print("SELECTION: void_tile")
						paint_tile = "0"
					case pygame.K_1:
						print("SELECTION: floor_tile")
						paint_tile = "1"
					case pygame.K_2:
						print("SELECTION: door_tile")
						paint_tile = "2"
					case pygame.K_3:
						print("SELECTION: wall_tile")
						paint_tile = "3"
					case pygame.K_s:
						print("¡¡SAVE MAP!!")
						save_map(grid_instance, spritesheet_file)
					case pygame.K_l:
						print("¡¡LOAD MAP (wip, now it just clears the tiles)!!")
						# TODO add dialogue choice: (new map) or (load from file)
						new_map_data = load_map()
						grid_instance = new_map_data["tile_map"]
						grid_size = new_map_data["grid_size"]
						tile_catalogue = load_sprites(new_map_data["spritesheet_file"], TILE_SIZE) 
					case _:
						print("¡¡¡UNKNOWN SELECTION!!!")
			if event.type == pygame.MOUSEBUTTONDOWN:
				print("MOUSE CLICK:: X:" + str(mouse_pos[0]) + " Y:" + str(mouse_pos[1]))
				for row in range(grid_size):
					for column in range(grid_size):
						if mouse_pos[0] >= ((TILE_SIZE*column)+MARGIN) and mouse_pos[0] <= ((TILE_SIZE*column)+MARGIN+TILE_SIZE):
							if mouse_pos[1] >= ((TILE_SIZE*row)+MARGIN) and mouse_pos[1] <= ((TILE_SIZE*row)+MARGIN+TILE_SIZE):
								# change the clicked tile
								grid_instance[row][column] = paint_tile
				# print grid struct
				print("new Grid:")
				print_grid_log(grid_instance)

		### clear previous frame ###
		screen.fill((255,255,255))

		### render map ###
		i = 0
		new_tile = ""
		for row in range(len(grid_instance)):
			for column in range(len(grid_instance[row])):
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
	# TODO: get user input for level name
	grid_size = len(grid_instance[0])
	new_map = {
		"name": "test_level",
		"spritesheet_file": spritesheet_file,
		"grid_size": grid_size,
		"tile_map": grid_instance,
	}
	file = json.dumps(new_map, indent=4)
	with open("new_level.json", "w") as f:
		f.write(file)

def load_map(map_name=""):
	# TODO:
		# select what map to load (filesystem dialogue?)
	if map_name == "":
		map_name = "empty_level.json"
	with open(map_name, "r") as f:
		data = json.load(f)
	return data

def load_sprites(spritesheet_file, tile_size):
	spritesheet_metadata_file = spritesheet_file.replace(".png", ".json")
	spritesheet = Spritesheet(spritesheet_file, spritesheet_metadata_file, tile_size)
	tile_catalogue = spritesheet.parse()
	return tile_catalogue

### conditional execution of main() ###
if __name__ == '__main__':
	main()
