import pygame
from Spritesheet import Spritesheet

# version: 0.1

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
	# void_tile = pygame.image.load("tile_assets/4_void.png")
	# wall_tile = pygame.image.load("tile_assets/0_wall.png")
	# floor_tile = pygame.image.load("tile_assets/floor_metal_1.png")
	# door_tile = pygame.image.load("tile_assets/2_door.png")
	# goal_tile = pygame.image.load("tile_assets/3_goal.png")

	### scale tiles ###
	player_32x = pygame.transform.scale(player_32x, (TILE_SIZE*PLAYER_SCALE,TILE_SIZE*PLAYER_SCALE))
	# void_tile = pygame.transform.scale(void_tile, (TILE_SIZE,TILE_SIZE))
	# wall_tile = pygame.transform.scale(wall_tile, (TILE_SIZE,TILE_SIZE))
	# floor_tile = pygame.transform.scale(floor_tile, (TILE_SIZE,TILE_SIZE))
	# door_tile = pygame.transform.scale(door_tile, (TILE_SIZE,TILE_SIZE))
	# goal_tile = pygame.transform.scale(goal_tile, (TILE_SIZE,TILE_SIZE))

	# tile selector dict used in game loop
	spritesheet = Spritesheet("tile_assets/test_spritesheet.png", "tile_assets/test_metadata.json", TILE_SIZE)
	tile_catalogue = spritesheet.parse()


	### construct void grid ###
	# thoughts
		# grid_instance = [
		# 	[ # row 0
		# 		0, # col 0; id 0
		# 		0, # col 1; id 0
		# 		0, # col 2; id 0
		# 	],
		# 	[ # row 1
		# 		0, # col 0; id 0
		# 		1, # col 1; id 1
		# 		0, # col 2; id 0
		# 	],
		# ]
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
				# Old code from another of my projects, just a note for how things were done there:
	            	# if the mouse_pos is clicked on the button
		            # for btn in buttons.keys():
		            #     if buttons[btn].get_pos_x() <= mouse_pos[0] <= (buttons[btn].get_pos_x() + buttons[btn].get_width()) and \
		            #         buttons[btn].get_pos_y() <= mouse_pos[1] <= (buttons[btn].get_pos_y() + buttons[btn].get_height()):
		                    # 🡹🡹 check if mouse_pos X and Y positions are within button bounds 🡹🡹

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

### conditional execution of main() ###
if __name__ == '__main__':
	main()
