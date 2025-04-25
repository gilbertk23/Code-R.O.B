#Import Files/Modules
import pygame


class Window:
    # Data Attributes
    __slots__ = ("__background", "screen")

    # Init
    def init(
        self,
        game_name="ROB",
        window_width=900,
        window_height=700,
        background=(0, 0, 0),
    ) -> None:
        # Create py window
        self.screen = pygame.display.set_mode((window_width, window_height))
        print(f'{self.screen = }')
        # Window Game Caption
        pygame.display.set_caption(game_name)

        self.set_background(background)

    # Helpers

    def get_background(self) -> tuple[int, int, int]:
        return self.__background

    # Setters
    def set_background(self, background: tuple[int, int, int]) -> None:
        self.__background = background

    # To String

