from fifteen_node import *
from fifteen_puzzle import *
class search:

	visited = set()
	max_depth = 0
	max_fringe_size = 0


	def __init__(self, root):
		self.add_to_fringe(root)
		

	def get_visited(self):
		return visited
	
	"""
	def get_fringe():

		raise NotImplementedError
	"""

	def pop(self):
		raise NotImplementedError

	
	def get_expanded_number(self):
		return visiting.size()


	def get_max_fringe_size(self):
		return max_fringe_size


	def get_max_depth(self):
		return max_depth


	def get_number_of_created_nodes(self):
		return get_visited.size() + get_fringe.size()

	def print_log(self):
		print "%d, %d, %d, %d" % (self.get_depth(), self.get_number_of_created_nodes(), self.get_expanded_number(), self.get_max_fringe_size())

	def visit_node(self):
		visiting = self.pop()
		visited.add(visiting)
		for childr_of_visiting in visiting.get_children():
			if childr_of_visiting.get_depth() > max_depth:
				max_depth = childr_of_visiting.get_depth()
		if childr_of_visiting not in visited:
			add_to_fringe(childr_of_visiting)
		if len(fringe) > max_fringe_size:
			max_fringe_size = len(fringe)

	def add_to_fringe(self, node):
		raise NotImplementedError

	def perform_search(self):
		goal = fifteen_node(fifteen_puzzle(), None)
		while goal not in self.visited:
			self.visit_node()
			






class heuristic_search(search):
	fringe = []

	def get_distance_to_goal(self, node):
		raise NotImplementedError

	def get_distance_from_start(self, node):
		return node.get_depth()

	def get_node_cost(self, node):
		raise NotImplementedError

	def pop(self):
		priority, node = heappop(fringe)
		return node

	def add_to_fringe(self, node):
		heappush(fringe, (self.get_node_cost(node), node))



class uninformed_search(search):
	fringe = []



class BFS(uninformed_search):
	utility_stack = []	
	
	def add_to_fringe(self, node):
		self.fringe.append(node)	

	def pop(self):
		if len(self.utility_stack) == 0:
			while len(self.fringe) != 0:
				self.utility_stack.append(self.fringe.pop())
		popping = self.utility_stack.pop()
		print "Trying to add type %s" (str(type(popping)))
		self.visited.add(popping)
		return popping

class DFS(uninformed_search):
	def pop(self):
		popping = fringe.pop()
		visited.add(popping)
		return popping
