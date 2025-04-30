# Import Files/Modules
from Source.Maps.game_world import world
from Source.Maps.map_generator import map_generator
from Source.Interactors.main_character import player
from Source.Game_Windows.default_window import default_window
import pygame

pygame.init()

class game_loop:
    # Data Attributes
    __fps = -1

    # Init
    def __init__(self, fps=60):
        self.set_fps(fps)

        self.window = default_window().run_window()
        self.game_world = world(map_generator().generate_map_array())  # Generates new_map
        self.main_character = player()

        # Set Font
        self.font = pygame.font.Font('freesansbold.ttf', 30)

        self.text = self.font.render('CODE: ROB', True, (255, 0, 0))

    # Helpers
    def generate_new_map(self, game_world):
        if self.main_character.portal_active:
            game_world.reset_map()
            self.main_character.portal_active = False

    def draw_window(self, main_character: player, game_world: world) -> None:
        pygame.Surface.fill(self.window, (255, 255, 0))
        pygame.draw.rect(self.window, (255, 0, 0), (100, 100, default_window().get_window_width() - 200, default_window().get_window_height() - 200))
        self.window.blit(self.text, (default_window().get_window_width() / 2.7, default_window().get_window_height() / 20))
        game_world.draw(self.window)
        main_character.update_player(game_world.get_tile_list())
        self.generate_new_map(game_world)
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

            self.draw_window(self.main_character, self.game_world)  # Call function

        pygame.quit()  # quits the game loop and exits window

    # Getters
    def get_fps(self):
        return self.__fps

    # Setters
    def set_fps(self, fps):
        self.__fps = fps

    # To String
