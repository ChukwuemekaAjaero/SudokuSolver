import random

class Cell:
    def __init__(self, value = "", fixed = False):
        self.value = value
        self.fixed = fixed

    def __repr__(self):
        return str(self.value)

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
        This method sets all the values on the board to null'''
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.board[i][j].value = '-'

    def resetBoard(self):
        '''Board -> None
        This method erases all the user inputs from the
        board'''

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
        '''Board -> Boolean
        This method checks if all the values in the board meet
        the constraints set by the game of Sudoku'''
        if(self.isComplete()):
            print()

    def checkRow(self, row):
        '''Board, int -> Boolean
        This method checks if the all the values in a
        given row meet all the constraints set by the
        game of Sudoku'''

        c1, c2, c3, c4, c5, c6, c7, c8, c9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
        for i in self.board[row]:
            if i.value == 1: c1 += 1
            if i.value == 2: c2 += 1
            if i.value == 3: c3 += 1
            if i.value == 4: c4 += 1
            if i.value == 5: c5 += 1
            if i.value == 6: c6 += 1
            if i.value == 7: c7 += 1
            if i.value == 8: c8 += 1
            if i.value == 9: c9 += 1

        return c1 < 2 and c2 < 2 and c3 < 2 and c4 < 2 and c5 < 2 and c6 < 2 and c7 < 2 and c8 < 2 and c9 < 2

    def checkColumn(self, column):
        '''Board, int -> Boolean
        This method checks if the all the values in a
        given column meet all the constraints set by the
        game of Sudoku'''

        c1, c2, c3, c4, c5, c6, c7, c8, c9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
        for i in range(len(self.board)):
            if self.board[i][column].value == 1: c1 +=1
            elif self.board[i][column].value == 2: c2 += 1
            elif self.board[i][column].value == 3: c3 += 1
            elif self.board[i][column].value == 4: c4 += 1
            elif self.board[i][column].value == 5: c5 += 1
            elif self.board[i][column].value == 6: c6 += 1
            elif self.board[i][column].value == 7: c7 += 1
            elif self.board[i][column].value == 8: c8 += 1
            elif self.board[i][column].value == 9: c9 += 1

        return c1 < 2 and c2 < 2 and c3 < 2 and c4 < 2 and c5 < 2 and c6 < 2 and c7 < 2 and c8 < 2 and c9 < 2

    def checkSquare(self, row, column):
        '''Board, int, int -> Boolean
        This method checks if the all the values in a
        values square meet all the constraints set by
        the game of Sudoku'''

        c1, c2, c3, c4, c5, c6, c7, c8, c9, rowStart, rowStop, colStart, colStop = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        if row <= 2:
            if column <= 2:
                rowStop, colStop = 2, 2
            elif column <= 5:
                rowStop, colStart, colStop = 2, 3, 5
            else:
                rowStop, colStart, colStop = 2, 6, 8
        elif row <= 5:
            if column <= 2:
                rowStart, rowStop, colStop = 3, 5, 2
            elif column <= 5:
                rowStart, rowStop, colStart, colStop = 3, 5, 3, 5
            else:
                rowStart, rowStop, colStart, colStop = 3, 5, 6, 8
        else:
            if column <= 2:
                rowStart, rowStop, colStop = 6, 8, 2
            elif column <= 5:
                rowStart, rowStop, colStart, colStop = 6, 8, 3, 5
            else:
                rowStart, rowStop, colStart, colStop= 6, 8, 6, 8

        for i in range(rowStart, rowStop+1):
            for j in range(colStart, colStop+1):
                if self.board[i][j].value == 1: c1 += 1
                elif self.board[i][j].value == 2: c2 += 1
                elif self.board[i][j].value == 3: c3 += 1
                elif self.board[i][j].value == 4: c4 += 1
                elif self.board[i][j].value == 5: c5 += 1
                elif self.board[i][j].value == 6: c6 += 1
                elif self.board[i][j].value == 7: c7 += 1
                elif self.board[i][j].value == 8: c8 += 1
                elif self.board[i][j].value == 9: c9 += 1

        return c1 < 2 and c2 < 2 and c3 < 2 and c4 < 2 and c5 < 2 and c6 < 2 and c7 < 2 and c8 < 2 and c9 < 2

    def generateBoard(self, difficulty):
        '''Board, int -> None
        Precondition: difficulty is greater than or equal
        to 2'''

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                dif = random.randint(0, difficulty+1)
                if (dif == 1):
                    self.board[i][j].value = random.randint(1,9)
                    while not (self.checkRow(i) and self.checkColumn(j) and self.checkSquare(i, j)):
                        self.board[i][j].value = random.randint(1, 9)
                    self.board[i][j].fixed = True

    def addValue(self, row, column, value):
        '''Board, int, int, int -> Boolean'''

    def removeValue(self, row, column):
        '''Board, int, int -> Boolean'''

    def isComplete(self):
        '''Board -> Boolean'''

        for i in len(self.board):
            for j in len(self.board[0]):
                if (self.board[i][j] == '-'):
                    return False
        return True

    def solveBackTracking(self):
        '''Board -> None'''

    def solveStochasticSearch(self):
        '''Board -> None'''

    def solveConstraint(self):
        '''Board -> None'''

    def solveExactCover(self):
        '''Board -> None'''