# Import Files/Modules
from pygame.sprite import Sprite

from Source.Interactors.sprite_sheet import sprite_sheet
from Source.Game_Windows.default_window import default_window
from Source.Interactors.character import character
from Source.Interactors.load_sprites import load_sprites
from Source.Maps.map_generator import map_generator
from Source.Game_Windows.windows import windows
from Source.Interactors.enemy import enemy
from Source.Maps.game_world import world
from Source.Interactors.config import *
import random
import pygame

# Initialize pygame
pygame.init()

class game_loop:
    __fps = -1

    def __init__(self, fps=FPS):
        self.set_fps(fps)

        # Initialize Game Window
        self.game_window = default_window().init_window()

        # Set Current Window
        self.current_window = windows(self.game_window)

        # Create world map
        self.world_array = map_generator()
        self.get_sprites = load_sprites(self.game_window, self.world_array, self.world_array.get_num_enemies(), self.world_array.generate_map_array())

        self.enemies = []

    def update_screen(self):
        self.game_window.fill(BLACK)
        self.current_window.draw_window()
        self.create_game_world()
        pygame.display.update()

    def create_game_world(self):
        if self.current_window.get_menu_state() == "play_game":
            self.get_sprites.update(self.game_window)


    def run_game(self):
        clock = pygame.time.Clock()
        run = True

        while run:
            clock.tick(self.get_fps())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.update_screen()

        pygame.quit()

    def get_fps(self):
        return self.__fps

    def set_fps(self, fps):
        self.__fps = fps

