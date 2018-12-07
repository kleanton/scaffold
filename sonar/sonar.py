# Охотник за сокровищами

import random
import sys
import math


width=60
height=15

def getNewBoard():
	board=[]
	for x in range(width):
		board.append([])
		for y in range(height):
			if random.randint(0,1)==0:
				board[x].append('~')
			else:
				board[x].append('`')
	return board

def drawBoard(board):
	tensDigitsLine=' '
	for i in range(1,6):
		tensDigitsLine+=(' '*9)+str(i)
	print(tensDigitsLine)
	print(' '+('123456789'*6)+str(i))
	print()
	for row in range(height):
		if row<10:
			extraSpace=' '
		else:
			extraSpace=''
		boardRow=''
		for column in range(width):
			boardRow+=board[column][row]
		print('%s%s %s %s' %(extraSpace,row,boardRow,row))
		print()
	print(' '+('0123456789'*6))
	print(tensDigitsLine)

def getRandomChests(numChests):
	chests=[]
	while len(chests)<numChests:
		newChest=[random.randint(0,59), random.randint(0,14)]
		if newChest not in chests:
			chests.append(newChest)
	return chests

def isOnBoard(x,y):
	return x>=0 and x<=59 and y>=0 and y<=14

def makeMove(board,chests,x,y):
	smallestDistance=100
	for cx,cy in chests:
		distance=math.sqrt((cx-x)*(cx-x)+(cy-y)*(cy-y))
		if distance < smallestDistance:
			smallestDistance=distance
	smallestDistance=round(smallestDistance)
	
	if smallestDistance==0:
		chests.remove([x,y])
		board[x][y]='$'
		return 'Вы нашли сундук с сокровищами на затонувшем судне!'

	elif smallestDistance<10:
		board[x][y]=str(smallestDistance)
		return 'Сундук с сокровищами обнаружен в %s милях от гидролокатора' %(smallestDistance)
	else:
		board[x][y]='X'
		return 'В пределах досигаемости гидролокатора ничего не обнаружено'

def enterPlayerMove(previousMoves):
	print('Где опустить гидролокатор? 0-59 0-14 ("выход" для окончания игры)')
	while True:
		move = input()
		if move.lower()=='выход':
			print('Спасибо за игру!')
			sys.exit()
		move=move.split()
		if len(move)==2 and move[0].isdigit() and move[1].isdigit()and isOnBoard(int(move[0]),int(move[1])):
			if [int(move[0]),int(move[1])] in previousMoves:
				print('Здесь уже опускали')
				continue
			return [int(move[0]),int(move[1])]
		else:
			print('Введите число от 0 до 59, потом пробел, а затем число от 0 до 14.')

def showInstructions():
	print('''Вы- капитан корабля, плывущего за сокровищами. Ваша задача с помощью гидролокатора найти три сундука с сокровищами на затонувших судах.
	вы узнаете только расстояние, но не направление. Введите координаты, чтобы опустить гидролокатор в воду. На карте будет показано число, обозначающее
	на каком расстоянии находится ближайший сундук. ''')

print('Охотник за сокровищами')
print()
print('Показать инструкции? да/нет')
if input().lower().startswith('д'):
	showInstructions()

while True:
	sonarDevices=20
	theBoard=getNewBoard()
	theChests=getRandomChests(3)
	drawBoard(theBoard)
	previousMoves=[]
	while sonarDevices>0:
		print('Осталось гидролокаторов:%s. Осталось сундуков с сокровищами:%s'%(sonarDevices,len(theChests)))
		x,y=enterPlayerMove(previousMoves)
		previousMoves.append([x,y])
		moveResult=makeMove(theBoard,theChests,x,y)
		if moveResult==False:
			continue
		elif moveResult=='Вы нашли сундук с сокровищами на затонувшем судне':
			for x,y in previousMoves:
				makeMove(theBoard,theChests,x,y)
		drawBoard(theBoard)
		print(moveResult)
		if len(theChests)==0:
			print('Вы выиграли')
			break
		sonarDevices-=1
		
		if sonarDevices==0:
			print('Игра окончена')
			print('Вы не нашли сундуки. Они были тут:')
			for x,y in theChests:
				print('%s, %s' %(x,y))
			print('хотите сыграть еще раз? д/н')
			if not input().lower().startswith('д'):
				sys.exit()
#MyChests=[]
#maze=getNewBoard()
#drawBoard(maze)
#MyChests=getRandomChests(4)
#print(MyChests)
#print(makeMove(maze,MyChests,5,7))
