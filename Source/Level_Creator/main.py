import pygame

def main():
	
	### pygame initialization ###
	pygame.init()
	pygame.display.set_caption("R.O.B game")

	# constants
	SCALE = 2 
	PLAYER_SCALE = 4
	TILE_SIZE = 16*SCALE # scale images by a factor SCALE (source image sizes are all 16x16 px)
	MARGIN = TILE_SIZE*2 # margin = border around play area
	GRID_SIZE = 32 # how many cells in rows & columns
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

	# load tile images from disk
	moon_square = pygame.image.load("Assets/moon-square.png")
	light_slate_square = pygame.image.load("Assets/light-slate-square.png")
	slate_square = pygame.image.load("Assets/slate-square.png")
	# dark_slate_square = pygame.image.load("Assets/dark-slate-square.png")
	# black_square = pygame.image.load("Assets/black-square.png")
	# green_square = pygame.image.load("Assets/green-square.png")
	# cat_square = pygame.image.load("Assets/cat.png")
	player_16x = pygame.image.load("Assets/player-idle-1-16x.png")
	player_32x = pygame.image.load("Assets/player-idle-1-32x.png")

	# scale tiles
	moon_square = pygame.transform.scale(moon_square, (TILE_SIZE,TILE_SIZE))
	light_slate_square = pygame.transform.scale(light_slate_square, (TILE_SIZE,TILE_SIZE))
	slate_square = pygame.transform.scale(slate_square, (TILE_SIZE,TILE_SIZE))
	# dark_slate_square = pygame.transform.scale(dark_slate_square, (TILE_SIZE,TILE_SIZE))
	# black_square = pygame.transform.scale(black_square, (TILE_SIZE,TILE_SIZE))
	# green_square = pygame.transform.scale(green_square, (TILE_SIZE,TILE_SIZE))
	# cat_square = pygame.transform.scale(cat_square, (TILE_SIZE,TILE_SIZE))
	player_16x = pygame.transform.scale(player_16x, (TILE_SIZE*PLAYER_SCALE,TILE_SIZE*PLAYER_SCALE))
	player_32x = pygame.transform.scale(player_32x, (TILE_SIZE*PLAYER_SCALE,TILE_SIZE*PLAYER_SCALE))

	# placeholder map creation (eventually will load map from file)
	til = [
		moon_square,
		slate_square,
		moon_square,
		light_slate_square,
		moon_square,
		slate_square,
		# green_square,
		# black_square,
		# cat_square,
	]
	tiles = []
	for t in range(2000):
		for a in til:
			tiles.append(a)


	### game loop ###
	running = True
	while running:
		# event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# clear previous frame
		screen.fill(COLORS["white"])

		# render map
		i = 0
		for row in range(GRID_SIZE):
			for column in range(GRID_SIZE):
				game_canvas.blit(tiles[i], ((TILE_SIZE*column)+MARGIN,(TILE_SIZE*row)+MARGIN))
				i += 1
		screen.blit(game_canvas, (0,0))


		screen.blit(player_16x, ((TILE_SIZE*10),(TILE_SIZE*5)))
		screen.blit(player_32x, ((TILE_SIZE*10),(TILE_SIZE*15)))

		# < game logic goes here! >

		# push frame to screen
		pygame.display.update()

	# no longer running, quit application
	pygame.quit()
	exit()

if __name__ == '__main__':
	main()