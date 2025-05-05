from Source.Game_Windows.default_window import default_window
from Source.Maps.map_generator import map_generator
from Source.Maps.game_world import world
from Source.Interactors.character import character
from Source.Game_Windows.windows import windows
from Source import Assets
import pygame

pygame.init()

class game_loop:
    __fps = -1

    def __init__(self, fps=60):
        self.set_fps(fps)
        self.current_window = windows()
        self.game_window = default_window().init_window()
        self.world_array = map_generator()
        self.game_world = world(self.world_array.generate_map_array())

        self.main_character = character(10, 10, 400, 560, 'Player Sprite.png', 100, 5, 2, 10)

    def update_screen(self):
        self.current_window.draw_window()
        self.create_game_world()
        pygame.display.update()

    def create_game_world(self):
        if self.current_window.get_menu_state() == "play_game":
            self.game_world.draw(self.game_window)
            self.border_collision()
            self.main_character.update_character()

    def border_collision(self):
        # Left border collision
        if self.main_character.get_x_pos() < self.world_array.get_left_portal_pos()[0] + 10:
            self.main_character.set_x_pos(self.world_array.get_left_portal_pos()[0] + 10)
            self.main_character.set_speed(0)

        # Right border collision
        elif self.main_character.get_x_pos() > self.world_array.get_right_portal_pos()[0] - 10:
            self.main_character.set_x_pos(self.world_array.get_right_portal_pos()[0] - 10)
            self.main_character.set_speed(0)

        # Top border collision
        elif self.main_character.get_y_pos() < self.world_array.get_top_portal_pos()[1] + 10:
            self.main_character.set_y_pos(self.world_array.get_top_portal_pos()[1] + 10)
            self.main_character.set_speed(0)

        elif self.main_character.get_y_pos() > self.world_array.get_bottom_portal_pos()[1] - 10:
            self.main_character.set_y_pos(self.world_array.get_bottom_portal_pos()[1] - 10)
            self.main_character.set_speed(0)
        else:
            self.main_character.set_speed(5)

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
