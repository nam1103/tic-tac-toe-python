import os
import time

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

current_turn = "x"
has_won = False

def check_winner() -> bool:
    # check diagonally
    if board[0][0] == board[1][1] == board[2][2]:
        return True

    if board[0][2] == board[1][1] == board[2][0]:
        return True

    # check horizontally
    for rowindex in range(len(board) - 1):
        if board[rowindex][0] == board[rowindex][1] == board[rowindex][2]:
            return True
    
    # check vertically
    for colindex in range(len(board) - 1):
        if board[0][colindex] == board[1][colindex] == board[2][colindex]:
            return True

    return False

def print_board() -> None:
    for row in board:
        for node in row:
            print(node, end=",")
        print()

while True:
    os.system("clear")
    print_board()

    print("----------------------")
    print(f"It is {current_turn} to move!")
    user_input = input("Enter coordinate. \n")

    if user_input not in ["1","2","3","4","5","6","7","8","9"]:
        continue

    coord = int(user_input)

    row = (coord - 1) // 3
    col = (coord - 1) % 3

    if board[row][col] == "x" or board[row][col] == "o":
        continue

    board[row][col] = current_turn

    has_won = check_winner()

    if has_won:
        os.system("clear")
        print_board()
        print("----------------------")
        print(f"{current_turn} has won")
        break

    if current_turn == "x":
        current_turn = "o"
    else:
        current_turn = "x"

    time.sleep(1)


print("Program ended")


