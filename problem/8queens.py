import math
queens = 0
occupiedSquares = []
blacklistedSquares = []

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
        #other diagonal
        for iter in list(range(-7, 15)):
            if 0 < (8 * (row - iter) + (col + iter)) < 64:
                illegals.append(8 * (row - iter) + (col + iter))
        #blacklisted
        for iter in blacklistedSquares:
            illegals.append(iter)
    return illegals

def determineLegality(position, board):
    illegalSquares = getIllegalSquares(occupiedSquares)
    if illegalSquares.count(position) == 0:
        return True
    return False

def findEmptyPlace(position, board):
    for pos in list(range(position + 1, 64)):
        col = pos%8
        row = math.floor(pos/8)
        if board[row][col] == 0:
            return (True, pos)
    return (False, position)

def showBoard(board):
    for i in list(range(0,8)):
            print("%d %d %d %d %d %d %d %d\n" % (board[i][0], board[i][1], board[i][2], board[i][3], board[i][4], board[i][5], board[i][6], board[i][7]))

def putQueen(square, board):
    legal = determineLegality(square, board)
    if legal == False:
        print("square %d is illegal!" % square)
        return (False, board)
    print("putting queen at square %d because it is legal" % square)
    col = square%8
    row = math.floor(square/8)
    board[row][col] = 1
    occupiedSquares.append(square)
    return (True, board)

def popQueen(square, board):
    print("removing queen from square %d" % square)
    col = square%8
    row = math.floor(square/8)
    board[row][col] = 0
    showBoard(board)
    return board

squares = [[0 for x in range(8)] for x in range(8)]
print("initial board:\n")
showBoard(squares)
currentPos = -1
nextEmptySquare = 0
while len(occupiedSquares) < 8:
    print("finding next empty square...")
    (success, nextEmptySquare) = findEmptyPlace(currentPos, squares)
    if success == False:
        print("out of empty squares!\nbacktracking...")
        blacklistedSquares.append(occupiedSquares.pop(len(occupiedSquares) - 1))
        if len(occupiedSquares) == 0:
            currentPos = -1
        else:
            currentPos = occupiedSquares[len(occupiedSquares) - 1]
        squares = popQueen(blacklistedSquares[len(blacklistedSquares) - 1], squares)
        continue
    print("found square number %d..." % nextEmptySquare)
    (success, squares) = putQueen(nextEmptySquare, squares)
    if success == True:
        currentPos = nextEmptySquare
        showBoard(squares)
        continue
    print("illegal square so moving on")
    currentPos = nextEmptySquare
    continue