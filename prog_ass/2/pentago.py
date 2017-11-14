from copy import *
import math
class pentago:
	
	def __init__(self):
		self.white_move = True
		self.win_state = ' '
		self.board = []
		self.value = None
		empty = [' ', ' ', ' ']
		for i in range(4):
			self.board.append([])
			for j in range(3):
				self.board[i].append(empty[:])

	def __copy__(self):
		cls = self.__class__
		new = pentago()
		new.board = deepcopy(self.board)
		new.win_state = self.win_state
		new.white_move = self.white_move		
		new.value = None
		return new

	def place_tile_with_sector(self, sector, row, column):
		to_return = copy(self)
		if self.win_state != ' ' or self.board[sector][row][column] != ' ' or sector > 3 or sector < 0 or row > 2 or row < 0 or column > 2 or column < 0:
			return None
		else:
			if self.white_move:
				move = 'w'
			else:
				move = 'b'	
			to_return.board[sector][row][column] = move
			print "was " + str(self.white_move)
			to_return.white_move = not self.white_move
		to_return.has_won()
		print "now " + str(to_return.white_move)
		return to_return
		
	def place_tile(self, row, col):
		sector = 0
		if row > 2:
			sector = sector + 2
		if col > 2:
			sector = sector + 1
		row = row % 3
		col = col % 3
		return self.place_tile_with_sector(sector, row, col)	

	def get_tile(self, row, col):
		if row > 5 or col > 5:
			return None
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
			return ' '
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
		if self.win_state == ' ':
			white_win = False
			black_win = False
			is_filled = True
			for i in range(36):
				is_filled = is_filled and self.get_tile(i % 6, int(math.floor(i / 6))) == ' '
				color = self.are_the_same(i % 6, int(math.floor(i / 6)), True, False)
				white_win = white_win or color == 'w'
				black_win = black_win or color == 'b'
				color = self.are_the_same(i % 6, int(math.floor(i / 6)), False, True)
				white_win = white_win or color == 'w'
				black_win = black_win or color == 'b'
				color = self.are_the_same(i % 6, int(math.floor(i / 6)), True, True)
				white_win = white_win or color == 'w'
				black_win = black_win or color == 'b'
			if black_win and not white_win:
				self.win_state = 'b'
			elif white_win and not black_win:
				self.win_state = 'w'
			elif is_filled or (white_win and black_win):
				self.win_state = 't'
			else:
				self.win_state = ' '
			

	def transpose(self, matrix):
		return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

	

	def rotate(self, rotate_sector, clock_wise):
		if  self.win_state != ' ' or rotate_sector > 3 or rotate_sector < 0:
			return None
		to_return = copy(self)
		to_put = self.transpose(self.board[rotate_sector])
		if clock_wise:
			to_put = to_put[::-1]	
		else:	
			for i in range(len(to_put)):
				to_put[i] = to_put[i][::-1]
		to_return.board[rotate_sector] = to_put
		to_return.has_won()
		return to_return

	def show_log(self):
		for i in [0, 2]:
			for j in range(3):
				print self.board[i][j], self.board[i + 1][j]

	def make_move(self, sector, row, column, rotate_sector, clock_wise):
		to_return = copy(self)
		if self.board[sector][row][column] != ' ' or sector > 3 or sector < 0 or row > 2 or row < 0 or column > 2 or column < 0:
			return None
		else:
			if self.white_move:
				move = 'w'
			else:
				move = 'b'	
			to_return.board[sector][row][column] = move
			to_return.white_move = not self.white_move
			to_return.rotate(rotate_sector, clock_wise)
			return to_return

	def get_in_a_row(self, start_row, start_col, down, over):
		place = (start_row, start_col)
		match = self.get_tile(place[0], place[1])
		for i in range(4):
			if down:
				place = (place[0] + 1, place[1])
			if over:
				place = (place[0], place[1] + 1)					
			if match != self.get_tile(place[0], place[1]):
				return i
			return 4 + 1

	def heuristic(self):
		if self.win_state == 'b':
			return -500
		if self.win_state == 'w':
			return 500
		if self.win_state == 't':
			return 0
		total = 0
		multiplier = 1
		for i in range(36):
			tile =  self.get_tile(i % 6, int(math.floor(i / 6))) 
			if tile == 'b':
				multiplier = -1
			elif tile == 'w':
				multiplier = 1
			else:
				multiplier = 0 
			total += multiplier * self.get_in_a_row(i % 6, int(math.floor(i / 6)), True, False)
			total += multiplier * self.get_in_a_row(i % 6, int(math.floor(i / 6)), False, True)
			total += multiplier * self.get_in_a_row(i % 6, int(math.floor(i / 6)), True, True)
		return total

	def get_heuristic(self):
		if self.value == None:
			self.value = self.heuristic()
		return self.value
