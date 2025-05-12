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

        self.draw_lose_window()

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

    def draw_lose_window(self):
        if self.get_menu_state() == "lose_game":
            pygame.Surface.fill(self.game_window, (0, 0, 0))
            self.create_title()
            self.create_lose_box()

    # Make world
    def draw_game_world(self):
        if self.get_menu_state() == "play_game":
            pygame.Surface.fill(self.game_window, (0, 0, 0))
            pygame.draw.rect(self.game_window, (255, 255, 255), (95, 95, self.game_window.get_width() - 187, self.game_window.get_height() - 177), 5)
            # self.create_title()
            self.create_main_menu_button()

    # Credits
    def draw_credits(self):
        if self.get_menu_state() == "credits":
            pygame.Surface.fill(self.game_window, (0, 0, 0))
            self.draw_credits_window()
            self.create_title()
            self.create_main_menu_button()

    def draw_credits_window(self):
        credits_img = pygame.image.load("Assets/main_menu/credit_screen.png").convert_alpha()
        credits_button = button(width=900, height=700, x_pos=0, y_pos=0, image=credits_img)
        credits_button.draw(self.game_window)

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

    def create_lose_box(self):
        lose_box_img = pygame.image.load("Assets/lose_box.png").convert_alpha()
        lose_box = button(x_pos=self.game_window.get_width()/2.5, y_pos=self.game_window.get_height() / 2, image=lose_box_img)
        lose_box.draw(self.game_window)

    def create_main_menu_button(self):
        main_menu_button_img = pygame.image.load("Assets/main_menu.png").convert_alpha()
        main_menu_button = button(x_pos=self.game_window.get_width()/2.5, y_pos=self.game_window.get_height()- 90, image=main_menu_button_img)
        if(main_menu_button.draw(self.game_window)):
            if self.get_menu_state() not in ["Main_Menu", "settings", "credits"]:
                pygame.mixer.music.load("Assets/sound/RPG Medieval Fantasy - It Must Not End Here (Loopable).wav")
                pygame.mixer.music.play(loops=-1) # loop indefinitely
            self.set_menu_state("Main_Menu")

    # Main Menu
    def draw_main_menu(self):
        if self.get_menu_state() == "Main_Menu":
            if not (pygame.mixer.music.get_busy()):
                pygame.mixer.music.load("Assets/sound/RPG Medieval Fantasy - It Must Not End Here (Loopable).wav")
                pygame.mixer.music.play(loops=-1) # loop indefinitely
            pygame.Surface.fill(self.game_window, (0,0,0))
            bg_image = pygame.image.load("Assets/main_menu/main_menu_background_desat_vingnette.png")
            self.game_window.blit(bg_image, (0,0))
            self.create_title()
            self.create_play_button()
            self.create_settings_button()
            self.create_credits_button()

    def create_title(self):
        title_img = pygame.image.load("Assets/main_menu/title.png").convert_alpha()
        title = button(width=384, height=128, x_pos=(self.game_window.get_width()/2)-(384/2), y_pos=self.game_window.get_height()/10, image=title_img)
        title.draw(self.game_window)

    def create_play_button(self):
        play_button_img = pygame.image.load("Assets/main_menu/start_btn2.png").convert_alpha()
        play_button = button(width=230*1.5, height=62*1.5, x_pos=(self.game_window.get_width()/2)-(230*1.5/2), y_pos=self.game_window.get_height()-425, image=play_button_img)
        if(play_button.draw(self.game_window)):
            pygame.mixer.music.load("Assets/sound/RPG Medieval Fantasy - Temple Call (Loopable).wav")
            pygame.mixer.music.play(loops=-1) # loop indefinitely
            self.set_menu_state("play_game")

    def create_settings_button(self):
        settings_button_img = pygame.image.load("Assets/main_menu/settings_btn.png").convert_alpha()
        settings_button = button(width=230*1.5, height=62*1.5, x_pos=(self.game_window.get_width()/2)-(230*1.5/2), y_pos=self.game_window.get_height()-300, image=settings_button_img)
        if (settings_button.draw(self.game_window)):
            self.set_menu_state("settings")

    def create_credits_button(self):
        credits_button_img = pygame.image.load("Assets/main_menu/cred_btn_2.png").convert_alpha()
        credits_button = button(width=230*1.5, height=62*1.5, x_pos=(self.game_window.get_width()/2)-(230*1.5/2), y_pos=self.game_window.get_height()-175, image=credits_button_img)
        if(credits_button.draw(self.game_window)):
            self.set_menu_state("credits")

    # Getters
    def get_menu_state(self):
        return self.__menu_state

    def get_font(self):
        return self.__font

    # Setters
    def set_menu_state(self, menu_state):
        try:
            self.__menu_state = menu_state
            print(menu_state, "has loaded successfully!")
        except ImportError:
            print("Source or pygame has not been imported correctly, please make sure to import the packages.")
        except Exception as e:
            print("Error: ", e)

    def set_font(self, font):
        self.__font = font

    # To String