import random

class Cell:
    def __init__(self, value = "", fixed = False):
        self.value = value
        self.fixed = fixed

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)

class Board:
    board = []
    def __init__(self):
        for row in range(9):
            self.board.append([])
            for column in range(9):
                self.board[row].append(Cell('-', False))

    def emptyBoard(self):
        '''Board -> None
        This method resets the values in a board'''
        for i in self.board:
            for j in self.board[i]:
                self.board[i][j].value = '-'

    def displayBoard(self):
        '''Board -> None
        This method displays the contents of the board'''
        print("   ", end="")
        col = 0
        while col < len(self.board):
            if(col == 3 or col == 6):
                print('|', col, end = "  ")
            else:
                print(col, end="  ")
            col += 1
        print()
        row = 0
        while row < len(self.board):
            if(row == 3 or row == 6):
                print("---------------------------------")
            print(row, end="")
            col = 0
            while col < len(self.board[row]):
                if(col == 3 or col == 6):
                    print("  |", self.board[row][col], end="")
                else:
                    print(" ", self.board[row][col], end="")
                col += 1
            print()
            row += 1


    def checkBoard(self):
        '''Board -> Boolean'''

    def generateBoard(self, difficulty = 1):
        '''Board -> None'''
        


    def addValue(self, row, column, value):
        '''Board, int, int, int -> Boolean'''

    def removeValue(self, row, column):
        '''Board, int, int -> Boolean'''

    def isComplete(self):
        '''Board -> Boolean'''

    def solveBackTracking(self):
        '''Board -> None'''

    def solveStochasticSearch(self):
        '''Board -> None'''

    def solveConstraint(self):
        '''Board -> None'''

    def solveExactCover(self):
        '''Board -> None'''