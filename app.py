import time

board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

solved_board = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0]
]

hints = [
    [1, 3, 5, 3, 1],
    [1, 3, 5, 3, 1]
]


class NonogramSolver(object):
    def __init__(self, board_size, hints):
        board = [[0*board_size]*board_size]


def generate_board(board):
    return [
        [int(char) for char in board[0:5]],
        [int(char) for char in board[5:10]],
        [int(char) for char in board[10:15]],
        [int(char) for char in board[15:20]],
        [int(char) for char in board[20:25]],
    ]


def check(potential_solve):
    potential_board = generate_board(potential_solve)
    if potential_board != solved_board:
        return False
    return True


def solve():
    stack = []
    stack.append("0")
    stack.append("1")
    while stack:
        current = stack.pop()
        if len(current) == 25:
            if check(current):
                print("Success")
                solved_board = generate_board(current)
                for row in solved_board:
                    print(row)
                break
        else:
            stack.append(current + "0")
            stack.append(current + "1")

start = time.time()
solve()
end = time.time()
print(end - start)
