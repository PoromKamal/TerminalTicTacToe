from typing import List

gameBoard = [["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]]
tutorialBoard = [["TL","TM","TR"],
            ["ML","MM","MR"],
            ["BL","BM","BR"]]
def drawBoard(board):
    print("________")
    for i in range(len(board)):
        for j in range(len(board)):
            if j == 2:
                print(board[i][j])
            else:
                print(board[i][j] +" "+ "|", end = "")
    print("--------")
def updateBoard(player: str, move: str):
    """
    Update the game board given player, and space which contains an x and y coordinate.
    """
    moveY = {"T": 0, "M": 1, "B": 2}
    moveX = {"L": 0, "M": 1, "R": 2}  
    gameBoard[moveY[move[0]]][moveX[move[1]]] = player

def validMove(move):
    moveY = {"T": 0, "M": 1, "B": 2}
    moveX = {"L": 0, "M": 1, "R": 2}  
    validCommands = ["TL", "TM", "TR", "ML", "MM", "MR", "BL", "BM", "BR"]
    if move in validCommands and gameBoard[moveY[move[0]]][moveX[move[1]]] == "-":
        return True
    return False

def checkWinner(board):
    startPiece = board[0][0]
    #Check diagonals
        #Top left to bottom right
    if(startPiece == board[1][1] and startPiece== board[2][2] and startPiece != "-"):
        return startPiece
        #Top right to bottom left
    startPiece = board[0][2]
    if(startPiece == board[1][1] and startPiece==board[2][0] and startPiece != "-"):
        return startPiece
    #Check horizontals
    for i in range(3):
        startPiece = board[i][0]
        if(startPiece == board[i][1] and startPiece == board[i][2] and startPiece != "-"):
            return startPiece
    #Check Verticals
    for i in range(3):
        startPiece = board[0][i]
        if(startPiece == board[1][i] and startPiece == board[2][i]and startPiece != "-"):
            return startPiece
    return "N"

def resetBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = "-"

def main():
    print("Welcome to terminal only tictactoe! This is a two player game!")
    print("Here is how the commands on board will work:")
    drawBoard(tutorialBoard)
    print("----------------------------------------------------------------")
    player = "X"
    winner = "N"
    moveCount = 0
    ex = "Y"
    while(ex == 'Y'):
        drawBoard(gameBoard)
        if winner == "N" and moveCount != 9:
            print("Player " + player + "'s move! ")
            move = input()
            if(validMove(move)):
                updateBoard(player, move)
                moveCount+=1
                winner = checkWinner(gameBoard)
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("Invalid move, Try again.")
        else:
            if winner == "N":
                print("Tie!")
            else:
                print("The winner is "+ winner + "!")
            print("If you would like to play again enter Y, else enter N:")
            ex = input()
            if ex == "Y":
                #reset variables:
                resetBoard(gameBoard)
                winner = "N"
                moveCount = 0
                player = "X"
def test_branch():
    print("This is the A.I. Integration Test Branch")


if __name__ == "__main__":
     main()
    