from fifteen_puzzle import *
def test_puzzle_functionality()
	tester = fifteen_puzzle()
	print "Is in order: %s" % str(tester.is_in_order())
	print_puzzle(tester)
	
	for i in ["up", "left", "down", "right"]:
		print str(i)
		for j in range(6):
			print j
			tester.move(i)
			print_puzzle(tester)
			print "Is in order: %s" % str(tester.is_in_order())

def test_bfs():
	puzzle = fifteen_puzzle()
	puzzle.move("up")
	puzzle.move("up")
	tester = BFS(puzzle)
	tester.perform_search()
	tester.print_log()


def main():
	#test_puzzle_functionality()
	test_bfs()

def print_puzzle(the_puzzle):
	print "--------------------------------------------------------------"
	print the_puzzle.format()

if __name__ == '__main__':
	main()
