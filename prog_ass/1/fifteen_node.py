class fifteen_node:


	def get_depth():
		return self.depth

	def get_children():
		up = fifteen_node(fifteen_puzzle(self.puzzle.data[:]).move("up"), self)
		down = fifteen_node(fifteen_puzzle(self.puzzle.data[:]).move("down"), self)
		left = fifteen_node(fifteen_puzzle(self.puzzle.data[:]).move("left"), self)
		right = fifteen_node(fifteen_puzzle(self.puzzle.data[:]).move("right"), self)

		return [up, down, left, right]


	def __init__(self, puzzle, parent):
		if parent == None:
			self.depth = 0
		else: 
			self.depth = parent.get_depth() + 1
		self.parent = parent
        	self.puzzle = puzzle
	
	def __hash__(self):
		return hash(self.puzzle.format())

    	def __eq__(self, other):
        	if isinstance(other, self.__class__):
           		return self.puzzle == other.puzzle
        	else:
            		return False
