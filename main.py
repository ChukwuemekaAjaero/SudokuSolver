from SudokuLibrary import *
print(3)
x = Board()
x.generateBoard(1)
x.displayBoard()
print("\n***************************************************************\n")
print(x.checkLocationSafe(4, 4, 7))
print("\n***************************************************************\n")
if(x.solveBackTracking()):
    x.displayBoard()
else:
    print("No solution")




