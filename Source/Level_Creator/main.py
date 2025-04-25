import pygame

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
		# moon_square = pygame.image.load("Assets/moon-square.png")
		# light_slate_square = pygame.image.load("Assets/light-slate-square.png")
		# slate_square = pygame.image.load("Assets/slate-square.png")
		# player_16x = pygame.image.load("Assets/player-idle-1-16x.png")
		# dark_slate_square = pygame.image.load("Assets/dark-slate-square.png")
		# black_square = pygame.image.load("Assets/black-square.png")
		# green_square = pygame.image.load("Assets/green-square.png")
		# cat_square = pygame.image.load("Assets/cat.png")
	player_32x = pygame.image.load("Assets/player-idle-1-32x.png")
	void_tile = pygame.image.load("tile_assets/4_void.png")
	wall_tile = pygame.image.load("tile_assets/0_wall.png")
	grass_tile = pygame.image.load("tile_assets/1_grass.png")
	door_tile = pygame.image.load("tile_assets/2_door.png")
	goal_tile = pygame.image.load("tile_assets/3_goal.png")

	### scale tiles ###
		# moon_square = pygame.transform.scale(moon_square, (TILE_SIZE,TILE_SIZE))
		# light_slate_square = pygame.transform.scale(light_slate_square, (TILE_SIZE,TILE_SIZE))
		# slate_square = pygame.transform.scale(slate_square, (TILE_SIZE,TILE_SIZE))
		# player_16x = pygame.transform.scale(player_16x, (TILE_SIZE*PLAYER_SCALE,TILE_SIZE*PLAYER_SCALE))
		# dark_slate_square = pygame.transform.scale(dark_slate_square, (TILE_SIZE,TILE_SIZE))
		# black_square = pygame.transform.scale(black_square, (TILE_SIZE,TILE_SIZE))
		# green_square = pygame.transform.scale(green_square, (TILE_SIZE,TILE_SIZE))
		# cat_square = pygame.transform.scale(cat_square, (TILE_SIZE,TILE_SIZE))
	player_32x = pygame.transform.scale(player_32x, (TILE_SIZE*PLAYER_SCALE,TILE_SIZE*PLAYER_SCALE))
	void_tile = pygame.transform.scale(void_tile, (TILE_SIZE,TILE_SIZE))
	wall_tile = pygame.transform.scale(wall_tile, (TILE_SIZE,TILE_SIZE))
	grass_tile = pygame.transform.scale(grass_tile, (TILE_SIZE,TILE_SIZE))
	door_tile = pygame.transform.scale(door_tile, (TILE_SIZE,TILE_SIZE))
	goal_tile = pygame.transform.scale(goal_tile, (TILE_SIZE,TILE_SIZE))

	tile_catalogue = {
		".": void_tile,
		"0": wall_tile,
		"1": grass_tile,
		"2": door_tile,
		"3": goal_tile,
	}

	### construct void grid ###
	grid_instance = []
	for R in range(grid_size_input):
		for C in range(grid_size_input):
			grid_instance.append(".")
		# grid_instance.append("\n")
	# print grid struct
	print("@@ Initial Grid: @@")
	num = -1
	for i in grid_instance:
		num += 1
		if num % GRID_SIZE == 0:
			print()
		else:
			print(i, end="")
	# print("Initial Grid:")
	# 			for i in grid_instance:
	# 				if i == "\n":
	# 					print()
	# 				else:
	# 					print(i, end="")

	### game loop ###
	# player_pos = (100,100)
	# player_dimensions = (player_32x.get_rect()[2], player_32x.get_rect()[3])
	# get offset to center of player
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
					case pygame.K_1:
						print("SELECTION: 1_grass")
						selected_tile = "1"
					case pygame.K_2:
						print("SELECTION: 2_door")
						selected_tile = "2"
					case pygame.K_3:
						print("SELECTION: 3_goal")
						selected_tile = "3"
					case pygame.K_4:
						print("SELECTION: 4_void")
						selected_tile = "."
					# case pygame.K_5:
					# 	print("SELECTION: 5")
					# 	# selected_tile = tile_catalogue["5"]
					# case pygame.K_6:
					# 	print("SELECTION: 6")
					# 	# selected_tile = tile_catalogue["6"]
					# case pygame.K_7:
					# 	print("SELECTION: 7")
					# 	# selected_tile = tile_catalogue["7"]
					# case pygame.K_8:
					# 	print("SELECTION: 8")
					# 	# selected_tile = tile_catalogue["8"]
					# case pygame.K_9:
					# 	print("SELECTION: 9")
						# selected_tile = tile_catalogue["9"]
					case pygame.K_0:
						print("SELECTION: 0_wall")
						selected_tile = "0"
					case _:
						print("¡¡¡UNKNOWN SELECTION!!!")
			if event.type == pygame.MOUSEBUTTONDOWN:
				print("MOUSE CLICK:: X:" + str(mouse_pos[0]) + " Y:" + str(mouse_pos[1]))
				# NOTE: this doesn't work quite right. 
				# it has some weird issues trying to get the tiles on the right and bottom edges. 
				# I'm going to do some OOP refactoring and fix it in Level_Editor_v0.2
				for row in range(GRID_SIZE):
					for column in range(GRID_SIZE):
						# next two commented lines -> thoughts for refactoring
						# if mouse_pos[0] >= Tile.get_bounds(min_x) and mouse_pos[0] <= Tile.get_bounds(max_x):
						# 	if mouse_pos[1] >= Tile.get_bounds(min_y) and mouse_pos[1] <= Tile.get_bounds(max_y):
						if mouse_pos[0] >= ((TILE_SIZE*column)+MARGIN-TILE_SIZE) and mouse_pos[0] <= ((TILE_SIZE*column)+MARGIN):
							if mouse_pos[1] >= ((TILE_SIZE*row)+MARGIN-TILE_SIZE) and mouse_pos[1] <= ((TILE_SIZE*row)+MARGIN):
								index = (row*GRID_SIZE) + column - (GRID_SIZE+1)
								grid_instance[index] = selected_tile
				# print grid struct
				print("new Grid:")
				num = -1
				for i in grid_instance:
					num += 1
					if num % GRID_SIZE == 0:
						print()
					else:
						print(i, end="")
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
				game_canvas.blit(tile_catalogue[grid_instance[i]], ((TILE_SIZE*column)+MARGIN,(TILE_SIZE*row)+MARGIN))
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

### conditional execution of main() ###
if __name__ == '__main__':
	main()
