import re

def get_probabilities(file):
	file_handler = open(file, 'r')
	text = file_handler.read()
	broken = re.findall(r'\w+|\S+', text)
	to_return = {}
	second_to_return = {}

	for i in range(2, len(broken)):
		key = (broken[i - 2], broken[i - 1])
		if (broken[i - 2], broken[i - 1]) not in to_return.keys():
			to_return[key] = {}
		if broken[i] not in to_return[key]:
			to_return[key][broken[i]] = 0
		to_return[key][broken[i]] += 1
		if broken[i - 1] not in second_to_return.keys():
			second_to_return[broken[i - 1]] = []
		second_to_return[broken[i -1]].append(broken[i])
	return (second_to_return, to_return)