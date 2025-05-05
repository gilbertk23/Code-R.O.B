from Source.Game_Windows.default_window import default_window
from Source.Maps.map_generator import map_generator
from Source.Maps.game_world import world
from Source.Interactors.main_character import main_character
from Source.Interactors.enemy import enemy
from Source.Game_Windows.windows import windows
import random
import pygame

pygame.init()

class game_loop():
    __fps = -1

    def __init__(self, fps=60):
        self.set_fps(fps)

        # Set Py Window
        self.current_window = windows()
        self.game_window = default_window().init_window()

        # Create world map
        self.world_array = map_generator()
        self.game_world = world(self.world_array.generate_map_array())

        # Instantiate Main Character
        self.main_character = main_character(10, 10, 400, 560, 'Player Sprite.png', 100, 5, 2, 10, True)
        self.font = pygame.font.Font('freesansbold.ttf', 20)

        # Set Interactable
        self.map_count = 0
        self.enemies = []
        self.coins = []

        self.all_sprites = pygame.sprite.Group()

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
        self.left_portal_collision()

        self.right_portal_collision()

        self.top_portal_collision()

        self.bottom_portal_collision()

    def left_portal_collision(self):
        if (self.main_character.get_x_pos() == self.world_array.get_left_portal_pos()[0] + 10 and
            self.main_character.get_y_pos() >= self.world_array.get_left_portal_pos()[1] - 10 and
            self.main_character.get_y_pos() <= self.world_array.get_left_portal_pos()[1] + 10):

            self.reset_map()

    def right_portal_collision(self):
        if (self.main_character.get_x_pos() == self.world_array.get_right_portal_pos()[0] - 10 and
            self.main_character.get_y_pos() >= self.world_array.get_right_portal_pos()[1] - 10 and
            self.main_character.get_y_pos() <= self.world_array.get_right_portal_pos()[1] + 10):

            self.reset_map()

    def top_portal_collision(self):
        if (self.main_character.get_y_pos() == self.world_array.get_top_portal_pos()[1] + 10 and
            self.main_character.get_x_pos() >= self.world_array.get_top_portal_pos()[0] - 10 and
            self.main_character.get_x_pos() <= self.world_array.get_top_portal_pos()[0] + 10):

            self.reset_map()

    def bottom_portal_collision(self):
        if (self.main_character.get_y_pos() == self.world_array.get_bottom_portal_pos()[1] - 10 and
            self.main_character.get_x_pos() >= self.world_array.get_bottom_portal_pos()[0] - 10 and
            self.main_character.get_x_pos() <= self.world_array.get_bottom_portal_pos()[0] + 10):

            self.reset_map()

    def generate_new_map(self):
        # Reset Map
        self.world_array = map_generator()
        self.game_world = world(self.world_array.generate_map_array())

    def update_player(self):
        # Update Player
        self.main_character.set_x_pos(self.game_window.get_width() / 2)
        self.main_character.set_y_pos(self.game_window.get_height() / 2)

    def update_enemies(self):
        self.enemies = []
        for enemies in range(self.world_array.get_num_enemies()):
            rand_x = random.randint(self.world_array.get_left_portal_pos()[0] + 10, self.world_array.get_right_portal_pos()[0] - 10)
            rand_y = random.randint(self.world_array.get_top_portal_pos()[1] + 10, self.world_array.get_bottom_portal_pos()[1] - 10)
            new_enemy = enemy(10, 10, rand_x, rand_y, 'enemy.png', 10, 2, 200, 10, 10)
            self.enemies.append(new_enemy)

    def update_map_information(self):
        # Update Map Count
        self.map_count += 1

        if self.map_count == 10:
            self.current_window.set_menu_state("win_game")

    def reset_map(self):
        self.generate_new_map()

        self.update_player()

        self.update_enemies()

        self.update_map_information()

    def border_collision(self):

        self.left_border_collision()

        self.right_border_collision()

        self.top_border_collision()

        self.bottom_border_collision()


    def left_border_collision(self):
        if (self.main_character.get_x_pos() < self.world_array.get_left_portal_pos()[0] + 10):
            self.main_character.set_x_pos(self.world_array.get_left_portal_pos()[0] + 10)
            self.main_character.set_speed(0)

        else:
            self.main_character.set_speed(5)

    def right_border_collision(self):
        if self.main_character.get_x_pos() > self.world_array.get_right_portal_pos()[0] - 10:
            self.main_character.set_x_pos(self.world_array.get_right_portal_pos()[0] - 10)
            self.main_character.set_speed(0)

        else:
            self.main_character.set_speed(5)

    def top_border_collision(self):
        if self.main_character.get_y_pos() < self.world_array.get_top_portal_pos()[1] + 10:
            self.main_character.set_y_pos(self.world_array.get_top_portal_pos()[1] + 10)
            self.main_character.set_speed(0)

        else:
            self.main_character.set_speed(5)

    def bottom_border_collision(self):
        if self.main_character.get_y_pos() > self.world_array.get_bottom_portal_pos()[1] - 10:
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
