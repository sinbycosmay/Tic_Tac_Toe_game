import random
def draw(board):
	print("     |       |       ")
	print(" "+board[7]+"   |"+board[8]+"      |"+board[9])
	print("-------------------")					

	print("     |       |       ")
	print(" "+board[4]+"   |"+board[5]+"      |"+board[6])
	print("-------------------")


	print("     |       |       ")
	print(" "+board[1]+"   |"+board[2]+"      |"+board[3])


def whoPlaysFirst():
	if random.randint(0,1)==0:
		return "computer"

	else:
		return "Player"	
def playAgain():
	print("Would you like to play again??(yes or no)")
	if input().lower().startswith("y"):
		return 1
	else:
		print("Thanks for playing")

def inputLetter():
	letter=""
	while letter!="X" and letter!="O":
		print("Do u want to be \"X\" or \"O\" )")
		input().upper()
	if letter=="O":
		return ["O","X"]
	else:
		return ["O","X"]

def makeMove(board,letter,move):
	board[move]=letter

def isWinner(board,letter):
	return ((board[7]==letter and board[8]==letter and board[9]==letter)or
		   (board[4]==letter and board[5]==letter and board[6]==letter) or
		   (board[1]==letter and board[2]==letter and board[3]==letter) or
		   (board[1]==letter and board[4]==letter and board[7]==letter) or		
		   (board[2]==letter and board[5]==letter and board[8]==letter) or
		   (board[3]==letter and board[6]==letter and board[9]==letter) or
		   (board[1]==letter and board[5]==letter and board[9]==letter) or
		   (board[7]==letter and board[5]==letter and board[3]==letter))


def getBoardCopy(board):
	dupboard=[]
	for i in board:
		dupboard.append(board[i])
	return dupboard	

def isSpaceFree(move,board):
	return board[move]==" "	

def getPlayerMove(board):
	move=" "
	while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(int(move),board):
		print("what is your next move?(1-9)")
		move=input() 
	return int(move)	

def RandomMoveFromList(board,movesList):
	possibleMoves=[]
	for i in movesList:
		if isSpaceFree(i,board):
			possibleMoves.append(i)

	if len(possibleMoves)!=0:
		return random.choice(possibleMoves)
	else:
		return None

def getComputerMove()




if __name__=="__main__":
	board=[" "]*10
	draw(board)
