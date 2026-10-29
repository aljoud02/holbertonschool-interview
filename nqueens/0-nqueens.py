#!/usr/bin/python3
"""
Module that solves the N-queens puzzle using backtracking algorithm.
"""
import sys


def print_usage_and_exit(message, status=1):
    """
    Prints the error message to standard output and terminates the program with a given status code.
    """
    print(message)
    sys.exit(status)


def init_arguments():
    """
    Validates command-line arguments and returns the integer value of N.
    """
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if n < 4:
        print_usage_and_exit("N must be at least 4")

    return n


def is_safe(row, col, board):
    """
    Evaluates whether a queen can be securely positioned at the specified board[row] = col coordinate.
    """
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(row, n, board):
    """
    Executes a recursive backtracking search to find and display all valid positions for the N-queens.
    """
    if row == n:
        solution = [[i, board[i]] for i in range(n)]
        print(solution)
        return

    for col in range(n):
        if is_safe(row, col, board):
            board[row] = col
            solve_nqueens(row + 1, n, board)


if __name__ == "__main__":
    n_queens = init_arguments()
    queen_board = [0] * n_queens
    solve_nqueens(0, n_queens, queen_board)
