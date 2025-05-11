"""
Config file should only contain constant variables and should be accessible to all directories
"""

# Game Name
GAME_NAME = "CODE: ROB"

# Window Settings
WIDTH = 900
HEIGHT = 700

# Game Settings
FPS = 60

'''
BOARD SIZE CALCULATED BY MULTIPLYING ROW_SIZE * TILE_SIZE AND COL_SIZE * TILE_SIZE
'''

# Board Settings
TILE_SIZE = 16
ROW_SIZE = 32
COL_SIZE = 44

# Menu Titles
MAIN_MENU = "Main_Menu"
SETTINGS_MENU = "Settings_Menu"
CREDITS_MENU = "Credits_Menu"
GAME_WINDOW = "Game_Window"
WIN_WINDOW = "Win_Window"
LOSE_WINDOW = "Lose_Window"
DEFAULT_WINDOW = MAIN_MENU

# Board Position Settings
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

# Character Settings
CHAR_WIDTH = TILE_SIZE
CHAR_HEIGHT = TILE_SIZE

# Color Types
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Font Types
FONT1 = 'freesansbold.ttf'

# Asset Settings
DEFAULT_IMAGE = 'Source/Assets/default.png'

# Terrain and Block Information

# Layer Settings
PLAYER_LAYER = 3
ENEMY_LAYER = 3
GROUND_LAYER = 1
BLOCK_LAYER = 2