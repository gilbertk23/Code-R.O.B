from __future__ import annotations

import importlib.resources
import random
import os
from typing import Final

import pygame

TILE_0_CONTEXT: Final = importlib.resources.path("roguelike_game.assets", "Clear Block.png")
TILE_1_CONTEXT: Final = importlib.resources.path("roguelike_game.assets", "Dark Block.jpg")
TILE_2_CONTEXT: Final = importlib.resources.path("roguelike_game.assets", "Grey Block.jpg")
TILE_3_CONTEXT: Final = importlib.resources.path("roguelike_game.assets", "grass.png")

with TILE_0_CONTEXT as _temp:
    TILE_0: Final = _temp
with TILE_1_CONTEXT as _temp:
    TILE_1: Final = _temp
with TILE_2_CONTEXT as _temp:
    TILE_2: Final = _temp
with TILE_3_CONTEXT as _temp:
    TILE_3: Final = _temp



class map_generator:
    # Data Attributes
    __slots__ = (
        "__min_width",
        "__max_width",
        "__min_height",
        "__max_height",
        "__min_enemies",
        "__max_enemies",
        "__min_chests",
        "__max_chests",
        "__current_score",
        "__map_count",
        "set_row_size",
        "set_col_size",
        "set_chest_num",
        "icons",
    )

    # Init
    def __init__(
        self,
        min_width: int = 10,
        max_width: int = 20,
        min_height: int = 10,
        max_height: int = 20,
        min_enemies: int = 0,
        max_enemies: int = 30,
        min_chests: int = 0,
        max_chests: int = 10,
        current_score: int = 0,
        map_count: int = 0,
    ) -> None:
        self.set_min_width(min_width)
        self.set_max_width(max_width)
        self.set_min_height(min_height)
        self.set_max_height(max_height)
        self.set_min_enemies(min_enemies)
        self.set_max_enemies(max_enemies)
        self.set_min_chests(min_chests)
        self.set_max_chests(max_chests)
        self.set_current_score(current_score)
        self.set_map_count(map_count)

        self.set_row_size = random.randint(self.get_min_height(), self.get_max_height())
        self.set_col_size = random.randint(self.get_min_width(), self.get_max_width())
        self.set_chest_num = random.randint(self.get_min_chests(), self.get_max_chests())

        self.icons = [
            pygame.image.load(TILE_0),
            pygame.image.load(TILE_1),
            pygame.image.load(TILE_2),
            pygame.image.load(TILE_3),
        ]

    # Helpers
    @staticmethod
    def get_block_render_data(
        block_surface: pygame.Surface,
        grid_size: int,
        col_count: int,
        row_count: int,
    ) -> tuple[pygame.Surface, pygame.Rect]:
        scaled_surface = pygame.transform.scale(block_surface, (grid_size, grid_size))  # Tranforming tile to size of grid
        block_rect = scaled_surface.get_rect()  # Convert image to rectangle
        block_rect.x = col_count * grid_size  # Find x value of image
        block_rect.y = row_count * grid_size  # Find y value of image
        return (scaled_surface, block_rect)  # Save tile as tuple
    
    def clear_block(
        self,
        tile_list: list[tuple[pygame.Surface, pygame.Rect]],
        grid_size: int,
        col_count: int,
        row_count: int,
    ) -> None:
        surface = self.icons[0]
        # Adding tile to list
        tile_list.append(self.get_block_render_data(surface, grid_size, col_count, row_count))

    def border_block(
        self,
        tile_list: list[tuple[pygame.Surface, pygame.Rect]],
        grid_size: int,
        col_count: int,
        row_count: int,
    ) -> None:
        surface = self.icons[1]
        # Adding tile to list
        tile_list.append(self.get_block_render_data(surface, grid_size, col_count, row_count))

    def portal_block(
        self,
        tile_list: list[tuple[pygame.Surface, pygame.Rect]],
        grid_size: int,
        col_count: int,
        row_count: int,
    ) -> None:
        surface = self.icons[2]
        # Adding tile to list
        tile_list.append(self.get_block_render_data(surface, grid_size, col_count, row_count))

    def floor_block(
        self,
        tile_list: list[tuple[pygame.Surface, pygame.Rect]],
        grid_size: int,
        col_count: int,
        row_count: int,
    ) -> None:
        surface = self.icons[3]
        # Adding tile to list
        tile_list.append(self.get_block_render_data(surface, grid_size, col_count, row_count))

    def chest_block(
        self,
        tile_list: list[tuple[pygame.Surface, pygame.Rect]],
        grid_size: int,
        col_count: int,
        row_count: int,
    ) -> None:
        self.clear_block(tile_list, grid_size, col_count, row_count)

    def get_row_size(self) -> int:
        return self.set_row_size  # Returns the size of the map row size

    def get_col_size(self) -> int:
        return self.set_col_size  # Returns the size of the map column size

    def get_row_portal(self) -> int:
        row_portal = int(self.get_row_size()//2)  # Set position of the portal on the row
        return row_portal  # Return position

    def get_col_portal(self) -> int:
        col_portal = int(self.get_col_size()//2)  # Set position of the portal on the column
        return col_portal  # Return position

    def get_chest_pos(self) -> list[list[int]]:
        total_chests = self.set_chest_num  # Get the total number of chests per map
        chest_list = []  # Create empty chest list

        for items in range(total_chests):  # Iterate through the range of total chests
            column = random.randint(1, self.get_col_size() - 1)  # Set random column value
            row = random.randint(1, self.get_row_size() - 1)  # Set random row value
            chest_list.append([column, row])  # Chest instance set to row and column

        return chest_list  # Return chest list

    def generate_chests(self, map_array: list[list[int]]) -> list[list[int]]:
        for columns in self.get_chest_pos():  # Iterate through columns on the chest positions
            map_array[columns[1]][columns[0]] = 4  # If available set position to chest block

        return map_array  # Return map array

    def generate_column_border(self) -> list[int]:
        left_distance = self.get_col_size() - self.get_col_portal()  # Left distance value of portal position

        top_border = [1] * left_distance  # Create top_border list
        top_border.append(2)  # Append portal block

        right_distance = self.get_col_size() - len(top_border)  # Right distance value of portal position

        for list in range(right_distance):  # Iterate through range of right_distance
            top_border.append(1)  # Append border walls

        return top_border  # Return top border

    def detect_left_row_portal(self, row: int, middle_map: list[int]) -> list[int]:
        if row == self.get_row_portal():  # If the row value is equal to portal position
            middle_map.append(2)  # border wall set to portal block

        else:
            middle_map.append(1)  # If not equal set border wall to border block

        return middle_map  # Return middle map

    def detect_right_row_portal(self, row: int, middle_map: list[int]) -> list[int]:
        if row == self.get_row_portal():  # If the row value is equal to portal position
            middle_map.append(2)  # border wall set to portal block

        else:
            middle_map.append(1) # If not equal set border wall to border block

        return middle_map  # Return middle map

    def generate_middle_map(self, row: int) -> list[int]:
        middle_map = []  # Instantiate middle map list
        self.detect_left_row_portal(row, middle_map)  # Call detect_left_row_portal

        if row != self.get_row_size() - 2:
            for rows in range(self.get_col_size() - 2):
                middle_map.append(3)  # Append floor to middle map list

            self.detect_right_row_portal(row, middle_map)  # Call detect_right_row_portal

        else:
            middle_map = self.generate_column_border()  # Make bottom map border

        return middle_map  # Return middle map

    def generate_map_array(self) -> list[list[int]]:
        map_array = []  # Instantiate map_array
        for columns in range(self.get_col_size()):  # Iterate through the range of column size
            map_array.append(self.generate_column_border())  # Append column border
            for rows in range(self.get_row_size() - 1):  # Iterate through range of border size
                map_array.append(self.generate_middle_map(rows))  # Append middle map

            self.generate_chests(map_array)  # Plot Chests onto map array

        return map_array  # Return middle map

    # Function to print viewable array
    def print_array(self) -> None:
        for items in self.generate_map_array():
            print(items)

    # Getters
    def get_min_width(self) -> int:
        return self.__min_width

    def get_max_width(self) -> int:
        return self.__max_width

    def get_min_height(self) -> int:
        return self.__min_height

    def get_max_height(self) -> int:
        return self.__max_height

    def get_min_enemies(self) -> int:
        return self.__min_enemies

    def get_max_enemies(self) -> int:
        return self.__max_enemies

    def get_min_chests(self) -> int:
        return self.__min_chests

    def get_max_chests(self) -> int:
        return self.__max_chests

    def get_current_score(self) -> int:
        return self.__current_score

    def get_map_count(self) -> int:
        return self.__map_count

    # Setters
    def set_min_width(self, min_width: int) -> None:
        self.__min_width = min_width

    def set_max_width(self, max_width: int) -> None:
        self.__max_width = max_width

    def set_min_height(self, min_height: int) -> None:
        self.__min_height = min_height

    def set_max_height(self, max_height: int) -> None:
        self.__max_height = max_height

    def set_min_enemies(self, min_enemies: int) -> None:
        self.__min_enemies = min_enemies

    def set_max_enemies(self, max_enemies: int) -> None:
        self.__max_enemies = max_enemies

    def set_min_chests(self, min_chests: int) -> None:
        self.__min_chests = min_chests

    def set_max_chests(self, max_chests: int) -> None:
        self.__max_chests = max_chests

    def set_current_score(self, current_score: int) -> None:
        self.__current_score = current_score

    def set_map_count(self, map_count: int) -> None:
        self.__map_count = map_count

    # ToString
    def __str__(self) -> str:
        map_generator_string = ""
        map_generator_string += (f"Map_Generator Data Attributes-->\n\t"
            f"Min_Width: {self.get_min_width()}\n\t"
            f"Max_Width: {self.get_max_width()}\n\t"
            f"Min_Height: {self.get_min_height()}\n\t"
            f"Max_Height: {self.get_max_height()}\n\t"
            f"Min_Enemies: {self.get_min_enemies()}\n\t"
            f"Max_Enemies: {self.get_max_enemies()}\n\t"
            f"Min_Chests: {self.get_min_chests()}\n\t"
            f"Max_Chests: {self.get_max_chests()}\n\t"
            f"Current_Score: {self.get_current_score()}\n\t"
            f"Map_Count: {self.get_map_count()}\n\t")
        return map_generator_string
