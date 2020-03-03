from termcolor import colored,cprint
class Wall():

	def __init__(self,r,c):
		self.__row = r
		self.__column = c
		self.__board = []

	def set_wall(self):
		for i in range(self.__row):
			self.__board.append([])
			for j in range(0,self.__column): #creating the framework for wall
				self.__board[i].append(' ')		
		self.set_board()
		

	def getcolumn(self):
		return self.__column

	def getrow(self):
		return self.__row
	
	def set_board(self):
		for j in range(self.__column):
			self.__board[0][j] = '#'
			self.__board[1][j] = '#'
			self.__board[36][j] = '#'
			self.__board[37][j] = '#'
		for i in range(self.__row):
			self.__board[i][0] = '#'
			self.__board[i][1] = '#'
			self.__board[i][2] = '#'
			self.__board[i][3] = '#'
			self.__board[i][72] = '#'	#making the borders of the board
			self.__board[i][73] = '#'
			self.__board[i][74] = '#'
			self.__board[i][75] = '#'
		for i in range(0,self.__row):
			for j in range(self.__column):
				if (i-1)%4 == 0 and (j%8 == 0 or j%8 == 1 or j%8 == 2 or j%8 == 3) :
					self.__board[i][j] = '#'
				if i%4 == 0 and (j%8 == 0 or j%8 == 1 or j%8 == 2 or j%8 == 3):
					self.__board[i][j] = '#'


	def clearblast(self):
		for i in range(self.__row):
			for j in range(self.__column):
				if self.__board[i][j] == '^' and self.__board[i][j-1] != '[' and self.__board[i][j+1] != ']':
					self.__board[i][j] = ' '	#clearing the bombblast

	def print_board(self):
		for i in range(self.__row):
			for j in range(self.__column):
				if self.__board[i][j] == '#':
					cprint (self.__board[i][j], 'cyan',end= "")
				elif self.__board[i][j] == '%':							#printing various elements present on the board using color
					cprint(self.__board[i][j], 'green' , end="")
				elif self.__board[i][j] == 'E':
					cprint(self.__board[i][j], 'red' , end ="")
				elif self.__board[i][j] == '[' or self.__board[i][j] == ']':
					cprint(self.__board[i][j], 'yellow', end="")
				elif self.__board[i][j] == '0':
					cprint(self.__board[i][j], 'blue', end = "")
				elif self.__board[i][j] == '^' and self.__board[i][j-1] != '[' and self.__board[i][j+1] != ']':
					cprint(self.__board[i][j],'magenta',end="")
				else:
					print(self.__board[i][j], end= "")
			print()

	def getboard(self):
		return self.__board