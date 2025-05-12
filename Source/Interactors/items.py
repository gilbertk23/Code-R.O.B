# Import Files/Modules
from Source.Interactors.sprite import sprite
import pygame
import os


class items(sprite, pygame.sprite.Sprite):
    # Data Attributes
    __isactive = True

    # Init
    def __init__(self, sprite_sheet, width, height, x_pos, y_pos, image, target=None, isactive=True):
        super().__init__(width, height, x_pos, y_pos, image)

        self.sprite_sheet = sprite_sheet
        self.groups = self.sprite_sheet.all_sprites  # Get all sprites group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.items = pygame.image.load(os.path.join('Assets', image))
        self.image = pygame.transform.scale(self.items, (width, height))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)

        self.set_target(target)
        self.set_isactive(isactive)

    # Helpers
    def update(self, world, target_x_pos, target_y_pos):
        self.item_collide(target_x_pos, target_y_pos)
        self.rect.topleft = (self.get_x_pos(), self.get_y_pos())  # Update character to window

    def item_collide(self, target_x_pos, target_y_pos):
        if self.get_x_pos() in range(target_x_pos-45, target_x_pos+45) and self.get_y_pos() in range(target_y_pos-45, target_y_pos+45):
            self.kill()

    # Getters
    def get_target(self):
        return self.__target

    def get_isactive(self):
        return self.__isactive

    # Setters
    def set_target(self, target):
        self.__target = target

    def set_isactive(self, isactive):
        self.__isactive = isactive
