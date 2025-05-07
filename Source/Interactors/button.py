# Import Files/Modules
from Interactors.config import *
from Interactors.sprite import sprite
import pygame

class button(sprite):
    # Data Attributes
    __is_hover = None
    __is_clicked = None

    # Init
    def __init__(self, width=200, height=100, x_pos=CENTER_X, y_pos=CENTER_Y, image=DEFAULT_IMAGE, is_hover=False, is_clicked=False):
        super().__init__(width, height, x_pos, y_pos, image)
        self.set_is_hover(is_hover)
        self.set_is_clicked(is_clicked)

        self.image = pygame.transform.scale(image, (int(width), int(height)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)

        self.mouse_pos = pygame.mouse.get_pos()

    # Helpers
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        self.set_is_clicked(False)
        return self.get_action()

    def hovered(self):
        pass

    def get_action(self):
        if self.rect.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.get_is_clicked() == False:
                self.set_is_clicked(True)

        return self.get_is_clicked()

    # Getters
    def get_is_hover(self):
        return self.__is_hover

    def get_is_clicked(self):
        return self.__is_clicked

    # Setters
    def set_is_hover(self, is_hover):
        self.__is_hover = is_hover

    def set_is_clicked(self, is_clicked):
        self.__is_clicked = is_clicked

    # To String