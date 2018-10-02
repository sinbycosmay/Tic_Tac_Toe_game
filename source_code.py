import random
def drawBoard(board):
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
		return "player"	
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
		letter=input().upper()
	if letter=="O":
		return ["O","X"]
	else:
		return ["X","O"]

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
		dupboard.append(i)
	return dupboard	

def isSpaceFree(move,board):
	return board[move]==" "	

def getPlayerMove(board):
	move=" "
	while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(int(move),board):
		print("what is your next move?(1-9)")
		move=input() 
	return int(move)	

def chooseRandomMoveFromList(board,movesList):
	possibleMoves=[]
	for i in movesList:
		if isSpaceFree(i,board):
			possibleMoves.append(i)

	if len(possibleMoves)!=0:
		return random.choice(possibleMoves)
	else:
		return None

def getComputerMove(board,computerLetter):
	if computerLetter=="X":
		playerLetter="O"

	else:
		playerLetter='X'	


	for i in range(1,10):
		copy=getBoardCopy(board)

		if isSpaceFree(i,copy):
			makeMove(copy,computerLetter,i)
			if isWinner(copy,computerLetter):
				return i	

	for i in range(1,10):
		copy=getBoardCopy(board)
		if isSpaceFree(i,copy):
			makeMove(copy,playerLetter,i)
			if isWinner(copy,playerLetter):
				return i			

	move=chooseRandomMoveFromList(board,[1,3,7,9])
	if move!=None:
		return move

	if isSpaceFree(5,board):
		return 5

	return chooseRandomMoveFromList(board,[2,4,6,8])

def isBoardFull(board):
	for i in range(1,10):
		if isSpaceFree(i,board):
			return False
	return True							

print("welcome! to Pulak\'s Tic-Tac-Toe")

while True:
	theBoard=[" "]*10;
	playerLetter,computerLetter= inputLetter()
	turn=whoPlaysFirst()
	print("The "+turn+" will go first")

	gameIsPlaying=True

	while gameIsPlaying:
		if turn=="player":
			drawBoard(theBoard)
			move=getPlayerMove(theBoard)
			makeMove(theBoard,playerLetter,move)
			if isWinner(theBoard,playerLetter):
				drawBoard(theBoard)
				print("You Nailed it!")
				gameIsPlaying=False		

			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print("ITS a TIE!!")
					break;				

				else:
					turn="computer"	


		else:
			move=getComputerMove(theBoard,computerLetter)
			makeMove(theBoard,computerLetter,move)

			if isWinner(theBoard,computerLetter):
				drawBoard(theBoard)
				print("My algo defeated you!")
				gameIsPlaying=False

			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print("ITS a TIE!!")	
				else:
					turn="player"	
						

	if not playAgain():
		break			


