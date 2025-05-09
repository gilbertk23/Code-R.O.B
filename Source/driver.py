# Import Files/Modules
from Source.Game_Windows.game_loop import game_loop

# Def main contains main game loop components only
def main() -> None:
    try:
        game_loop().run_game()
    except TimeoutError:
        print("Game has timed out and failed to load.")
    except ImportError:
        print("Source or pygame has failed to import, please make sure to install all of the packages.")
    except KeyboardInterrupt:
        print("You have exited the program yourself, game has successfully closed.")
    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":  # Ensures code only runs file in file
    main()
