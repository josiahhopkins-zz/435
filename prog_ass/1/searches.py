class search:

	visited = []
	fringe = []

	def get_visited():
		raise NotImplementedError
	
	def get_fringe():

		raise NotImplementedError
	
	def peek():
		raise NotImplementedError


	def pop():
		raise NotImplementedError

	
	def get_expanded_number():
		raise NotImplementedError


	def get_max_fringe_size():
		raise NotImplementedError


	def is_heuristic_guided():
		raise NotImplementedError


	def get_depth():
		raise NotImplementedError


	def get_number_of_created_nodes():
		raise NotImplementedError


	def get_distance_to_goal(node):
		raise NotImplementedError


	def get_distance_traveled(node):
		raise NotImplementedError


		
