class pentago_node:


	def __init__(self, game_state, last_move):
		self.game = game_state
		self.last_move = last_move
	
	
	def get_children(self):
		to_return = []
		for i in range(36):
			placed_move_board = self.game.place_tile(i % 6, i / 6)
			for j in range(4):
				for i in range(2):
					to_return.append(pentago_node(placed_move_board.rotate(j, i == 1), (i % 6, i / 6, j, i == 1)))
		self.children = to_return
		return self.children
