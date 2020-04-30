"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    if not terminal(board):
        count_x, count_o = 0, 0
        for row in board:
            count_o += row.count(O)
            count_x += row.count(X)
        if count_x > count_o:
            return 0
        else:
            return X
    else:
        return X


    """
    Returns player who has the next turn on a board.
    """


def actions(board):
    possible_actions = set()

    if not terminal(board):
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    possible_actions.add((i, j))
        return possible_actions

    """
    Returns set of all possible actions (i, j) available on the board.
    """



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    boardcopy = copy.deepcopy(board)
    try:
        if boardcopy[action[0]][action[1]] != EMPTY:
            raise IndexError
        else:
            boardcopy[action[0]][action[1]] = player(boardcopy)
            return boardcopy
    except IndexError:
        print('Spot already occupied')

`
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    columns = []

    # Checks rows
    for row in board:
        xcounter = row.count(X)
        ocounter = row.count(O)
        if xcounter == 3:
            return X
        if ocounter == 3:
            return O

    # Checks columns
    for j in range(len(board)):
        column = [row[j] for row in board]
        columns.append(column)

    for j in columns:
        xcounter = j.count(X)
        ocounter = j.count(O)
        if xcounter == 3:
            return X
        if ocounter == 3:
            return O

    # Checks diagonals
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    if board[0][2] == X and board [1][1] == X and board[2][0] == X:
        return X


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_counter = 0
    for row in board:
        empty_counter += row.count(EMPTY)
    if empty_counter == 0:
        return True
    elif winner(board) is not None:
        return True
    else:
        return False


def utility(board):

    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    empty_counter = 0
    for row in board:
        empty_counter += row.count(EMPTY)
    if empty_counter == 0:
        return True
    elif winner(board) is not None:
        return True
    else:
        return False

def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for a in actions(board):
        v = min(v, max_value(result(board, a)))
    return v

def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for a in actions(board):
        v = max(v, min_value(result(board, a)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)

    if current_player ==0:
        v = math.inf
        for action in actions(board):
            move = max_value(result(board, action))
            if move < v:
                v = move
                best_move = action
    else:
        v = -math.inf
        for action in actions(board):
            move = min_value(result(board, action))
            if move > v:
                v = move
                best_move = action
    return best_move
