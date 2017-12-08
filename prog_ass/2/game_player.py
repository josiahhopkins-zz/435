class game_player:
	
	def get_move(self):
		raise NotImplementedError

class human:
	def get_move():
		raise NotImplementedError

class cli_human:
	def get_choice():
		
class alpha_beta:
	def get_move(depth, min, node, alpha, beta)

		return (value, chosen_move)

class minimax:



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
