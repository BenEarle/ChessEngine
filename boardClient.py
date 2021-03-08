#################################################
# ChessBoard.py by Ben Earle					#
# Basic pygame board layout for a client.	   #
#################################################
import pygame as pg 
from enum import Enum

pieceFolder = "C:\\Users\\BenEa\\fun_code\\ChessEngine\\pieces\\"
OFFSET = 94
pOFFSET = 100

BLACK = pg.Color('darkgrey')
WHITE = pg.Color('white')
COL = [WHITE, BLACK]

# class Piece(Enum):
WHITE_PAWN = 1
WHITE_BISHOP = 2
WHITE_KNIGHT = 3
WHITE_ROOK = 4
WHITE_KING = 5
WHITE_QUEED = 6

BLACK_PAWN = 11
BLACK_BISHOP = 12
BLACK_KNIGHT = 13
BLACK_ROOK = 14
BLACK_KING = 15
BLACK_QUEED = 16

whitePawn = pg.image.load(pieceFolder + 'wp.png')
whiteBishop = pg.image.load(pieceFolder + 'wb.png')
whiteHorse = pg.image.load(pieceFolder + 'wn.png')
whiteCastle = pg.image.load(pieceFolder + 'wr.png')
whiteKing = pg.image.load(pieceFolder + 'wk.png')
whiteQueen = pg.image.load(pieceFolder + 'wq.png')
blackPawn = pg.image.load(pieceFolder + 'bp.png')
blackBishop = pg.image.load(pieceFolder + 'bb.png')
blackHorse = pg.image.load(pieceFolder + 'bn.png')
blackCastle = pg.image.load(pieceFolder + 'br.png')
blackKing = pg.image.load(pieceFolder + 'bk.png')
blackQueen = pg.image.load(pieceFolder + 'bq.png')

imgMap = {
	WHITE_PAWN : whitePawn,
	WHITE_BISHOP : whiteBishop,
	WHITE_KNIGHT : whiteHorse,
	WHITE_ROOK : whiteCastle,
	WHITE_KING :  whiteKing,
	WHITE_QUEED :  whiteQueen,

	BLACK_PAWN : blackPawn,
	BLACK_BISHOP : blackBishop,
	BLACK_KNIGHT : blackHorse,
	BLACK_ROOK : blackCastle,
	BLACK_KING : blackKing,
	BLACK_QUEED : blackQueen,
}


def get_pixel(x, y):
	return (OFFSET + x*50, OFFSET + y*50)

def get_coordinates(x, y):
	return ((x - pOFFSET)//50, (y - pOFFSET)//50)

def draw_board(screen):
	tile_size = 50
	width, height = 8*tile_size, 8*tile_size
	background = pg.Surface((width, height))
	count = 0
	for y in range(0, height, tile_size):
		for x in range(0, width, tile_size):
			rect = (x, y, tile_size, tile_size)
			pg.draw.rect(background, COL[count%2], rect)
			count += 1

		count += 1

	screen.fill((60, 70, 90))

	# Display a pawn
	screen.blit(background, (100, 100))

def draw_pieces(grid):
	for i in range(8):
		for j in range(8):
			if(grid[i][j] != 0):
				screen.blit(imgMap[grid[i][j]], get_pixel(j,i))


def init_grid():
	grid = [[0 for x in range(8)] for y in range(8)]
	grid[0] = [BLACK_ROOK, BLACK_KNIGHT, BLACK_BISHOP, BLACK_QUEED, BLACK_KING, BLACK_BISHOP, BLACK_KNIGHT, BLACK_ROOK]
	grid[1] = [BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN]
	grid[6] = [WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN]
	grid[7] = [WHITE_ROOK, WHITE_KNIGHT, WHITE_BISHOP, WHITE_QUEED, WHITE_KING, WHITE_BISHOP, WHITE_KNIGHT, WHITE_ROOK]
	return grid



pg.init()

screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()










game_exit = False

grid = init_grid()

while not game_exit:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			game_exit = True
	if event.type == pg.MOUSEBUTTONDOWN:
			# Set the x, y postions of the mouse click
			x, y = event.pos
			print(get_coordinates(x,y))

	draw_board(screen)
	draw_pieces(grid)
	pg.display.flip()
	clock.tick(500)

pg.quit()

