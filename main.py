from SudokuLibrary import *
import pygame
from GUI import *
import time
run = True
win = pygame.display.set_mode((450, 500))
win.fill((255, 255, 255))
pygame.display.set_caption("Sudoku")
x = Board()
x.generateBoard()

#Test Lines
x = 50
y = 50
width = 50
height = 50
velocity = 5
dumBoard = [[1,2,3],[4,5,6],[7,8,9]]
solveButton = Button((255, 255, 255), 150, 225, 70, 50, 'Solve')
#End Test Lines

#Static Elements
startTime = time.time()
clearButton = Button((255, 255, 255), 18, 462, 55, 27, 'Clear')
solveButton = Button((255, 255, 255), 123, 462, 55, 27, 'Solve')
submitButton = Button((255, 255, 255), 228, 462, 55, 27, 'Submit')
while run:
    #pygame.time.delay(100)
    pygame.font.init()
    fnt = pygame.font.SysFont('serif', 20)
    playTime = round(time.time() - startTime)
    clearButton.draw(win, (0, 0, 0))
    solveButton.draw(win, (0, 0, 0))
    submitButton.draw(win, (0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), (0, 0, 500, 00))  # Makes a the background white

    text = fnt.render(str(dumBoard[1][2]), 1, (0, 0, 0))
    win.blit(text, (30, 30))
    text2 = fnt.render(str(dumBoard[2][2]), 1, (0, 0, 0))
    win.blit(text2, (60, 60))


    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                dumBoard[2][2] = dumBoard[2][2] + 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if solveButton.isOver(pos):
                solveButton.colour = (34, 24, 84)
        if event.type == pygame.MOUSEMOTION:
            if solveButton.isOver(pos):
                dumBoard[2][2] = dumBoard[2][2] + 00
    redrawWindow(win, x.board, playTime)
    pygame.display.update()


#x = Board()
#x.generateBoard(2)
#x.displayBoard()





