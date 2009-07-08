#!/usr/bin/env python

def playgame():
    """Asks user what size board they want to play on, creates a 
       board, and runs the game."""

    size = int(raw_input("Enter a game size: "))
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(True)
        board.append(row)
    done = False
    while not done:
        printboard(board)
        input = raw_input("Enter a row and column: ").split(' ')
        row = int(input[0])-1
        col = int(input[1])-1
        board = move(board,row,col)
        done = checkboard(board)
    input = raw_input("You win! Would you like to play again: ")
    if input.lower().strip() == "yes":
        game()
    else:
        print "Thanks for playing!"

def checkboard(board):
    """Checks the board to see whether or not the game
       is finished."""

    for row in board:
        for state in row:
            if state:
                return False
    return True

def printboard(board):
    """Prints out the game board where an 'x' represents 
       that there is a light on at that location and a '.'
       represents that there is a light off at that location."""

    size = len(board)
    print " ",
    for i in range(size):
        print (i+1),
    print ''
    for i,row in enumerate(board):
        print (i+1),
        for state in row:
            if state:
                print 'x', 
            else:
                print '.',
        print ''

def switch(board, row, col):
    """Toggles a light on or off at the given location."""

    board[row][col] = not board[row][col]
    return board

def move(board, row, col):
    """Toggles all thew lights that are affected by the 
       players movement to the given location."""

    size = len(board)
    board[row][col] = not board[row][col]
    myboard = board
    if row - 1 >= 0:
        myboard = switch(myboard,row-1,col)
    if row + 1 < size:
        myboard = switch(myboard,row+1,col)
    if col - 1 >= 0:
        myboard = switch(myboard,row,col-1)
    if col + 1 < size:
        myboard = switch(myboard,row,col+1)
    return myboard

if __name__ == "__main__":
    playgame()
