class Tile():
	### Attributes ###
	"""
	A class that holds a single tile of the map and its properties.

	@param id: unique number for the specific tile in the map, set dynamically.
	@param type: the identifying char that is parsed for image loading (see levelgrid_docs.md for more info on this).
	@param bounds: the X and Y bounding coordinates of the tile.
	@param collision_action: string identifying what should happen when the player collides with this tile, see documentation for list of collision actions (TODO).
	"""
	__id = -1
	__type = "."
	__bounds = {
		"max_x": -1,
		"max_y": -1,
		"min_x": -1,
		"min_y": -1,
	}
	__collision_action = ""


	### Constructors ###
	def __init__(id, type, bounds, collision_action):
		pass

	### Helpers ###

	### Getters ###
	def get_id(self):
		return __id
	def get_type(self):
		return type
	def get_bounds(self):
		return bounds
	def get_collision_action(self):
		return collision_action

	### Setters ###
	def set_id(self, new_id):
		__id = new_id
	def set_type(self, type):
		__type = type
	def set_bounds(self, bounds):
		__bounds = bounds
	def set_collision_action(self, action):
		__collision_action = action

	### __str___ ###
	def __str__(self):
		txt = ""
		txt += "Tile Info:" + "\n"
		txt += "\tid: " + str(self.get_id()) + "\n"
		txt += "\ttype: " + str(self.get_type()) + "\n"
		txt += "\tbounds: " + str(self.get_bounds()) + "\n"
		txt += "\tcollision action: " + str(self.get_collision_action()) + "\n"
		return txt

#  idea for new class: Tile
	# this can be for individual tiles, which are then put into an iterable array
		# will make .levelgrid files really ugly if we just store Tile instances in a CSV, 
		# but maybe we could store the data in multiple masks?
			# e.g. bounds-mask, collision-action-mask, id-mask, type-mask
			# might bloat out the code, tho... maybe we'll need to do some compression
# __bounds  (max_x, max_y) 
		  # (min_x, min_y)
# __collision_action
# __id
# __type (char, relates to grid_instance[]; e.g. ".","0","1"; this is what loads the images like with tile_catalogue)
