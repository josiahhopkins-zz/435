from node_pentago import *
from pentago import *
from game_player import *

def base_test():
	game = pentago()
	game.show_log()

def move_test():
	game = pentago()
	game = game.place_tile_with_sector(0, 0, 1)
	game.show_log()
	print "heuristic: %d" % game.heuristic()
	game = game.rotate(0, True)
	game.show_log()
	print "heuristic: %d" % game.heuristic()
	print "\n\n"
	game = game.place_tile_with_sector(2,2,2)
	game.show_log()
	print "heuristic: %d" % game.heuristic()
	game = game.rotate(0, False)
	game.show_log()
	print "heuristic: %d" % game.heuristic()

	game = game.place_tile_with_sector(0, 1, 1)
	game.show_log()
	print "heuristic: %d" % game.heuristic()
	game = game.rotate(0, True)
	game.show_log()
	print "heuristic: %d" % game.heuristic()
	print "\n\n"
if __name__ == "__main__":
	#base_test()
	move_test()
