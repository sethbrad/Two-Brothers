import array

""" # returns something
def add(x, y):
    return x + y

# does not return (void)
def addNoReturn(x, y):
    print(x + y)"""

board = [[0,0,0], [0,0,0], [0,0,0]]

# 6 is player 1, 7 is player 2
# Tic Tac Toe but with 6's and 7's
# 0 is blank, 6 is x, 7 is o

def printBoard():
    print("Current board: ")
    print(board[0])
    print(board[1])
    print(board[2])
    print()

def playerMove(row, column, symbol):
    # check if the input is valid
    # then check if the space is blank

    # assign new value
    board[row][column] = symbol

printBoard()
playerMove(0,0,6)
printBoard()

playerMove(1,1,7)
printBoard()