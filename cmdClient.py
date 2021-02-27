#################################################
# chessClient.py by Ben Earle                   #
# This script acts as the chess client, with    #
# a real player or sending moves via commandline#
#################################################

import socket

def getMove():
	return str.encode(input("Move: "))

IP = "127.0.0.1"
SERVER_PORT = 5000
MESSAGE = b"R"
COL = ""
print("UDP target IP: %s" % IP)
print("UDP target port: %s" % SERVER_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(b"R", (IP, SERVER_PORT))

data, addr = sock.recvfrom(1024)
print(data)
if(data == b"W" or data == b"B"):
	COL = data
else:
	print("Error connecting...")
	quit()

data, addr = sock.recvfrom(1024)

if(data != b"P"):
	print("Error connecting...")
	quit()

if(COL == b"W"):
	# Play a Move 
	sock.sendto(getMove(), (IP, SERVER_PORT))

playing = True
while playing:
	# Recieve a move
	data, addr = sock.recvfrom(1024)

	# Update game state in agent [almost-existant]
	if(data == b"xk"):
		playing = False

	# Play a Move 
	move = getMove()
	if(move == b"xk"):
		playing = False

	sock.sendto(move, (IP, SERVER_PORT))