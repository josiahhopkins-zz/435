class search:

	visited = set()
	max_depth = 0
	max_fringe_size = 0


	def __init__(root):
		self.add_to_fringe(root)
		

	def get_visited():
		return visited
	
	"""
	def get_fringe():

		raise NotImplementedError
	"""

	def pop():
		raise NotImplementedError

	
	def get_expanded_number():
		return visiting.size()


	def get_max_fringe_size():
		return max_fringe_size


	def get_max_depth():
		return max_depth


	def get_number_of_created_nodes():
		return get_visited.size() + get_fringe.size()

	def print_log(self):
		print "%d, %d, %d, %d" % (self.get_depth(), self.get_number_of_created_nodes(), self.get_expanded_number(), self.get_max_fringe_size())

	def visit_node():
		visiting = self.pop()
		visited.add(visiting)
		for childr_of_visiting in visiting.get_children():
			if childr_of_visiting.get_depth() > max_depth:
				max_depth = childr_of_visiting.get_depth()
		if(childr_of_visiting not in visited )
			add_to_fringe(childr_of_visiting)
		if fringe.size() > max_fringe_size:
			max_fringe_size = fringe.size()

	def add_to_fringe(node):
		raise NotImplementedError

	def perform_search():
		goal = fifteen_
		while







class heuristic_search(search):
	fringe = []

	def get_distance_to_goal(node):
		raise NotImplementedError

	def get_distance_from_start(node):
		return node.get_depth()

	def get_node_cost(node):
		raise NotImplementedError

	def pop():
		priority, node = heappop(fringe)
		return node

	def add_to_fringe(node):
		heappush(fringe, (self.get_node_cost(node), node))



class uninformed_search(search):
	fringe = Stack()



class BFS(uninformed_search):
	utility_stack = Stack()

	def pop():
		if utility_stack.size() == 0:
			while fringe.size() != 0:
				utility_stack.append(fringe.pop())
		popping = utility_stack.pop()
		visited.add(popping)
		return popping

class DFS(uninformed_search):
	def pop():
		popping = fringe.pop()
		visited.add(popping)
		return popping

def h1(node):


def h2(node)