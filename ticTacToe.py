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
    if(row > 2 or column > 2):
        print("Error: index out of bounds!")
        return

    # then check if the space is blank
    if(board[row][column] != 0):
        print("Error: that space is taken!")
        return

    # assign new value
    board[row][column] = symbol

# user inputs location
def userInput():
    # check for correct format

    # row,space,column
    location = input("Enter your move: ")
    arr = location.split(',')
    row = int(arr[0])
    column = int(arr[1])
    symbol = int(arr[2])
    
    playerMove(row, column, symbol)
    printBoard()

# # # # THE GAME LOOP
print("Input format: row,column,your number")
while(True):
    try:
        userInput()
        
        # check if someone won?

    except(KeyboardInterrupt):
        print("Game aborted!")
        break
