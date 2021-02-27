#################################################
# chessServer.py by Ben Earle                   #
# This script acts as the chess server, with    #
# either a real player or a CPU.                #
#################################################
import socket
# Debug will print msgs received and other state info
debug = True
disp_board = True

# Dictionarys for board setup
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

# Print the board from whites perspective
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

# Check if move is legal
# def legal(grid, move):
# 	piece = grid[files[move[1]]][ranks[move[0]]]
# 	source = (files[move[1]], ranks[move[0]])
# 	switch(piece){
# 		case "r":
# 		case "n":
# 		case "b":
# 		case "q":
# 		case "k":
# 		case "p":
# 	}

# 	return True

# Applies a move to board, turn is true if its white's turn
def move(grid, move, turn):
	move = move.lower()

	## TODO: Check if move is legal
	if(move == "0-0-0" or move == "o-o-o"):
		#special case for queen side castle
		if(turn):
			file = "1"
		else: 
			file = "8"
		grid[files[file]][ranks["d"]] = "r"
		grid[files[file]][ranks["c"]] = "k"
		return grid

	elif(move == "0-0" or move == "o-o"):
		#special case for king side castle
		if(turn):
			file = "1"
		else: 
			file = "8"
		grid[files[file]][ranks["f"]] = "r"
		grid[files[file]][ranks["g"]] = "k"
		return grid
	else:
		piece = grid[files[move[1]]][ranks[move[0]]]


		grid[files[move[4]]][ranks[move[3]]] = piece
		grid[files[move[1]]][ranks[move[0]]] = empty

	return grid

# Setup the board in the starting configuration
def setupBoard():

	grid = [[empty for x in range(8)] for y in range(8)] 

	grid[0] = ["r", "n","b","q","k","b","n","r"]
	grid[1] = ["p", "p","p","p","p","p","p","p"]

	grid[6] = ["p", "p","p","p","p","p","p","p"]
	grid[7] = ["r", "n","b","q","k","b","n","r"]

	return grid

# Returns true if the game is over
def checkmate(grid):
	return False

UDP_IP   = "127.0.0.1"
RX_PORT  = 5000
BUFF_LEN = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, RX_PORT))

# tx_sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

# tx_sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
# Setup clients...
playerCount = 0
while playerCount < 2:
	data, addr = sock.recvfrom(BUFF_LEN) # buffer size is 1024 bytes
	if debug:
		print(addr)
		print("%s" % data)

	if data == b"R" and playerCount == 0:
		if debug:
			print("White received...")
		white_addr = addr
		playerCount += 1
		sock.sendto(b"W", white_addr)

	elif data == b"R" and playerCount == 1:
		if debug:
			print("White received...")
		black_addr = addr
		playerCount += 1
		sock.sendto(b"B", black_addr)


# Clients are preped, let's play!
sock.sendto(b"P", white_addr)
sock.sendto(b"P", black_addr)
grid = setupBoard()	
turn = True
while not checkmate(grid):
	if disp_board:
		printBoardWhite(grid)

	if(turn and debug):
		print("white to play")
	elif(debug):
		print("black to play")

	data, addr = sock.recvfrom(BUFF_LEN)
	data = data.lower()

	if(turn and addr == white_addr):
		sock.sendto(data, black_addr)
		if data == b"xk":
			break
		grid = move(grid, data.decode("utf-8"), turn)

	elif(not turn and addr == black_addr):
		sock.sendto(data, white_addr)
		if data == b"xk":
			break
		grid = move(grid, data.decode("utf-8"), turn)
		
	else:
		if(debug):
			print("Recv from wrong addr: " + str(addr))

	turn = not turn


if turn:
	sock.sendto(b"WIN", black_addr)
	sock.sendto(b"LOS", white_addr)
	if debug:
		print("black win")
else:
	sock.sendto(b"WIN", white_addr)
	sock.sendto(b"LOS", black_addr)
	if debug:
		print("white win")

