from wall import Wall
import random

class Brick(Wall):
	

	def set_bricks(self,board):
		num = random.randint(5,10)
		for i in range(num):
			m = random.randrange(6,34,2)
			n = random.randrange(12,68,4)
			while(board[m][n] != ' '):
				m = random.randrange(6,34,2)
				n = random.randrange(12,68,4)
			self.r = m
			self.c = n
			board[self.r][self.c] = '%'
			board[self.r][self.c+1] = '%'
			board[self.r][self.c+2] = '%'
			board[self.r][self.c+3] = '%'
			board[self.r+1][self.c] = '%'
			board[self.r+1][self.c+1] = '%'
			board[self.r+1][self.c+2] = '%'
			board[self.r+1][self.c+3]= '%'