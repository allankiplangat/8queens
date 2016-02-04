import math
queens = 0
occupiedSquares = []
def getIllegalSquares(occu):
    illegals = []
    for place in occu:
        row = math.floor(place/8)
        col = place%8
        #vertical and horizontal illegals
        for iter in list(range(0, 8)):
            illegals.append(8*iter + col)
            illegals.append(8*row + iter)
        #diagonal illegals
        for iter in list(range(-7, 15)):
            if 0 < (8 * (row + iter) + (col + iter)) < 64:
                illegals.append(8 * (row + iter) + (col + iter))
    return illegals
def determineLegality(position, board):
    #how to do this?
    illegalSquares = getIllegalSquares(occupiedSquares)
    if illegalSquares.count(position) == 0:
        return True
    return False
def findEmptyPlace(position, board):
    for pos in list(range(position + 1, 64)):
        col = pos%8
        row = math.floor(pos/8)
        if board[row][col] == 0:
            return (pos, board)
    return (False, board)
def showBoard(board):
    for i in list(range(0,8)):
            print("%d %d %d %d %d %d %d %d\n" % (board[i][0], board[i][1], board[i][2], board[i][3], board[i][4], board[i][5], board[i][6], board[i][7]))
def putQueen(queens, board):
    print("finding first legal position, and putting queen there.")
    queens = queens + 1
    if queens <= 8:
        position = 0
        #find first empty space
        while True:
            (position, board) = findEmptyPlace(position, board)
            if position == False:
                break
            legality = determineLegality(position, board)
            if legality == True:
                col = position%8
                row = math.floor(position/8)
                board[row][col] = 1
                occupiedSquares.append(position)
                return (queens, board)
    return (False, board)

squares = [[0 for x in range(8)] for x in range(8)]
print("initial board:\n")
showBoard(squares)
while True:
    print("press enter to add queen")
    #input()
    if queens == 0:
        squares[0][0] = 1
        occupiedSquares.append(0)
        showBoard(squares)
        queens = 1
        continue
    (trial, squares) = putQueen(queens, squares)
    if trial == False:
        showBoard(squares)
        print("end")
        break
    queens = trial
    showBoard(squares)