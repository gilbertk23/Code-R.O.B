# Level creator
Right now this is just a proof-of-concept that creates a grid of tiles, eventually this will be a level editor and be refactored into OOP principles.

# current functionality: 
- dynamic level display based on reading an array of tile IDs (see grid_instance variable)
- reading mouse pointer position on occurence of click
- key inputs 1,2,3,4,5,6,7,8,9,0
	- currently doesn't do anything except print to the console that a key-press event has occured

# TODO
- add functionality for editing tiles (mouse-click changes tile to current selected tile; change tile selection with number keys;)
- add functionality for reading and writing map files
- add `.levelgrid` file parsing capability (see [levelgrid docs](levelgrid_docs.md) for more info)

# ideas for gameplay key-map
## movement
W S A D 🡺 movement
## interaction
<, > 🡺 yes, no; interaction options

/ 🡺 attack? (because it's "slash" for slashing?)

I think it should be keyboard-based, I don't see much reason for the player to click on things.