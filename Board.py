from Direction import *


class Board:
    board = []
    beadsPlayed = 0
    row = 0
    column = 0
    color = ''
    otherColor = ''

    def __init__(self):
        for row in range(19):
            self.board.append([])
            for column in range(19):
                self.board[row].append('.')
        print(self.board)

    def play(self, row, column, color):
        self.board[row][column] = color[0]
        self.beadsPlayed += 1
        self.row = row
        self.column = column
        self.color = color[0]
        if self.color == 'B':
            self.otherColor = 'R'
        else:
            self.otherColor = 'B'
        self.print()

    def get(self, row, column):
        return self.board[row][column]

    def getBeadsPlayed(self):
        return self.beadsPlayed

    def analyzeJump(self, direction):
        if self.bead(direction, 1) != self.otherColor:
            return False
        if self.bead(direction, 2) != self.otherColor:
            return False
        if self.bead(direction, 3) != self.color:
            return False
        return True

    def bead(self, direction, offset):
        if direction == Direction.NORTH:
            if self.row - offset < 0:
                return -1
            return self.board[self.row - offset][self.column]
        if direction == Direction.NORTHEAST:
            if self.row - offset < 0:
                return -1
            if self.column + offset > 19:
                return -1
            return self.board[self.row - offset][self.column + offset]
        if direction == Direction.EAST:
            if self.column + offset > 19:
                return -1
            return self.board[self.row][self.column + offset]
        if direction == Direction.SOUTHEAST:
            if self.row + offset > 19:
                return -1
            if self.column + offset > 19:
                return -1
            return self.board[self.row + offset][self.column + offset]
        if direction == Direction.SOUTH:
            if self.row + offset > 19:
                return -1
            return self.board[self.row + offset][self.column]
        if direction == Direction.SOUTHWEST:
            if self.row + offset > 19:
                return -1
            if self.column - offset < 0:
                return -1
            return self.board[self.row + offset][self.column - offset]
        if direction == Direction.WEST:
            if self.column - offset < 0:
                return -1
            return self.board[self.row][self.column - offset]
        if direction == Direction.NORTHWEST:
            if self.row - offset < 0:
                return -1
            if self.column - offset < 0:
                return -1
            return self.board[self.row - offset][self.column - offset]

    def print(self):
        print()
        for row in range(19):
            for column in range(19):
                print(self.board[row][column], end=' ')
            print()
