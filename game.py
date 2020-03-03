import string
import click
import sys
from termcolor import cprint
from wall import Wall
from man import Person
from bomberman import BomberMan
from enemy import Enemy
from bricks import Brick
from bomb import Bomb
	
def main():
	b = Wall(38,76)
	b.set_wall()
	array = b.getboard()
	man = BomberMan(array)
	enemy = Enemy()
	enemy.setposition(array,b)
	bricks = Brick(2,4)
	bricks.set_bricks(array)
	bomb = Bomb(2,4,0,False,False)
	flag = 0
	count = 0
	while True:
		cprint("Score is "+ str(bomb.get_score()), 'red', attrs=['bold'])
		cprint("Number of lives: " + str(man.getlives()),'green',attrs=['bold'])
		if flag == 4 :
			bomb.blast(array)
			if bomb.getdestroy() == True:
				cprint("YOU HAVE WON :D", 'yellow')
				cprint("Your final score is " + str(bomb.get_score()), 'green', attrs = ['bold'])
				sys.exit()
			if bomb.getdead() == True:
				man.decrementlives()
				if(man.getlives() != 0):
					man.clear_bomberman(array)
					man.afterdeath()
					man.initialise_bomberman(array)
					bomb.setdead(False)
				else:
					cprint("GAME OVER! :'(",'red', attrs = ['bold'])
					sys.exit()

			flag = 0
		elif flag != 0:
			flag = flag + 1
		else:
			pass
		b.print_board()
		b.clearblast()
		b.set_wall()
		if count == 1:
			count = 0
		enemyx = enemy.getx()
		enemyy = enemy.gety()
		manx = man.getx()
		many = man.gety()
		if manx == enemyx and (many == enemyy + 4 or many == enemyy - 4 or many == enemyy):
			man.decrementlives()
			if (man.getlives() != 0):
				man.clear_bomberman(array)
				man.afterdeath()
				man.initialise_bomberman(array)
			else:
				print("GAME OVER! :'(")
				sys.exit()
				
		elif many == enemyy and (manx == enemyx + 2 or manx == enemyx - 2 or manx == enemyx):		#to check whether the enemy is killing the bomberman or not :P
			man.decrementlives()
			if (man.getlives() != 0):
				man.clear_bomberman(array)
				man.afterdeath()
				man.initialise_bomberman(array)
			else:
				print("GAME OVER! :'(")
				sys.exit()
		else:
			pass
		enemy.enemy_motion(array)			#bomb doing shit :/
		inp = click.getchar()
		if inp == 'b' and flag == 0:
			flag = flag + 1
			bomb.get_bomb_coordinates(array,man)	
		elif inp == 'q':
			cprint("You have quit!",'red',attrs=['bold'])
			sys.exit()
		else:
			val = man.movement(array,inp)
			if flag != 0 and val == 1:
				bomb.set_bomb(array,3-flag)
	

if __name__ == "__main__":
	main()
