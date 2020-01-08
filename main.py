from SudokuLibrary import *
import pygame
import GUI
run = True
win = pygame.display.set_mode((450, 500))
pygame.display.set_caption("Sudoku")

x = 50
y = 50
width = 50
height = 50
velocity = 5

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 255, 255), (0, 0, 500, 00)) #Makes a the background white
    pygame.draw.line(win, (0, 0, 0), (250, 0), (250, 500), 2)
    pygame.display.update()


#x = Board()
#x.generateBoard(2)
#x.displayBoard()





