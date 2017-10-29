from fifteen_node import *
from heapq import *
from fifteen_puzzle import *
class search:
	def __init__(self, root):
		self.add_to_fringe(root)
		visited = set()
		max_depth = 0
		max_fringe_size = 0		
		print "init search"		

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
		self.show_log()

		self.visited.add(visiting)
		if visiting.get_depth() > self.max_depth:
			self.max_depth = visiting.get_depth()
		for childr_of_visiting in visiting.get_children():
			if childr_of_visiting not in self.visited:
				self.add_to_fringe(childr_of_visiting)
		if len(self.fringe) > self.max_fringe_size:
			self.max_fringe_size = len(self.fringe)
		print "\n\ncurrently visiting \n%s" % visiting.puzzle.format() 
	def add_to_fringe(self, node):
		raise NotImplementedError

	def perform_search(self):
		print "-----------------------------------------------------------------------------------------------"
		goal = fifteen_node(fifteen_puzzle(data=range(16)), None)
		
		print "goal :\n%s" % goal.puzzle.format()
		while goal not in self.visited:
			self.visit_node()





class heuristic_search(search):

	def __init__(self, node):
		search.__init__(self, node)
		self.fringe = []
		print "init heuristic"

	def get_distance_to_goal(self, node):
		raise NotImplementedError

	def get_distance_from_start(self, node):
		return node.get_depth()

	def get_node_cost(self, node):
		return node.get_depth() 

	def pop(self):
		priority, node = heappop(self.fringe)
		return node

	def add_to_fringe(self, node):
		heappush(fringe, (self.get_node_cost(node), node))



class uninformed_search(search):

	def __init__(self, node):
		search.__init__(self, node)
		self.fringe = []
		print "init uninformed"


class BFS(uninformed_search):

	def __init__(self, node):
		uninformed_search.__init__(self, node)
		self.utility_stack = []
		self.fringe = []
		print "init BFS"	

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
	
	def add_to_fringe(node):
		self.fringe.append(node)

	def get_fringe_size(self):
		return len(self.fringe)

	def pop(self):
		popping = self.fringe.pop()
		self.visited.add(popping)
		return popping



class GBFS(heuristic_search):

	def __init__(self, node):
		heuristic_search.__init__(self, node)
		self.next_level = []

	def add_to_fringe(self, node):
		if node.get_depth > self.max_depth:
			heappush(self.next_level, (self.get_node_cost(node), node))
		else:
			heappush(self.fringe, (self.get_node_cost(node), node))

	def get_fringe_size(self):
		return len(self.fringe) + len(self.next_level)

	def get_distance_to_goal(self, node):
		return node.h1()

	def pop(self):
		if len(self.fringe) == 0:
			self.fringe = self.next_level
			self.next_level = []
		return heuristic_search.pop(self)
