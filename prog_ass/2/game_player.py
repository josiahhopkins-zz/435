from pentago import *

def alpha_beta(depth, minim, node, alpha, beta):
	if node.game.win_state != ' ' or depth == 0:
		return node.game.heuristic()
	value = 100000 
	chosen_move = None
	if minim:
		value = -100000
	for child in node.get_children():
		child_value = None
		if child != None:
			child_value = alpha_beta(depth -1 , not minim, child, alpha, beta)
		if child_value != None:
			if minim:
				if child_value > value:
					chosen_move = child.last_move
				value = max(value, child_value)

				alpha = max(value, chosen_move)
			else: 
				if child_value < value:
					chosen_move = child.last_move
				value = min(value, child_value)
				beta = min(value, beta)
			if beta <= alpha:
				return (value, chosen_move)
	return (value, chosen_move)

def minimax(depth, minim, node):
	if node.game_state.win_state != ' ' or depth == 0:
		return node.game_state.heuristic()
	value = 100000 
	chosen_move = None
	if not minim:
		value = -100000
	for child in node.get_children():
		child_value = None
		if child != None:
			child_value = alpha_beta(depth -1 , not minim, child)
		if minim:
			if child_value > value:
				chosen_move = child.last_move
			value = max(value, child_value)
		else: 
			if child_value < value:
				chosen_move = child.last_move
			value = min(value, child_value)
	return (value, chosen_move)

def redone_alpha_beta(depth, minim, node, alpha, beta):
	if node.game.win_state != ' ' or depth == 0:
		return (node.game.heuristic(), node.last_move)
	if minim:
		value = 10000
		move = None
		for child in node.get_children():
			if child != None:
				child_value = alpha_beta(depth -1 , not minim, child, alpha, beta)[0]
				if value > child_value:
					value = child_value
					move = node.last_move
				beta = min(beta, value)
				if beta <= alpha:
					return (value, move)
		return (value, move)
	else:
		value = -10000
		move = None
		for child in node.get_children():
			if child != None:
				child_value = alpha_beta(depth -1 , not minim, child, alpha, beta)[0]
				if value < child_value:
					value = child_value
					move = node.last_move
				alpha = max(alpha, value)
				if beta <= alpha:
					return (value, move)
		return (value, move)

def redone_minimax(depth, minim, node):
	if node.game.win_state != ' ' or depth == 0:
		return (node.game.heuristic(), node.last_move)
	if minim:
		value = 10000
		move = None
		for child in node.get_children():
			if child != None:
				child_value = minimax(depth -1 , not minim, child, alpha, beta)[0]
				if value > child_value:
					value = child_value
					move = node.last_move
		return (value, move)
	else:
		value = -10000
		move = None
		for child in node.get_children():
			if child != None:
				child_value = minimax(depth -1 , not minim, child, alpha, beta)[0]
				if value < child_value:
					value = child_value
					move = node.last_move
		return (value, move)


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
			print " NOT IMPLEMENTED"	
