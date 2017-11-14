class pentago_node:


	def __init__(self, game_state):
		self.game = game_state
	
	
	def get_children(self):
		to_return = []
		for i in range(36):
			placed_move_board = self.game.make_move(i)
			for j in range(4):
				to_return.append(pentago_node(placed_move_board.rotate_section(j)))
		self.children = to_return
		return self.children
