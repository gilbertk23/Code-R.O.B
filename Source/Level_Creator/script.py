import json
  
def main():
	# GLOBAL VARIABLES 
	COLOR = (255, 100, 98) 
	SURFACE_COLOR = (167, 255, 100) 
	WIDTH = 500
	HEIGHT = 500
	RED = (255, 0, 0)

	f = open("tile_assets/test_metadata.json")
	foo = json.load(f)
	print(foo)
	f.close()
	
if __name__ == '__main__':
	main()