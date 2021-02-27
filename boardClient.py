#################################################
# ChessBoard.py by Ben Earle                    #
# Basic pygame board layout for a client.       #
#################################################
import pygame as pg


pg.init()

BLACK = pg.Color('black')
WHITE = pg.Color('white')
COL = [WHITE, BLACK]

screen = pg.display.set_mode((1000, 750))
clock = pg.time.Clock()

tile_size = 75
width, height = 8*tile_size, 8*tile_size
background = pg.Surface((width, height))

for y in range(0, height, tile_size):
    for x in range(0, width, tile_size):
        rect = (x, y, tile_size, tile_size)
        pg.draw.rect(background, COL[(x+y)%2], rect)

game_exit = False

screen.fill((60, 70, 90))
screen.blit(background, (100, 100))
pg.display.flip()
while not game_exit:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			game_exit = True

	clock.tick(30)

pg.quit()