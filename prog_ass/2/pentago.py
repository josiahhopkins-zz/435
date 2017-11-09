class pentago:
	
	def __init__(self):
		self.white_move = True
		self.board = []
		empty = [' ', ' ', ' ']
		for i in range(4):
			self.board.append([])
			for j in range(3):
				self.board[i].append(empty[:])

	def get_tile(self, row, col):
		sector = 0
		if row > 2:
			sector = sector + 2
		if col > 2:
			sector = sector + 1
		row = row % 3
		col = col % 3
		return self.board[sector][row][col]	

	def are_the_same(self, start_row, start_col, down, over):
		if (start_row > 1 and over) or (start_col > 1 and down) or not (down or over):
			return 0
		else:
			place = (start_row, start_col)
			match = self.get_tile(place[0], place[1])
			for i in range(3):
				if down:
					place = (place[0] + 1, place[1])
				if over:
					place = (place[0], place[1] + 1)
					
				if match != self.get_tile(place[0], place[1]):
					return ' '
			return match
				
	
	def has_won(self):
		white_win = False
		black_win = False
		for i in range(36):
			color = self.are_the_same(i % 6, i / 6, True, False)
			white_win = white_win or color == 'w'
			black_win = black_win or color == 'b'
			color = self.are_the_same(i % 6, i / 6, False, True)
			white_win = white_win or color == 'w'
			black_win = black_win or color == 'b'
			color = self.are_the_same(i % 6, i / 6, True, True)
			white_win = white_win or color == 'w'
			black_win = black_win or color == 'b'
			

	def transpose(self, matrix):
		return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

	

	def rotate(self, rotate_sector, clock_wise):
		to_put = self.transpose(self.board[rotate_sector])
		if clock_wise:
			to_put = to_put[::-1]	
		else:	
			for i in range(len(to_put)):
				to_put[i] = to_put[i][::-1]
		self.board[rotate_sector] = to_put

	def show_log(self):
		for i in [0, 2]:
			for j in range(3):
				print self.board[i][j], self.board[i + 1][j]

	def make_move(self, sector, row, column, rotate_sector, clock_wise):
	
		if self.board[sector][row][column] != ' ' or sector > 3 or sector < 0 or row > 2 or row < 0 or column > 2 or column < 0:
			return -1
		else:
			if self.white_move:
				move = 'w'
			else:
				move = 'b'	
			self.board[sector][row][column] = move
			self.white_move = not self.white_move
			self.rotate(rotate_sector, clock_wise)
			return 0

