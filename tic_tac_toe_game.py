def printboard(xstate, ostate):
    #Functions to print the current state of the board
    board = []
    for i in range(9):
        if xstate[i]:
            board.append('X')
        elif ostate[i]:
            board.append('O')
        else:
            board.append('-')


    print(f"{board[0]} | {board[1]} | {board[2]} ")
    print(f"--|---|---")
    print(f"{board[3]} | {board[4]} | {board[5]} ")
    print(f"--|---|---")
    print(f"{board[6]} | {board[7]} | {board[8]} ") 

def check_wins(xstate, ostate):
    #Function to check if ther's a winner
    win_conditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], #Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], #Columns
    [0, 4, 8], [2, 4, 6]             #Diagonals
    ]

    for condition in win_conditions:
        if xstate[condition[0]] and xstate[condition[1]] and xstate[condition[2]]:
            print("CONGRATS! X YOU WIN THE MATCH!")
            return 1
        if ostate[condition[0]] and ostate[condition[1]] and ostate[condition[2]]:
            print("CONGRATS! O YOU WIN THE MATCH!")
            return 0
    return -1

if __name__ == "__main__":
    xstate = [0] * 9 #state of the board of X
    ostate = [0] * 9 #state of the board O
    turn = 1 #1 for X's turn and 0 for O's turn
    print("Welcome to Tic Tac Toe Game")

    while True:
        printboard(xstate, ostate)

        if (turn == 1):
            print("X's Turn")
            move = int(input("Enter your move (0-8): "))
            if 0 <= move < 9 and xstate[move] == 0 and ostate[move] == 0:
                xstate[move] = 1
        else:
            print("O's Turn")
            move = int(input("Enter your move (0-8): "))
            if 0 <= move < 9 and xstate[move] == 0 and ostate[move] == 0:
                ostate[move] = 1
            else:
                print("Invalid move, try again")
                continue
        
        winner = check_wins(xstate, ostate)
        if winner != -1:
            printboard(xstate, ostate)
            print("Match Over!")
            break
        
        turn = 1 - turn #switch turns

