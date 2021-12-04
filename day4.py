#!/usr/bin/env python3

class BingoBoard:
    MARK = -1 # can be any non-Bingo number

    def __init__(self):
        self.board = []
        self.bingo = False
        self.score = 0

    def print(self):
        for row in self.board:
            for col in row:
                print(f"{col:2} ", end='')
            print()

    def add_row(self, row):
        self.board.append(row)

    def check(self, number):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == number:
                    # number found, mark it
                    self.board[row][col] = self.MARK
                    # row or column bingo?
                    if self.board[row].count(self.MARK) == len(self.board[row]) or \
                        [self.board[r][col] for r in range(len(self.board))].count(self.MARK) == len(self.board):
                        self.bingo = True
                        self.score = number * self.calc_sum()
                        return True
                    else:
                        return False
        # number not on the board
        return False

    def calc_sum(self):
        total = 0
        for row in self.board:
            for c in row:
                if c != self.MARK:
                    total += c
        return total


# Main
# work with any rectangular board
if __name__ == "__main__":
    boards = []
    with open("day4_input") as fh:
        line = fh.readline().strip()
        numbers = [int(x) for x in line.split(',')]

        line = fh.readline()
        while line != '':
            line = line.strip()
            if not line:
                line = fh.readline()
                continue
            boards.append(BingoBoard())
            while line:
                bingo_row = [int(x) for x in line.split()]
                boards[-1].add_row(bingo_row)
                line = fh.readline().strip()
            line = fh.readline()

    winners = []
    for num in numbers:
        # only check boards that have not been solved yet
        for board in filter(lambda x: not x.bingo, boards):
            if board.check(num):
                winners.append(board)

    print(f"First winning score (index = {boards.index(winners[0])}): {winners[0].score}")
    winners[0].print()
    print(f"Last winning score (index = {boards.index(winners[-1])}): {winners[-1].score}")
    winners[-1].print()