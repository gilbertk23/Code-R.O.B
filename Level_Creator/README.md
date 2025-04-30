# Level creator v0.2

This has very limited functionality as of now, eventually this will be a fully-fledged level editor and be refactored into OOP principles.

## current functionality: 

- dynamic level display based on reading an array of tile IDs (see grid_instance variable)
- painting tiles with clicking
	- reading mouse pointer position on occurence of click
- key inputs -> number keys
	- change currently selected tile to paint with
- level saving (press "s") (currently no option to name level)
- level loading (hypothetically, at least. It doesn't work *well*)

## planned features:

- refactor into OOP
	- Tile class
		- bounding coordinates
		- collision event editing
- fully-fledged level editing
	- entity placement (e.g. collectable items, enemies)
	- maps are readable and writable via JSON files
		- custom parsing (see [levelgrid docs](levelgrid_docs.md) for more info)

## tile grid values

[tile_spritesheet.json](Assets/tile_spritesheet.json):

- 0 : void
- 1 : floor
- 2 : door
- 3 : wall

# Spritesheets

Spritesheets must have an associated JSON file containing metadata for the contained sprites. The metadata file must have the same name as the spritesheet it describes.

## Spritesheet Metadata

JSON format.

Example metadata below for a spritesheet containing two 16x16 sprites with no border:

```JSON
{
	"0": {
		"pos_x": 16,
		"pos_y": 0,
		"width": 16,
		"height": 16,
		"name": "void.png"
	},

	"1": {
		"pos_x": 0,
		"pos_y": 0,
		"width": 16,
		"height": 16,
		"name": "metal_floor.png"
	},

	"2": {
		"pos_x": 32,
		"pos_y": 0,
		"width": 16,
		"height": 16,
		"name": "door.png"
	},

	"3": {
		"pos_x": 48,
		"pos_y": 0,
		"width": 16,
		"height": 16,
		"name": "wall.png"
	}
}
```
