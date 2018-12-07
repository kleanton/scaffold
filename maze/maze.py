import random


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



maze=getNewBoard()
drawBoard(maze)
