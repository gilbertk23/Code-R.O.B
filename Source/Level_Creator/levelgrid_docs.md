# NOTE
`.levelgrid` files currently have no functionality. I plan on making a parser that will load the levels from these `.levelgrid` files in the future.

Seeing as they have no functionaliy, the rest of this document can be regarded as "hopes and dreams" instead of actual usable information.

---

HOW TO USE .levelgrid FILES

# header
The file starts with a few lines of metadata.

Each line starts with "@" to denote that it is a part of the header.

Properties are in all-caps, key-value pairs separated by ":"

## @NAME
the name of the level

**use**:
`@NAME:"level 1"`

## @SIZE
the size of the level, in grid squares.

**use**:
`@SIZE:16x16`

rows x columns

## data reference
### `.`
empty / null / void
### `0`
wall, collision
### `1`
grass, walkable
### `2`
door, walkable, event(next_level)
### `3`
goal, walkable, event(game_end)