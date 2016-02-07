import math
import os
import time
allReps = 0
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
            if ((0 < (8 * (row + iter) + (col + iter)) < 64) and (((row + iter)*(col + iter)) >= 0)):
                illegals.append(8 * (row + iter) + (col + iter))
        #other diagonal
        for iter in list(range(-7, 15)):
            if ((0 < (8 * (row - iter) + (col + iter)) < 64) and (((row - iter)*(col + iter)) >= 0)):
                illegals.append(8 * (row - iter) + (col + iter))
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
    os.system('cls')
    for i in list(range(0,8)):        
        print("%d %d %d %d %d %d %d %d\n" % (board[i][0], board[i][1], board[i][2], board[i][3], board[i][4], board[i][5], board[i][6], board[i][7]))

def putQueen(square, board):
    legal = determineLegality(square, board)
    if legal == False:
        #print("square %d is illegal!" % square)
        return (False, board)
    #print("putting queen at square %d because it is legal" % square)
    col = square%8
    row = math.floor(square/8)
    board[row][col] = 1
    occupiedSquares.append(square)
    return (True, board)

def popQueen(square, board):
    #print("removing queen from square %d" % square)
    col = square%8
    row = math.floor(square/8)
    board[row][col] = 0
    return board

squares = [[0 for x in range(8)] for x in range(8)]
#print("initial board:\n")
currentPos = -1
nextEmptySquare = 0
start = time.time()
while len(occupiedSquares) < 8:
    allReps = allReps + 1
    #if allReps%10000 == 0:
    #    showBoard(squares)
    #print("finding next empty square...")
    (success, nextEmptySquare) = findEmptyPlace(currentPos, squares)
    if success == False:
        #print("out of empty squares!\nbacktracking...")
        currentPos = occupiedSquares.pop()
        squares = popQueen(currentPos, squares)
        continue
    #print("found square number %d..." % nextEmptySquare)
    (success, squares) = putQueen(nextEmptySquare, squares)
    if success == True:
        currentPos = nextEmptySquare
        continue
    #print("illegal square so moving on")
    currentPos = nextEmptySquare
    continue
stop = time.time()
showBoard(squares)
print(stop - start)
print(allReps)