from pentago import *

def base_test():
	game = pentago()
	game.show_log()

def move_test():
	game = pentago()
	game.make_move(0, 0, 1, 0, True)
	game.show_log()
	print "\n\n"
	game.make_move(2, 2, 2, 0, False)
	game.show_log()

if __name__ == "__main__":
	#base_test()
	move_test()
