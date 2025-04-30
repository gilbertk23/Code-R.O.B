# Level creator v0.2

This has very limited functionality as of now, eventually this will be a fully-fledged level editor and be refactored into OOP principles.

# planned features for this release:

- refactor into OOP
	- Tile class
		- bounding coordinates
		- collision event editing
- fully-fledged level editing
	- entity placement (e.g. collectable items, enemies)
	- maps are readable and writable via JSON files

# current functionality: 

- dynamic level display based on reading an array of tile IDs (see grid_instance variable)
- painting tiles with clicking
	- reading mouse pointer position on occurence of click
- key inputs -> number keys
	- change currently selected tile to paint with
- map can be saved to file (JSON)
	- press "s"

# ideas for gameplay key-map

## movement

W S A D 🡺 movement

## interaction

<, > 🡺 yes, no; interaction options

/ 🡺 attack? (because it's "slash" for slashing?)

I think it should be keyboard-based, I don't see much reason for the player to click on things.

# Spritesheets

Spritesheets must have an associated JSON file containing metadata for the contained sprites. The metadata file must have the same name as the spritesheet it describes. [See documentation](spritesheet_metadata_docs.md).

# tile grid values

- 0 : void
- 1 : floor
- 2 : door
- 3 : wall
