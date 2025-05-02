# R.O.B

R.O.B is a Python 2d RPG game that allows you to pick up coins to progress in score.

## Installation

Use the main branch link, [main](https://github.com/gilbertk23/cybr404project3/tree/main) to install the zip code for R.O.B.


## Usage
`Go to the file that includes the following code.`
```python
# Import Files/Modules
from Source.Game_Windows.game_loop import game_loop


# Def main contains main game loop components only
def main() -> None:
    game_loop().run_game()


if __name__ == "__main__":  # Ensures code only runs file in file
    main()

```

## Documentation Index
#### `Data Flow Diagrams:`
- **[Nova L1 DFD](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/DFDs/DFD_L1_Nova_1.svg)**
- [Rob L0 DFD](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/DFDs/Rob_DFD_WK1.0.drawio.png)

#### `Timeline:`
- [Timeline](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/Preliminary_Elements/Project_Timeline/Project_Timeline.png)

#### `UMLS:`
- [Uml Week One.One](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/UMLs/Rob_wk_1.1(Readable%20Image).drawio.png)
- [UML Week One.Three](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/UMLs/Rob_UML_WK1.3.drawio.png)
- [UML Week One.Four](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/UMLs/Rob_UML_WK1.4.drawio.png)

#### `Main Documentation:`
- [Executive Summary](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/Preliminary_Elements/Executive_Summary.md)
- [Outcome Summary](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/Preliminary_Elements/Outcome_Summary.md)
- [Problem Statement](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/Preliminary_Elements/Problem_Statement.md)
- [Coding Standards and Practices](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/Preliminary_Elements/Standards_and_Practices_Statement.md)
- [Statement of Work](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/Preliminary_Elements/Statement_of_Work.md)

#### `Requirements:`
- [Hardware Requirements](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/Requirements/Hardware_Requirements.md)
- [Security Requirements](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/Requirements/Security%20Requirements.md)
- [Software Requirements](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/Requirements/Software_Requirements.md)
- [User Requirements](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/Requirements/User_Requirements.md)

#### `Maintence / Security:`
- [Security Design Document](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/Security/Security%20Design%20Document.md)
- [Security Statement](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/Security/Security%20Statement.md)
- [Maintenance Overview](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/Maintenance/Maintenance_Overview.md)
- [Maintenance Timeline](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/Maintenance/Maintenance_Timeline.md)

#### `Misc:`
- [Main Daily Update Index](https://github.com/gilbertk23/cybr404project3/tree/main/Documentation/Daily_Updates)
- [Lore](https://github.com/gilbertk23/cybr404project3/tree/main/Documentation/LORE)
- [Rough Idea](https://github.com/gilbertk23/cybr404project3/blob/main/Documentation/rough_idea.md)

## Coding Index
#### `Assets`
- [Assets](https://github.com/gilbertk23/cybr404project3/tree/main/Source/Assets)
- 
#### `Game Window`
- [Default Window](https://github.com/gilbertk23/cybr404project3/blob/main/Source/Game_Windows/default_window.py)
- [Game Loop](https://github.com/gilbertk23/cybr404project3/blob/main/Source/Game_Windows/game_loop.py)
- [Main Menu](https://github.com/gilbertk23/cybr404project3/blob/main/Source/Game_Windows/main_menu.py)

#### `Interactors`
- [Main Character](https://github.com/gilbertk23/cybr404project3/blob/main/Source/Interactors/main_character.py)

#### `Maps`
- [Map Generator](https://github.com/gilbertk23/cybr404project3/blob/main/Source/Maps/map_generator.py)
- [Game World](https://github.com/gilbertk23/cybr404project3/blob/main/Source/Maps/game_world.py)

#### `Test`
- [Getters / Setters](https://github.com/gilbertk23/cybr404project3/blob/main/Source/Test/getters_and_setters_test.py)

`Note: This only includes the working classes that I personally know of - Jerry (The ones I've done testing for)`

## Test Index
#### `Results / Plans`
- [Security Plan](https://github.com/gilbertk23/cybr404project3/blob/main/Test/Security%20Testing%20Plan.md)
- [Results 04/25/2025](https://github.com/gilbertk23/cybr404project3/blob/main/Test/Test%20Results%2004.25%2C2025.png)
- [Results 04/25/2025 Updated](https://github.com/gilbertk23/cybr404project3/blob/main/Test/Test%20Results%2004.25.2025%20(VER%202).png)




## How Documentation Will Be Done
Everything is to be done in `.md` files unless there is reason to use another format (e.g. diagrams).

#### Team Members: Gavin Sloan | Coder, Jerry Cai | Security, Kaden Gilbert | Team Lead, Nova Solarz | Documentation, and Nick Clark | Design
