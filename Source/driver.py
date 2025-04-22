# Import Files/Modules
from Game_Windows import main_menu
from Game_Windows import default_window
from Interactors import buttons
import pygame

pygame.init()

Menu = main_menu.Main_Menu(900, 700, (100, 100, 255), r'C:\Windows\Fonts\comic.ttf', (0, 0, 0), (75, 75, 255), (100, 100, 255), (100, 100, 255), 0, 500, "KILLER BUNNIES")

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                Menu.get_hover()

            if event.type == pygame.MOUSEBUTTONDOWN:
                Menu.get_click()

        Menu.main_menu()
        pygame.display.update()


if __name__ == '__main__':
    main()
