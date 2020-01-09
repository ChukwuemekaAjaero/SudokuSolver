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
dumBoard = [[1,2,3],[4,5,6],[7,8,9]]
while run:
    pygame.time.delay(100)



    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 255, 255), (0, 0, 500, 00)) #Makes a the background white
    pygame.draw.line(win, (0, 0, 0), (250, 0), (250, 500), 2)
    pygame.font.init()
    fnt = pygame.font.SysFont('comicsans', 40)
    text = fnt.render(str(dumBoard[1][2]), 1, (0, 0, 0))
    win.blit(text, (30, 30))
    text2 = fnt.render(str(dumBoard[2][2]), 1, (0, 0, 0))
    win.blit(text2, (60, 60))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                dumBoard[2][2] = dumBoard[2][2] + 1

    pygame.display.update()


#x = Board()
#x.generateBoard(2)
#x.displayBoard()





