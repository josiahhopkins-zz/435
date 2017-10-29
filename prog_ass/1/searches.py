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
		return len(self.visited)

	
	def get_fringe_size(self):
		raise NotImplementError	


	def get_max_fringe_size(self):
		return self.max_fringe_size


	def get_max_depth(self):
		return self.max_depth


	def get_number_of_created_nodes(self):
		return len(self.visited) + self.get_fringe_size()

	def show_log(self):
		print "%d, %d, %d, %d" % (self.get_max_depth(), self.get_number_of_created_nodes(), self.get_expanded_number(), self.get_max_fringe_size())

	def visit_node(self):
		visiting = self.pop()
		self.visited.add(visiting)
		if visiting.get_depth() > self.max_depth:
			self.max_depth = visiting.get_depth()
		for childr_of_visiting in visiting.get_children():
			if childr_of_visiting not in self.visited:
				self.add_to_fringe(childr_of_visiting)
		if len(self.fringe) > self.max_fringe_size:
			self.max_fringe_size = len(self.fringe)

	def add_to_fringe(self, node):
		raise NotImplementedError

	def perform_search(self):
		goal = fifteen_node(fifteen_puzzle(data=range(16)), None)
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

	def get_fringe_size(self):
		return len(self.fringe) + len(self.utility_stack)

	def pop(self):
		if len(self.utility_stack) == 0:
			while len(self.fringe) != 0:
				self.utility_stack.append(self.fringe.pop())
		
		popping = self.utility_stack.pop()
		self.visited.add(popping)
		return popping

class DFS(uninformed_search):
	
	def add_to_fringe(self, node):
		self.fringe.append(node)

	def get_fringe_size(self):
		return len(self.fringe)

	def pop(self):
		popping = self.fringe.pop()
		self.visited.add(popping)
		return popping
