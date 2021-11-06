import time
import logging

class NonogramSolver(object):
    def __init__(self, board_size, hints):
        self.board_size = board_size
        self.board = [ [0] * board_size ] * board_size
        self.hints = hints

    def generate_board(self, board):
        my_list = [int(char) for char in [row for row in board]]
        return [my_list[i * self.board_size:(i + 1) * self.board_size] for i in range((len(my_list) + self.board_size - 1) // self.board_size )]

    def get_column(self, board, col):
        return [row[col] for row in board]

    def check_rows(self, potential_board):
        # For each row in the board
        for i in range(0, len(potential_board)):
            # if the number in the row is larger than the size of the hint for the row
            if sum(potential_board[i]) > self.hints[0][i]:
                return False
        return True

    def get_column(self, potential_board, column):
        generated_column = [row[column] for row in potential_board if len(row) > column]
        return generated_column
    
    def check_columns(self, potential_board):
        for i in range(0, len(potential_board[0])):
            if sum(self.get_column(potential_board, i)) > self.hints[1][i]:
                return False
        return True

    def check(self, potential_solve):
        potential_board = self.generate_board(potential_solve)
        # If any of the rows are invalid, return false.
        if not self.check_rows(potential_board):
            return False
        elif not self.check_columns(potential_board):
            return False
        return True

    def solve(self):
        self.stack = []
        self.stack.append("0")
        self.stack.append("1")
        while self.stack:
            current = self.stack.pop()
            # If the current board is invalid, don't add to the stack because this is invalid
            if not self.check(current):
                continue
            if len(current) < self.board_size*self.board_size:
                self.stack.append(current + "0")
                self.stack.append(current + "1")
            if self.generate_board(current) == self.generate_board("0010001110111110111000100"):
                logging.info("Solved")
                break


logging.basAicConfig(filename='nonogram.log', encoding='utf-8', level=logging.INFO)

nono = NonogramSolver(board_size=5, hints=[[1,3,5,3,1],[1,3,5,3,1]])

start = time.time()
nono.solve()
end = time.time()

logging.info(f"Algorithm took: {end - start} seconds!")
