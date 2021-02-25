#################################################
# ChessBoard.py by Ben Earle                    #
# C:/Ben/ChessEngine/ChessBoard.py              #
#################################################
# from enum import Enum

# class File(Enum):
# 	A = 0
# 	B = 1
# 	C = 2
# 	D = 3
# 	E = 4
# 	F = 5
# 	G = 6
# 	H = 7

# class abstract_piece:
# 	def __init__():

# 	def legal_moves(board) -> Move[]:
# 		pass
empty = '-' #'■'
files = {
	"1": 7,
	"2": 6,
	"3": 5,
	"4": 4,
	"5": 3,
	"6": 2,
	"7": 1,
	"8": 0
}

ranks = {
	"a": 0,
	"b": 1,
	"c": 2,
	"d": 3,
	"e": 4,
	"f": 5,
	"g": 6,
	"h": 7
}
def printBoardWhite(grid):
	print("   a b c d e f g h ")
	print("  +---------------+ ")
	for i in range(8):
		line = str(8-i) + " |"
		line = line + str(grid[i][0]) 
		for j in range(1, 8):
			line = line + " " + str(grid[i][j]) 
	
		line = line + "| " + str(8-i)
		print(line)
	print("  +---------------+ ")
	print("   a b c d e f g h  ")
	print()

# Applies a move to board
def move(grid, notation):
	notation = notation.lower()

	## TODO: Check if move is legal
	if(notation == "0-0-0" or notation == "O-O-O"):
		#special case for queen side castle
		return grid

	elif(notation == "0-0" or notation == "O-O"):
		#special case for king side castle
		return grid
	else:
		piece = grid[files[notation[1]]][ranks[notation[0]]]


		grid[files[notation[4]]][ranks[notation[3]]] = piece
		grid[files[notation[1]]][ranks[notation[0]]] = empty

	return grid


def setupBoard():

	grid = [[empty for x in range(8)] for y in range(8)] 

	grid[0] = ["r", "n","b","q","k","b","n","r"]
	grid[1] = ["p", "p","p","p","p","p","p","p"]

	grid[6] = ["p", "p","p","p","p","p","p","p"]
	grid[7] = ["r", "n","b","q","k","b","n","r"]

	return grid

grid = setupBoard()
printBoardWhite(grid)
grid = move(grid, "E2-E4")
printBoardWhite(grid)
grid = move(grid, "E7-E5")
printBoardWhite(grid)