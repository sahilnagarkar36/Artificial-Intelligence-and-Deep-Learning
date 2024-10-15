# -*- coding: utf-8 -*-
"""Min_Max_Algorithm.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v9dKJWNW0wm4FzJt4A_r4bmxLS5fNs_Z
"""

import math

# Constants for players
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = "."

# Function to print the current game board
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Function to evaluate the board and return a score
def evaluate_board(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return 10 if board[i][0] == PLAYER_X else -10
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return 10 if board[0][i] == PLAYER_X else -10

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return 10 if board[0][0] == PLAYER_X else -10
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return 10 if board[0][2] == PLAYER_X else -10

    return 0  # Draw or game still ongoing

# Function to check if the game is over
def is_game_over(board):
    return evaluate_board(board) != 0 or all(cell != EMPTY for row in board for cell in row)

# Minimax function to determine the best move
def minimax(board, depth, is_maximizing):
    score = evaluate_board(board)

    # If the game is over, return the score
    if score == 10 or score == -10:
        return score

    if is_game_over(board):
        return 0  # Draw

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    best_score = max(best_score, minimax(board, depth + 1, False))
                    board[i][j] = EMPTY
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    best_score = min(best_score, minimax(board, depth + 1, True))
                    board[i][j] = EMPTY
        return best_score

# Function to find the best move for the computer
def find_best_move(board):
    best_value = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                move_value = minimax(board, 0, False)
                board[i][j] = EMPTY

                if move_value > best_value:
                    best_move = (i, j)
                    best_value = move_value

    return best_move

# Main game loop
def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe: Player X (you) vs. Player O (computer)")
    print_board(board)

    while True:
        # Player X (Human)
        row = int(input("Enter your move row (0, 1, or 2): "))
        col = int(input("Enter your move column (0, 1, or 2): "))

        if row not in (0, 1, 2) or col not in (0, 1, 2):
            print("Invalid input! Please enter 0, 1, or 2 for both row and column.")
            continue

        if board[row][col] != EMPTY:
            print("Invalid move! Try again.")
            continue

        board[row][col] = PLAYER_X

        if is_game_over(board):
            print_board(board)
            if evaluate_board(board) == 10:
                print("You win!")
            else:
                print("It's a draw!")
            break

        # Player O (Computer)
        print("Computer's turn...")
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = PLAYER_O

        print_board(board)
        if is_game_over(board):
            if evaluate_board(board) == -10:
                print("Computer wins!")
            else:
                print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()