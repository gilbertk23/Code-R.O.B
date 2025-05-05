from Source.Game_Windows.default_window import default_window
from Source.Maps.map_generator import map_generator
from Source.Maps.game_world import world
from Source.Game_Windows.windows import windows
import pygame

pygame.init()

class game_loop:
    __fps = -1

    def __init__(self, fps=60):
        self.set_fps(fps)
        self.current_window = windows()
        self.game_window = default_window().init_window()
        self.world_array = map_generator().generate_map_array()
        self.game_world = world(self.world_array)

    def update_screen(self):
        self.current_window.draw_window()
        self.create_game_world()
        pygame.display.update()

    def create_game_world(self):
        if self.current_window.get_menu_state() == "play_game":
            self.game_world.draw(self.game_window)


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
