import time


class NonogramSolver(object):


    def __init__(self, board_size, hints):
        self.board_size = board_size
        self.board = [ [0] * board_size ] * board_size
        self.hints = hints


    def generate_board(self, board):
        my_list = [int(char) for char in [row for row in board]]
        return [my_list[i * self.board_size:(i + 1) * self.board_size] for i in range((len(my_list) + self.board_size - 1) // self.board_size )]


    def check(self, potential_solve):
        potential_board = self.generate_board(potential_solve)
        if potential_board == self.generate_board("0010001110111110111000100"):
            print("Solved")
            return True
        return False


    def solve(self):
        self.stack = []
        self.stack.append("0")
        self.stack.append("1")
        while self.stack:
            current = self.stack.pop()
            if len(current) == self.board_size * self.board_size:
                if self.check(current):
                    print("Success")
                    solved_board = self.generate_board(current)
                    for row in solved_board:
                        print(row)
                    break
            else:
                self.stack.append(current + "0")
                self.stack.append(current + "1")


nono = NonogramSolver(board_size=5, hints=[[1,3,5,3,1],[1,3,5,3,1]])

start = time.time()
nono.solve()
end = time.time()

print(end - start)
