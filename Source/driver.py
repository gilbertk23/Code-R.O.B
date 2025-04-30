# Import Files/Modules
from Source.Game_Windows.game_loop import game_loop

# Def main contains main game loop components only
def main() -> None:
    game_loop().run_game()

if __name__ == "__main__":  # Ensures code only runs file in file
    main()
