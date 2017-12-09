from text_analysis import *
import random
import bisect

class producer_analyzer:

	def __init__(self, source_file):
		self.one_layer, two_layer = get_probabilities(source_file)
		self.count = self.reverse_count(two_layer)

	def reverse_count(self, count_map):
		the_map = {}
		for key in count_map.keys():
			total = 0 
			count_values = []
			corespondant = []
			for value in count_map[key].keys():
				total += count_map[key][value]
				count_values.append(total - 1)
				corespondant.append(value)
			the_map[key] = (total, count_values, corespondant)
		return the_map
	
	def get_choice(self, second_last, last):
		brute_index = random.randint(self.count[(second_last, last)][0])
		true_index = bisect.bisect_left(self.count[(second_last, last)][1]) - 1
		return self.count[(second_last, last)][2][true_index]

	def generate_file(self, output_file):
		god_i_am_so_ready_to_graduate = open(output_file, 'w')
		second_last = random.choice(self.one_layer.keys())
		print second_last
		last = random.choice(self.one_layer[second_last])
		print last
		#print second_last, last
		god_i_am_so_ready_to_graduate.write(second_last + " ")
		god_i_am_so_ready_to_graduate.write(last + " ")
		for i in range(998):
			new = self.get_choice(second_last, last)
			god_i_am_so_ready_to_graduate.write(new + " ")
			second_last = last
			last = new

