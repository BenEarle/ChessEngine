#################################################
# ChessBoard.py by Ben Earle                    #
# C:/Ben/ChessEngine/ChessBoard.py              #


grid = setupBoard()
printBoardWhite(grid)
grid = move(grid, "E2-E4")
printBoardWhite(grid)
grid = move(grid, "E7-E5")
printBoardWhite(grid)