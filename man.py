from wall import Wall
import random

class Person():

	def __init__ (self,board):
		self.__x = 2
		self.__y = 4
		self.__lives = 3
		board[4][2] = '['
		board[4][3] = '^'
		board[4][4] = '^'
		board[4][5] = ']'
		board[5][3] = ']'
		board[5][4] = '['

	def getx(self):
		return self.x

	def gety(self):
		return self.y