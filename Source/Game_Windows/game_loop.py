# Import Files/Modules
from Source.Maps.game_world import world
from Source.Maps.map_generator import map_generator
from Source.Interactors.main_character import player
from Source.Game_Windows.default_window import default_window
from Source.Assets import preset_maps
import pygame

pygame.init()

class game_loop:
    # Data Attributes
    __fps = -1

    # Init
    def __init__(self, fps=60):
        self.set_fps(fps)

        self.window = default_window().run_window()
        """
        self.generated_map = map_generator()  # Generates new_map
        self.game_world = world(self.generated_map.generate_map_array())
        """
        self.main_character = player()

        self.map = 1

        # Set Font
        self.font = pygame.font.Font('freesansbold.ttf', 30)

        self.text = self.font.render('CODE: ROB', True, (255, 0, 0))

    # Helpers
    def generate_new_map(self):
        if self.main_character.portal_active:
            self.get_game_window().reset_map()
            self.main_character.portal_active = False
            pygame.display.update()

    def draw_window(self, main_character: player) -> None:
        pygame.Surface.fill(self.window, (255, 255, 0))
        pygame.draw.rect(self.window, (255, 0, 0), (100, 100, default_window().get_window_width() - 200, default_window().get_window_height() - 200))
        self.window.blit(self.text, (default_window().get_window_width() / 2.7, default_window().get_window_height() / 20))
        self.get_game_window().draw(self.window)
        main_character.update_player(self.get_game_window().get_tile_list())
      #  self.generate_new_map()
        pygame.display.update()

    def get_game_window(self):
        game_map = map_generator(map_count=self.map)
        if game_map.get_map_count() == 1:
            game_map = world(preset_maps.start_map())
            return game_map


        else:
            print(game_map.get_map_count())
            print("donkey")
            game_map = world(game_map.generate_map_array())
            return game_map

    def run_game(self):
        pygame.init()

        clock = pygame.time.Clock()  # Control time of main function
        run = True
        while run:
            clock.tick(60)
            for event in pygame.event.get():  # For loop looks for events
                if event.type == pygame.QUIT:  # User quit window
                    run = False

            self.draw_window(self.main_character)  # Call function

        pygame.quit()  # quits the game loop and exits window

    # Getters
    def get_fps(self):
        return self.__fps

    # Setters
    def set_fps(self, fps):
        self.__fps = fps

    # To String