# Import Files/Modules
from Source.Maps.game_world import world
from Source.Maps.map_generator import map_generator
from Source.Interactors.main_character import player
from Source.Game_Windows.default_window import default_window
import pygame

class game_loop:
    # Data Attributes
    __fps = -1

    # Init
    def __init__(self, fps=60):
        self.set_fps(fps)

        self.window = default_window().run_window()
        self.game_world = world(map_generator().generate_map_array())  # Generates new_map
        self.main_character = player()

    # Helpers
    def generate_new_map(self, world, main_character):
        if main_character.portal_active:
            world.reset_map()
            main_character.portal_active = False

    def draw_window(self, world: world, main_character: player) -> None:
        pygame.Surface.fill(self.window, (0, 0, 0))
        world.draw(self.window)
        main_character.update_player(world.get_tile_list())
        self.generate_new_map(world, main_character)
        pygame.display.update()

    def run_game(self):
        pygame.init()

        clock = pygame.time.Clock()  # Control time of main function
        run = True
        while run:
            clock.tick(60)
            for event in pygame.event.get():  # For loop looks for events
                if event.type == pygame.QUIT:  # User quit window
                    run = False

            self.draw_window(self.game_world, self.main_character)  # Call function

        pygame.quit()  # quits the game loop and exits window

    # Getters
    def get_fps(self):
        return self.__fps

    # Setters
    def set_fps(self, fps):
        self.__fps = fps

    # To String
