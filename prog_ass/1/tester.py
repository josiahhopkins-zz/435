from fifteen_puzzle import *

def main():
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

def print_puzzle(the_puzzle):
	print "--------------------------------------------------------------"
	print the_puzzle.format()

if __name__ == '__main__':
	main()
