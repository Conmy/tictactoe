#!/usr/bin/python

#******************************************************************************
#| Title: Tic Tac Toe
#| Description: Text based game of tic tac toe.
#| Author: David Conmy
#|-----------------------------------------------------------------------------
#| EditNo.  | Date      | Comments
#|----------|-----------|------------------------------------------------------
#| 001      | 21/05/2013| David Conmy
#|          |           | 1. Initial Version
#|----------|-----------|------------------------------------------------------
#******************************************************************************
        
import random

def getInitialBoard():
    board = [" "] * 10
    return board

# Toggle the current letter (either X or O)
def toggleLetter():
    global Letter
    if Letter == 'X':
        Letter = 'O'
    else:
        Letter = 'X'

# Toggle the player's turn.
def togglePlayersTurn():
    global PlayersTurn
    PlayersTurn = not PlayersTurn

# Is the move valid?
def validateMove(board, position):
    return board[position] == " "

# Is the board full?
def checkIfFull(board):
    for i in board:
        if i == " ":
            return False
    print("Board is full. DRAW GAME")
    return True

# Sets the move on the board in the specified position.
def setMove(board, position, letter):
    board[position] = letter

# Returns True if the specified letter is a winner.
def isWinner(bo, le):
    # returns true if the letter has lined up three in a row.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # middle -> that way
    (bo[1] == le and bo[2] == le and bo[3] == le) or # bottom
    (bo[1] == le and bo[4] == le and bo[7] == le) or # left
    (bo[2] == le and bo[5] == le and bo[8] == le) or # middle upways
    (bo[3] == le and bo[6] == le and bo[9] == le) or # right
    (bo[1] == le and bo[5] == le and bo[9] == le) or # diag upways /
    (bo[7] == le and bo[5] == le and bo[3] == le))   # diag downwards \

# True if there is a winner.
def checkForWinner(board):
    if isWinner(board, "X"):
        print("X WINS")
        return True
    elif isWinner(board, "O"):
        print("O WINS")
        return True
    else:
        return False

# Print the board to the screen.
def printBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

# Get the next player move.
def getPlayerMove():
    return int(input("Enter your move: "))

# Get the computer's move.
def generateComputerMove():
    return random.randrange(1, 10)

# Handles making a move on the board.
def MakeMove(board):
    global PlayersTurn
    global Letter
    
    if PlayersTurn:
        print("Player's move.")
        position = getPlayerMove()
        while validateMove(board, position) == False:
            position = getPlayerMove()
        setMove(board, position, Letter)
    else:
        print("Computer's move:")
        position = generateComputerMove()
        while validateMove(board, position) == False:
            position = generateComputerMove()
        setMove(board, position, Letter)

# Let the user choose which character he is (X or O)
def setPlayerCharacter():
    global PlayersTurn
    global Letter
    result = str(input("Are you (X) or (O): "))
    result = result.upper()
    while result != 'X' and result != 'O':
        result = str(input("Are you (X) or (O): "))
        result = result.upper()
    if result == 'X':
        PlayersTurn = False
        Letter = 'O'
    else:
        PlayersTurn = True
        Letter = 'O'

# Print help to the user to know how to play.
def printHelp():
    print('7|8|9')
    print('-+-+-')
    print('4|5|6')
    print('-+-+-')
    print('1|2|3')
    print('Number corresponds to position.')

# =============================================================================
# Game Start
# =============================================================================

# The current letter of the game.
Letter = "O"
# If it is the player's turn or not.
PlayersTurn = True

# Print game header.
print ("===========")
print ("TIC TAC TOE")
print ("===========")

printHelp()

result = str(input("Press 5 for new game: "))

while result == '5':
    # Set up board.
    Board = getInitialBoard()
    # Choose which character to be (X or O) 
    setPlayerCharacter()
    
    while (not checkIfFull(Board) and not checkForWinner(Board)):
        # Change whose turn it is.
        togglePlayersTurn()
        toggleLetter()

        # Make a move on the board.
        MakeMove(Board)
        # Print the board.
        printBoard(Board)

    # Check if the user wants to play again.
    result = str(input("Press 5 for new game: "))



