# Import Files/Modules
from Source.Game_Windows.default_window import default_window
from Source.Interactors.button import button
from Source import Assets
import pygame

class windows:
    # Data Attributes
    __menu_state = None
    __font = None

    # Init
    def __init__(self, menu_state="main_menu", font='freesansbold.ttf'):
        self.set_menu_state(menu_state)
        self.set_font(pygame.font.Font(font, 30))  # Sets the font
        self.game_window = default_window().init_window()  # Instantiate the window

    # Helpers
    def draw_window(self):
        self.draw_main_menu()

        self.draw_game_world()

        self.draw_settings()

        self.draw_credits()

    # Make world
    def draw_game_world(self):
        if self.get_menu_state() == "play_game":
            pygame.Surface.fill(self.game_window, (0, 0, 0))
            pygame.draw.rect(self.game_window, (255, 0, 0), (95, 95, self.game_window.get_width() - 190, self.game_window.get_height() - 190), 5)
            self.create_title()
            self.create_back_button()

    # Credits
    def draw_credits(self):
        if self.get_menu_state() == "credits":
            pygame.Surface.fill(self.game_window, (0, 0, 0))
            self.create_title()
            self.create_back_button()

    # Settings
    def draw_settings(self):
        if self.get_menu_state() == "settings":
            pygame.Surface.fill(self.game_window, (0, 0, 0))
            self.create_title()
            self.create_back_button()


    def create_back_button(self):
        settings_button_img = pygame.image.load("Assets/button_quit.png").convert_alpha()
        settings_button = button(x_pos=self.game_window.get_width()/2.5, y_pos=self.game_window.get_height()- 90, image=settings_button_img)
        if(settings_button.draw(self.game_window)):
            self.set_menu_state("main_menu")

    # Main Menu
    def draw_main_menu(self):
        if self.get_menu_state() == "main_menu":
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
        play_button_img = pygame.image.load("Assets/button_resume.png").convert_alpha()
        play_button = button(x_pos=self.game_window.get_width()/2.5, y_pos=self.game_window.get_height()/3, image=play_button_img)
        if(play_button.draw(self.game_window)):
            self.set_menu_state("play_game")

    def create_settings_button(self):
        settings_button_img = pygame.image.load("Assets/button_back.png").convert_alpha()
        settings_button = button(x_pos=self.game_window.get_width() / 2.5, y_pos=self.game_window.get_height() / 2, image=settings_button_img)
        if (settings_button.draw(self.game_window)):
            self.set_menu_state("settings")

    def create_credits_button(self):
        credits_button_img = pygame.image.load("Assets/button_options.png").convert_alpha()
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