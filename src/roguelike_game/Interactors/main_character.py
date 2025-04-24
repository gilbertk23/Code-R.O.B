import pygame
import os
from ..Maps.map_generator import map_generator
from ..Maps.game_world import World


WIDTH, HEIGHT = 900, 600  # Pygame Window Width and Height
FPS = 60  # Sets the Frames Per Second for game
Py_Window = pygame.display.set_mode((WIDTH, HEIGHT))  # Create py window
pygame.display.set_caption("Game Platformer")  # Window Game Caption

class Player:  # Create player class
    def __init__(self, x, y):
        Character = pygame.image.load(os.path.join('Assets', 'Player Sprite.png'))
        Player_Width, Player_Height = 10, 20
        self.image = pygame.transform.scale(Character, (Player_Width, Player_Height))
        self.rect = self.image.get_rect()  # Turn character into rectangle
        self.rect.x = x  # X position
        self.rect.y = y  # Y position
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.jumped = False
        self.health = 0
        self.Is_coliding = False

        self.map = map_generator()
        self.world = World(self.map.generate_map_array())



    def update(self):
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx -= 5
        if key[pygame.K_d]:
            dx += 5
        if key[pygame.K_w]:
                dy -= 5
        if key[pygame.K_s]:
            dy += 5

        # Check for collisions
        for tile in self.map.generate_map_array():
            if tile[0] > self.rect.x:

                self.Is_coliding = True


                self.rect.x = 20
                self.rect.y = 20

        # Update Player Coordinates
        self.rect.x += dx
        self.rect.y += dy

        # Drawing Player onto screen
        Py_Window.blit(self.image, self.rect)
        # pygame.draw.rect(Py_Window, (255, 255, 255), self.rect, 2)
