# Import Files/Modules
from Source.Interactors.button import button
from Source.Interactors.config import *
import pygame

class windows:
    # Data Attributes
    __menu_state = None
    __font = None

    # Init
    def __init__(self, window, menu_state=DEFAULT_WINDOW, font=FONT1):
        self.set_menu_state(menu_state)  # Sets the state of the window
        self.set_font(pygame.font.Font(font, 30))  # Sets the font
        self.game_window = window # Instantiate the window

    # Helpers
    def draw_window(self):
        self.draw_win_window()

        self.draw_main_menu()

        self.draw_game_world()

        self.draw_settings()

        self.draw_credits()

    # Win Window
    def draw_win_window(self):
        if self.get_menu_state() == "win_game":
            pygame.Surface.fill(self.game_window, (0, 0, 0))
            self.create_title()
            self.create_win_box()
            self.create_main_menu_button()

    # Make world
    def draw_game_world(self):
        if self.get_menu_state() == "play_game":
            pygame.Surface.fill(self.game_window, (0, 0, 0))
            pygame.draw.rect(self.game_window, (255, 0, 0), (95, 95, self.game_window.get_width() - 190, self.game_window.get_height() - 190), 5)
            self.create_title()
            self.create_main_menu_button()

    # Credits
    def draw_credits(self):
        if self.get_menu_state() == "credits":
            pygame.Surface.fill(self.game_window, (0, 0, 0))
            self.create_title()
            self.create_main_menu_button()

    # Settings
    def draw_settings(self):
        if self.get_menu_state() == "settings":
            pygame.Surface.fill(self.game_window, (0, 0, 0))
            self.create_title()
            self.create_main_menu_button()

    def create_win_box(self):
        win_box_img = pygame.image.load("Assets/win_box.png").convert_alpha()
        win_box = button(x_pos=self.game_window.get_width()/2.5, y_pos=self.game_window.get_height() / 2, image=win_box_img)
        win_box.draw(self.game_window)

    def create_main_menu_button(self):
        main_menu_button_img = pygame.image.load("Assets/main_menu.png").convert_alpha()
        main_menu_button = button(x_pos=self.game_window.get_width()/2.5, y_pos=self.game_window.get_height()- 90, image=main_menu_button_img)
        if(main_menu_button.draw(self.game_window)):
            self.set_menu_state("Main_Menu")

    # Main Menu
    def draw_main_menu(self):
        if self.get_menu_state() == "Main_Menu":
            pygame.Surface.fill(self.game_window, (0, 0, 0))
            self.create_title()
            self.create_play_button()
            self.create_settings_button()
            self.create_credits_button()

    def create_title(self):
        title_img = pygame.image.load("Assets/ROB.png").convert_alpha()
        title = button(x_pos=self.game_window.get_width()/2.5, y_pos=self.game_window.get_height()/25, image=title_img)
        title.draw(self.game_window)

    def create_play_button(self):
        play_button_img = pygame.image.load("Assets/play_game.png").convert_alpha()
        play_button = button(x_pos=self.game_window.get_width()/2.5, y_pos=self.game_window.get_height()/3, image=play_button_img)
        if(play_button.draw(self.game_window)):
            self.set_menu_state("play_game")

    def create_settings_button(self):
        settings_button_img = pygame.image.load("Assets/settings.png").convert_alpha()
        settings_button = button(x_pos=self.game_window.get_width() / 2.5, y_pos=self.game_window.get_height() / 2, image=settings_button_img)
        if (settings_button.draw(self.game_window)):
            self.set_menu_state("settings")

    def create_credits_button(self):
        credits_button_img = pygame.image.load("Assets/credits.png").convert_alpha()
        credits_button = button(x_pos=self.game_window.get_width()/2.5, y_pos=self.game_window.get_height()/1.5, image=credits_button_img)
        if(credits_button.draw(self.game_window)):
            self.set_menu_state("credits")

    # Getters
    def get_menu_state(self):
        return self.__menu_state

    def get_font(self):
        return self.__font

    # Setters
    def set_menu_state(self, menu_state):
        self.__menu_state = menu_state

    def set_font(self, font):
        self.__font = font

    # To String