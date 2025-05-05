from Source.Game_Windows.default_window import default_window
from Source.Game_Windows.windows import windows
import pygame

pygame.init()

class game_loop:
    # Data Attributes
    __fps = -1

    def __init__(self, fps=60):
        # Set target FPS
        self.set_fps(fps)
        # Initialize with the main menu (or default_window if you prefer)
        self.current_window = windows()

    def update_screen(self):
        self.draw_window()

    def draw_window(self) -> None:
        self.current_window.draw_window()
        pygame.display.update()

    def run_game(self):
        clock = pygame.time.Clock()
        run = True

        while run:
            clock.tick(self.get_fps())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.draw_window()

        pygame.quit()

    # Getter
    def get_fps(self) -> int:
        return self.__fps

    # Setter
    def set_fps(self, fps: int) -> None:
        self.__fps = fps