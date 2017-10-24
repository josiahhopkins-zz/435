class fifteen_puzzle:	
	def __init__(self):
		keys = range(15)
		values = [" " * (3 - (len(str(i + 1)))) + str(i + 1) for i in range(15)]	
		self.empty = 15
		self.data = range(16)
		self.mapper = dict(zip(keys, values))
		self.mapper.update({15:" XX"})

	def shift(self, shift_key):
		self.data[self.empty] = self.data[self.empty + shift_key]
		self.data[self.empty + shift_key] = 15
		self.empty = self.empty + shift_key		

	def move(self, op):
		if op == "up" and self.empty > 3:
			self.shift(-4)
		elif op == "down" and self.empty < 12 :
			self.shift(4)
		elif op == "left" and self.empty % 4 != 0:
			self.shift(-1)
		elif op == "right" and self.empty% 4 != 3:
			self.shift(1)
	
	def is_in_order(self):
		return self.data == sorted(self.data) 

	def format(self):
		to_return = ""
		for i in range(4):
			for j in self.data[4 * i: 4 * i + 4]:
				to_return += self.mapper[j]
			to_return += "\n"
		return to_return
