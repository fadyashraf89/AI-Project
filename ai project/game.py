import time
from board import *
from GUI import *

# GAME LINK
# http://kevinshannon.com/connect4/

"""
 the code implements a playable game of Connect Four with a computer player that uses the minimax algorithm to make its 
 moves. The difficulty level of the game can be adjusted by selecting a different search depth for the minimax algorithm.
 The game is played ona GUI created using the GUI.py file, and the board is represented using the board.py file. The GUI
 allows the player to select a column by clicking on it, and the computer player uses the minimax algorithm to determine
 its moves. The game ends when either player wins or the board is full.
"""

# This function is the implementation of the minimax algorithm.
# It takes a board object, depth of the search tree, a boolean maximizing_player flag, and alpha beta values for pruning.
# The function returns the best move (column) and its score.
def minimax(board, depth, maximizing_player, alpha, beta):
    if depth == 0:
        return None, evaluate_board(board)

    if maximizing_player:
        max_value = float('-inf')
        column = None
        for i in range(7):
            if is_valid_move(board, i):
                new_board = make_move(board, i, RED)
                _, value = minimax(new_board, depth - 1, False, alpha, beta)
                if value > max_value:
                    max_value = value
                    column = i
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
        return column, max_value
    else:
        min_value = float('inf')
        column = None
        for i in range(7):
            if is_valid_move(board, i):
                new_board = make_move(board, i, BLUE)
                _, value = minimax(new_board, depth - 1, True, alpha, beta)
                if value < min_value:
                    min_value = value
                    column = i
                beta = min(beta, value)
                if alpha >= beta:
                    break
        return column, min_value

# This function evaluates the score of a given board configuration. It checks all possible winning combinations of four chips in a row, column, or diagonal.
def evaluate_board(board):
    score = 0
    # Check rows
    for i in range(6):
        for j in range(4):
            window = [board[i][j], board[i][j + 1], board[i][j + 2], board[i][j + 3]]
            score += evaluate_window(window)
    # Check columns
    for i in range(3):
        for j in range(7):
            window = [board[i][j], board[i + 1][j], board[i + 2][j], board[i + 3][j]]
            score += evaluate_window(window)
    # Check diagonals
    for i in range(3):
        for j in range(4):
            window = [board[i][j], board[i + 1][j + 1], board[i + 2][j + 2], board[i + 3][j + 3]]
            score += evaluate_window(window)
    for i in range(3, 6):
        for j in range(4):
            window = [board[i][j], board[i - 1][j + 1], board[i - 2][j + 2], board[i - 3][j + 3]]
            score += evaluate_window(window)
    return score


# This function evaluates the score of a given window (4 chips in a row, column, or diagonal).
# It assigns scores to different types of windows based on the number of chips and empty spaces.
def evaluate_window(window):
    score = 0
    red_count = window.count(RED)
    blue_count = window.count(BLUE)
    empty_count = window.count(EMPTY)
    if red_count == 4:
        score += 100
    elif red_count == 3 and empty_count == 1:
        score += 5
    elif red_count == 2 and empty_count == 2:
        score += 2
    if blue_count == 4:
        score -= 100
    elif blue_count == 3 and empty_count == 1:
        score -= 5
    elif blue_count == 2 and empty_count == 2:
        score -= 2
    return score

# This function creates a new board object with a move (chip placement) made by a given player in a given column.
def make_move(board, column, player):
    new_board = [row[:] for row in board]
    for i in range(5, -1, -1):
        if new_board[i][column] == EMPTY:
            new_board[i][column] = player
            break
    return new_board

# This function checks if a given column is a valid move on the current board.
def is_valid_move(board, column):
    return board[0][column] == EMPTY

"""
- In the main function, the code imports the Boardand mygui classes from the board.py and GUI.py files, respectively. 
- It then creates a Board object and waits for 3 seconds to allow the GUI to initialize.
- The code then displays a difficulty selection menu using the select_diff, select_diff2, and select_diff3 functions from
  the GUI. 
- These functions allow the player to select a difficulty level for the computer player by choosing the search depth of 
  the minimax algorithm.
- The while loop in the main function is the main game loop. It first gets the current game grid from the Board object and 
  prints it to the console using the print_grid function.
- The code then calls the minimax function with the current game grid, the selected search depth, and the computer player 
  as the maximizing player. It selects the column returned by the minimax function using the select_column function from 
  the Board class.
- The code then waits for 2 seconds before repeating the loop.
- The game loop continues until the game is over, which is determined by the get_game_grid function from the Board class.
"""
def main():
    board = Board()
    time.sleep(3)
    game_end = False
    gui = mygui()
    num = gui.select_diff()
    num2 = gui.select_diff2()
    num3 = gui.select_diff3()
    if num == 4:
        Depth = num
    if num2 == 5:
        Depth = num2
    if num3 == 6:
        Depth = num3
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        board.print_grid(game_board)

        column, _ = minimax(game_board, Depth, True, float('-inf'), float('inf'))
        board.select_column(column)

        time.sleep(2)


if __name__ == "__main__":
    main()
