import random
from view import *

def winner_check(board):
    winner = ""

    if board[0] == board[1] == board[2]: winner = board[0]
    elif board[3] == board[4] == board[5]: winner = board[3]
    elif board[6] == board[7] == board[8]: winner = board[6]

    if board[0] == board[3] == board[6]: winner = board[0]
    elif board[1] == board[4] == board[7]: winner = board[1]
    elif board[2] == board[5] == board[8]: winner = board[2]

    if board[0] == board[4] == board[8]: winner = board[0]
    elif board[2] == board[4] == board[6]: winner = board[2]
    return winner

def man_turn(board, choose: int):
    clean_list = ([x for x in board if x.isdigit()])
    if choose not in clean_list:
        return board
    for num, x in enumerate(board):
        if x == choose:
            board[num] = "O"
    return board

def bot_turn(board):
    clean_list = ([x for x in board if x.isdigit()])
    choose = random.choice(list(map(int, clean_list)))
    for num, x in enumerate(board):
        board[choose-1] = "X"
    return board


def game():
    board = \
    [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9"
    ]
    return board



