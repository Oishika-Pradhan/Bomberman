from man import Person
from wall import Wall
import random
class Enemy(Person):

	def __init__(self):
		self.x = random.randint(1,20)
		self.y = random.randint(1,20)

	def setposition(self,board,b):
		m = random.randrange(6,34,2)
		n = random.randrange(12,68,4)
		while(board[m][n] != ' '):
			m = random.randrange(6,34,2)
			n = random.randrange(12,68,4)
		self.x = m
		self.y = n
		board[self.x][self.y] = 'E'
		board[self.x][self.y+1] = 'E'
		board[self.x][self.y+2] = 'E'
		board[self.x][self.y+3] = 'E'
		board[self.x+1][self.y] = 'E'
		board[self.x+1][self.y+1] = 'E'
		board[self.x+1][self.y+2] = 'E'
		board[self.x+1][self.y+3]= 'E'

	def clear_enemy(self,board):
		board[self.x][self.y] = ' '
		board[self.x][self.y+1] = ' '
		board[self.x][self.y+2] = ' '
		board[self.x][self.y+3] = ' '
		board[self.x+1][self.y] = ' '
		board[self.x+1][self.y+1] = ' '
		board[self.x+1][self.y+2] = ' '
		board[self.x+1][self.y+3] = ' '


	def initialise_enemy(self,board):
		board[self.x][self.y] = 'E'
		board[self.x][self.y+1] = 'E'
		board[self.x][self.y+2] = 'E'
		board[self.x][self.y+3] = 'E'
		board[self.x+1][self.y] = 'E'
		board[self.x+1][self.y+1] = 'E'
		board[self.x+1][self.y+2] = 'E'
		board[self.x+1][self.y+3]= 'E'

	def enemy_motion(self,board):
		num = random.randint(1,4)
		'''print(num)'''
		if num == 1:
			if (board[self.x-2][self.y] != '#' and board[self.x-2][self.y] != '%' and board[self.x-2][self.y] != '0' and board[self.x-2][self.y] != '1'):
				self.clear_enemy(board)
				self.x = self.x - 2
		
		elif num == 2:
			if (board[self.x][self.y-4] != '#' and board[self.x][self.y-4] != '%' and board[self.x][self.y-4] != '0' and board[self.x][self.y-4] != '1'):
				self.clear_enemy(board)
				self.y = self.y - 4
	
		elif num == 3:
			if (board[self.x + 2][self.y] != '#' and board[self.x + 2][self.y] != '%' and board[self.x + 2][self.y] != '0' and board[self.x + 2][self.y] != '1'):
				self.clear_enemy(board)
				self.x = self.x + 2
	
		elif num == 4:
			if (board[self.x][self.y + 4] != '#' and board[self.x][self.y + 4] != '%' and board[self.x][self.y + 4] != '0' and board[self.x][self.y + 4] != '1'):
				self.clear_enemy(board)
				self.y = self.y + 4
		self.initialise_enemy(board)