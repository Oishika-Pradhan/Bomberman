from wall import Wall
from man import Person
class BomberMan(Person):

	def __init__(self,board):
		self.x = 2
		self.y = 4
		self.lives = 3
		self.prevx = 0
		self.prevy = 0
		board[self.x][self.y] = '['
		board[self.x][self.y+1] = '^'
		board[self.x][self.y+2] = '^'
		board[self.x][self.y+3] = ']'
		board[self.x+1][self.y+1] = ']'
		board[self.x+1][self.y+2] = '['

	def getlives(self):
		return self.lives

	def decrementlives(self):
		self.lives = self.lives - 1

	def change(self):
		self.x = self.prevx
		self.y = self.prevy

	def store_prev_coordinates(self,board):
		self.prevx = self.x
		self.prevy = self.y

	def restore_bman(self,board):
		board[self.prevx][self.prevy] = '['
		board[self.prevx][self.prevy+1] = '^'
		board[self.prevx][self.prevy+2] = '^'
		board[self.prevx][self.prevy+3] = ']'
		board[self.prevx+1][self.prevy+1] = ']'
		board[self.prevx+1][self.prevy+2] = '['

	def clear_bomberman(self,board):
		board[self.x][self.y] = ' '
		board[self.x][self.y+1] = ' '
		board[self.x][self.y+2] = ' '
		board[self.x][self.y+3] = ' '
		board[self.x+1][self.y+1] = ' '
		board[self.x+1][self.y+2] = ' '
	
	def initialise_bomberman(self,board):
		board[self.x][self.y] = '['
		board[self.x][self.y+1] = '^'
		board[self.x][self.y+2] = '^'
		board[self.x][self.y+3] = ']'
		board[self.x+1][self.y+1] = ']'
		board[self.x+1][self.y+2] = '['

	def after_bomb_drop(self,board):
		board[self.prevx][self.prevy] = '['
		board[self.prevx][self.prevy+1] = '^'
		board[self.prevx][self.prevy+2] = '^'
		board[self.prevx][self.prevy+3] = ']'
		board[self.prevx+1][self.prevy+1] = ']'
		board[self.prevx+1][self.prevy+2] = '['

	def afterdeath(self):
		self.x = 2
		self.y = 4


	def movement(self,board,inp):
		flag = 0
		if inp =='w':
			if (board[self.x-2][self.y] != '#' and board[self.x-2][self.y] != '%' and board[self.x-2][self.y] != '0' and board[self.x-2][self.y] != 'E' and board[self.x-2][self.y] != '1'):
				flag = 1
				self.clear_bomberman(board)
				self.store_prev_coordinates(board)
				self.x = self.x - 2
		elif inp =='a':
			if (board[self.x][self.y-4] != '#' and board[self.x][self.y-4] != '%' and board[self.x][self.y-4] != '0' and board[self.x][self.y-4] != 'E' and board[self.x][self.y-4] != '1'):
				flag = 1
				self.clear_bomberman(board)
				self.store_prev_coordinates(board)
				self.y = self.y - 4
		elif inp =='s':
			if (board[self.x + 2][self.y] != '#' and board[self.x + 2][self.y] != '%' and board[self.x + 2][self.y] != '0' and board[self.x + 2][self.y] != 'E' and board[self.x + 2][self.y] != '1'):
				flag = 1
				self.clear_bomberman(board)
				self.store_prev_coordinates(board)
				self.x = self.x + 2
		elif inp =='d':
			if (board[self.x][self.y + 4] != '#' and board[self.x][self.y + 4] != '%' and board[self.x][self.y + 4] != '0' and board[self.x][self.y + 4] != 'E' and board[self.x][self.y + 4] != '1'):
				flag = 1
				self.clear_bomberman(board)
				self.store_prev_coordinates(board)
				self.y = self.y + 4
		else:
			pass
		self.initialise_bomberman(board)
		return flag