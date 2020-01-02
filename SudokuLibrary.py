class Cell:
    def __init__(self, value = "", fixed = True):
        self.value = value
        self.fixed = fixed

class Board:
    def __int__(self):
        board = []

    def emptyBoard(self):
        '''Board -> None'''

    def displayBoard(self):
        '''Board -> None'''

    def checkBoard(self):
        '''Board -> Boolean'''

    def generateBoard(self):
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