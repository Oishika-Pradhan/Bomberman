from man import Person
from wall import Wall
class Bomb():
	def __init__(self,r,c,s,val,dead):
		self.__r = r
		self.__c = c
		self.__score = s
		self.__destroy_enemy = val
		self.__dead = False

	def get_bomb_coordinates(self,board,bman):
		self.r = bman.getx()
		self.c = bman.gety()

	def get_score(self):
		return self.__score

	def set_bomb(self,board,flag):
		board[self.r][self.c] = str(flag)
		board[self.r][self.c+1] = str(flag)
		board[self.r][self.c+2] = str(flag)
		board[self.r][self.c+3] = str(flag)
		board[self.r+1][self.c] = str(flag)
		board[self.r+1][self.c+1] = str(flag)
		board[self.r+1][self.c+2] = str(flag)
		board[self.r+1][self.c+3]= str(flag)

	def getdead(self):
		return self.__dead

	def setdead(self,val):
		self.__dead = val

	def getdestroy(self):
		return self.__destroy_enemy

	def set_blast(self,board,row,column):
		if board[row][column] == 'E' or board[row][column + 1] == 'E' or board[row][column + 2] == 'E' or board[row][column + 3] == 'E' or board[row+1][column] == 'E' or board[row+1][column + 1] == 'E' or board[row+1][column+3]== 'E':
			self.__score = self.__score + 100
			self.destroy_enemy = True
		elif board[row][column] == '%' or board[row][column + 1] == '%' or board[row][column + 2] == '%' or board[row][column + 3] == '%' or board[row+1][column] == '%' or board[row+1][column + 1] == '%' or board[row+1][column+3]== '%':
			self.__score = self.__score + 20
		elif board[row][column] == '[' or board[row][column + 1] == '[' or board[row][column + 2] == '[' or board[row][column + 3] == '[' or board[row+1][column] == '[' or board[row+1][column + 1] == '[' or board[row+1][column+3]== '[':
			self.__dead = True
		board[row][column] = '^'
		board[row][column + 1] = '^'
		board[row][column + 2] = '^'
		board[row][column + 3] = '^'
		board[row+1][column] = '^'
		board[row+1][column + 1] = '^'
		board[row+1][column + 2] = '^'
		board[row+1][column+3]= '^'

	def clearbomb(self,board):
		board[self.r][self.c] = ' '
		board[self.r][self.c+1] = ' '
		board[self.r][self.c+2] = ' '
		board[self.r][self.c+3] = ' '
		board[self.r+1][self.c] = ' '
		board[self.r+1][self.c+1] = ' '
		board[self.r+1][self.c+2] = ' '
		board[self.r+1][self.c+3]= ' '

	def blast(self,board):
		if board[self.r - 1][self.c] != '#' and board[self.r + 2][self.c] != '#' and board[self.r][self.c - 1] != '#' and board[self.r][self.c+4] != '#':
			self.set_blast(board,(self.r-2),self.c)
			self.set_blast(board,self.r+2,self.c)
			self.set_blast(board,self.r,self.c-4)
			self.set_blast(board,self.r,self.c+4)
			self.clearbomb(board)
		elif board[self.r-1][self.c] == '#' and board[self.r + 2][self.c] == '#' and self.r + 2 != 36 or (self.r-1 == 1  and board[self.r-1][self.c] == '#' and board[self.r + 2][self.c] == '#') :
			self.set_blast(board,self.r,self.c-4)
			self.set_blast(board,self.r+2, self.c-4)
			self.set_blast(board,self.r,self.c+4)
			self.set_blast(board,self.r+2,self.c+4)
			self.clearbomb(board)
		elif board[self.r-1][self.c] == '#' and board[self.r + 2][self.c] == '#' and self.r + 2 == 36:
			self.set_blast(board,self.r,self.c-4)
			self.set_blast(board,self.r-2, self.c-4)
			self.set_blast(board,self.r,self.c+4)
			self.set_blast(board,self.r-2,self.c+4)
			self.clearbomb(board)
		elif board[self.r - 1][self.c] == '#' and board[self.r][self.c-1] == '#':
			self.set_blast(board,self.r,self.c+4)
			self.set_blast(board,self.r, self.c+8)
			self.set_blast(board,self.r+2,self.c)
			self.set_blast(board,self.r+4,self.c)
			self.clearbomb(board)
		elif board[self.r - 1][self.c] == '#' and board[self.r][self.c+4] == '#':
			self.set_blast(board,self.r,self.c-4)
			self.set_blast(board,self.r, self.c-8)
			self.set_blast(board,self.r+2,self.c)
			self.set_blast(board,self.r+4,self.c)
			self.clearbomb(board)
		elif board[self.r+2][self.c] == '#' and board[self.r][self.c-1] == '#':
			self.set_blast(board,self.r,self.c+4)
			self.set_blast(board,self.r, self.c+8)
			self.set_blast(board,self.r-2,self.c)
			self.set_blast(board,self.r-4,self.c)
			self.clearbomb(board)
		elif board[self.r+2][self.c] == '#' and board[self.r][self.c+4] == '#':
			self.set_blast(board,self.r,self.c-4)
			self.set_blast(board,self.r, self.c-8)
			self.set_blast(board,self.r-2,self.c)
			self.set_blast(board,self.r-4,self.c)
			self.clearbomb(board)
		elif board[self.r + 2][self.c] == '#' and board[self.r - 1][self.c] == ' ':
			self.set_blast(board,self.r,self.c-4)
			self.set_blast(board,self.r, self.c-8)
			self.set_blast(board,self.r,self.c + 4)
			self.set_blast(board,self.r,self.c + 8)
			self.clearbomb(board)
		elif board[self.r -1][self.c] == '#' and board[self.r + 2][self.c] == ' ':
			self.set_blast(board,self.r,self.c-4)
			self.set_blast(board,self.r, self.c-8)
			self.set_blast(board,self.r,self.c + 4)
			self.set_blast(board,self.r,self.c + 8)
			self.clearbomb(board)
		elif (board[self.r][self.c - 1] == ' ' or board[self.r][self.c+4] == '#') and (self.c-1 == 3 or self.c+4 == 72):
			self.set_blast(board,self.r+2,self.c)
			self.set_blast(board,self.r+4, self.c)
			self.set_blast(board,self.r-2,self.c)
			self.set_blast(board,self.r-4,self.c)
			self.clearbomb(board)
		elif (board[self.r][self.c - 1] == ' ' and board[self.r][self.c+4] == '#')  and (self.c-1 == 3 or self.c+4 == 72):
			self.set_blast(board,self.r+2,self.c)
			self.set_blast(board,self.r+4, self.c)
			self.set_blast(board,self.r-2,self.c)
			self.set_blast(board,self.r-4,self.c)
			self.clearbomb(board)
		elif board[self.r][self.c - 1] == '#' and board[self.r][self.c+4] == ' ' and (self.r - 1 != 1 or self.r+1 != 36):
			self.set_blast(board,self.r+2,self.c)
			self.set_blast(board,self.r+4, self.c)
			self.set_blast(board,self.r-2,self.c)
			self.set_blast(board,self.r-4,self.c)
			self.clearbomb(board)
		elif board[self.r][self.c-1] == '#' and board[self.r][self.c+4] == '#' and ((self.c - 1) == 3 or self.c + 4 == 72):
			self.set_blast(board,self.r-2,self.c)
			self.set_blast(board,self.r-2, self.c+4)
			self.set_blast(board,self.r+2,self.c)
			self.set_blast(board,self.r+2,self.c+4)
			self.clearbomb(board)
		elif board[self.r][self.c-1] == '#' and board[self.r][self.c+4] == '#':
			self.set_blast(board,self.r+2,self.c-4)
			self.set_blast(board,self.r+2, self.c)
			self.set_blast(board,self.r-2,self.c)
			self.set_blast(board,self.r-2,self.c+4)
			self.clearbomb(board)

		else:
			pass