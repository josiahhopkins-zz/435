def alpha_beta(depth, min, node, alpha, beta)
	if node.game_state.win_state != ' ' or depth == 0:
		return node.game_state.heuristic()
	value = 100000 
	chosen_move = None
	if not min:
		value = -100000
	for child in node.get_children():
		child_value = alpha_beta(depth -1 , not min, child, alpha, beta)
		if child_value != None
			if min:
				if child_value > value:
					chosen_move = child.last_move
				value = max(value, child_value)

				alpha = max(value, alpha)
			else: 
				if child_value < value:
					chosen_move = child.last_move
				value = min(value, child_value)
				beta = min(value, beta)
			if beta <= alpha:
				return (value, chosen_move)
	return (value, chosen_move)

def minimax(depth, min, node):
	if node.game_state.win_state != ' ' or depth == 0:
		return node.game_state.heuristic()
	value = 100000 
	chosen_move = None
	if not min:
		value = -100000
	for child in node.get_children():
		child_value = alpha_beta(depth -1 , not min, child)
		if min:
			if child_value > value:
				chosen_move = child.last_move
			value = max(value, child_value)
		else: 
			if child_value < value:
				chosen_move = child.last_move
			value = min(value, child_value)
	return (value, chosen_move)

class game:
	def __init__(self, p1=False, p2=True, minimax=False):
		self.current_game = pentago_node(pentago())
		if p1:
			self.p1 = human()
		else:
			if minimax:
				self.p1 = minimax()
			else:
				self.p1 = alpha_beta()
		if p2:
			self.p2 = human()
		else:
			if minimax:
				self.p2 = minimax()
			else:
				self.p2 = alpha_beta()	
	
	def play_move():
		if self.current_game.game.move_state:	
