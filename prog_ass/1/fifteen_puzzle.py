class fifteen_puzzle:

	def __init__(self):
		
		self.data = [" " * (3 - (len(str(i + 1)))) + str(i + 1) for i in range(15)]
		self.data.append("000")


	def format(self):
		to_return = ""
		for i in range(4):
			to_return += str(self.data[4 * i: 4 * i + 4]) + "\n"
		return to_return
