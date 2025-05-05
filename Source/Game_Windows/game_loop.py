from fontTools.colorLib.builder import populateCOLRv0

from Source.Game_Windows.default_window import default_window
from Source.Maps.map_generator import map_generator
from Source.Maps.game_world import world
from Source.Interactors.main_character import main_character
from Source.Interactors.enemy import enemy
from Source.Game_Windows.windows import windows
import random
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
        self.main_character = main_character(10, 10, 400, 560, 'Player Sprite.png', 100, 5, 2, 10, True)
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.map_count = 0
        self.enemies = []

    def update_map_count(self):
        map_count = self.font.render(f"Map Count: {self.map_count}", True, (255, 0, 0))
        self.game_window.blit(map_count, (100, 100))

    def update_screen(self):
        self.current_window.draw_window()
        self.create_game_world()
        pygame.display.update()


    def create_game_world(self):
        if self.current_window.get_menu_state() == "play_game":
            self.game_world.draw(self.game_window)
            self.update_map_count()
            for bad_guy in self.enemies:
                bad_guy.update_enemy(self.main_character.get_x_pos(), self.main_character.get_y_pos())
            self.border_collision()
            self.portal_collision()
            self.main_character.update_main_character()

    def portal_collision(self):
        # Detect collision on the left portal
        if (self.main_character.get_x_pos() == self.world_array.get_left_portal_pos()[0] + 10 and
            self.main_character.get_y_pos() >= self.world_array.get_left_portal_pos()[1] - 10 and
            self.main_character.get_y_pos() <= self.world_array.get_left_portal_pos()[1] + 10):

            self.reset_map()

        # Detect collision on the right portal
        elif (self.main_character.get_x_pos() == self.world_array.get_right_portal_pos()[0] - 10 and
            self.main_character.get_y_pos() >= self.world_array.get_right_portal_pos()[1] - 10 and
            self.main_character.get_y_pos() <= self.world_array.get_right_portal_pos()[1] + 10):

            self.reset_map()

    def reset_map(self):
        # Reset Map
        self.world_array = map_generator()
        self.game_world = world(self.world_array.generate_map_array())

        # Update Player
        self.main_character.set_x_pos(self.game_window.get_width()/2)
        self.main_character.set_y_pos(self.game_window.get_height()/2)

        # Update Enemies
        self.enemies = []
        for enemies in range(self.world_array.get_num_enemies()):
            rand_x = random.randint(self.world_array.get_left_portal_pos()[0] + 10, self.world_array.get_right_portal_pos()[0] - 10)
            rand_y = random.randint(self.world_array.get_top_portal_pos()[1] + 10, self.world_array.get_bottom_portal_pos()[1] - 10)
            new_enemy = enemy(10, 10, rand_x, rand_y, 'enemy.png', 10, 2, 200, 10, 10)
            self.enemies.append(new_enemy)

        # Update Map Count
        self.map_count += 1

        if self.map_count == 10:
            print("test")
            self.current_window.set_menu_state("win_game")

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
