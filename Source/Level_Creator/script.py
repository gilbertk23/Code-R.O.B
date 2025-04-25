

import pygame 
import random 
  

  
# Object class 
class Sprite(pygame.sprite.Sprite): 
    def __init__(self, image, pos_x, pos_y): 
        super().__init__() 
  
        self.image = image # insert image
        self.rect = self.image.get_rect() #define rect
        self.rect.x = pos_x # set up sprite location
        self.rect.y = pos_y # set up sprite location
  
def main():
	# GLOBAL VARIABLES 
	COLOR = (255, 100, 98) 
	SURFACE_COLOR = (167, 255, 100) 
	WIDTH = 500
	HEIGHT = 500
	RED = (255, 0, 0) 
	  
	pygame.init() 
	  
	size = (WIDTH, HEIGHT) 
	screen = pygame.display.set_mode(size) 
	pygame.display.set_caption("Creating Sprite") 
	  
	all_sprites_list = pygame.sprite.Group() 
	player_32x = pygame.image.load("Assets/player-idle-1-32x.png")
	object_ = Sprite(player_32x, 30, 30)
	all_sprites_list.add(object_) 
	  
	exit = True
	clock = pygame.time.Clock() 
	while exit: 
	    for event in pygame.event.get(): 
	        if event.type == pygame.QUIT:
	            exit = False
	        if event.type == pygame.MOUSEBUTTONDOWN:
	        	mouse_pos = pygame.mouse.get_pos()
	        	object_.rect.x = mouse_pos[0]
	        	object_.rect.y = mouse_pos[1]
	  
	    all_sprites_list.update() 
	    screen.fill(SURFACE_COLOR) 
	    all_sprites_list.draw(screen) 
	    pygame.display.flip() 
	    clock.tick(60) 

if __name__ == '__main__':
	main()