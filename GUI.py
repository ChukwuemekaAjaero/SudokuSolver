import pygame

class Button:
    def __init__(self, colour, x, y, width, height, text = ''):
        '''Button, tuple, int, int, int, int, string -> None'''
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline = None):
        '''Button, pygame.display, pygame.rect -> None
        This method draws the button on the board
        '''

        if outline:
            pygame.draw.rect(win, (0,0,0), (self.x-2, self.y-2, self.width+4, self.height+4))

        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 20)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, position):
        '''Button, tuple -> Boolean
        Returns True if the mouse position is above the button
        and False otherwise.'''
        if position[0] > self.x and position[0] < self.x + self.width:
            if position[1] > self.y and position[1] < self.y + self.height:
                return True
        return False

class Square:

    isClicked = False
    outline = False
    def __init__(self, colour, x, y, height, text = ''):
        self.colour = colour
        self.x = x
        self.y = y
        self.height = height
        self.text = text

    def isOver(self, position):
        '''Button, tuple -> Boolean
        Returns True if the mouse position is above the button
        and False otherwise.'''
        if position[0] > self.x and position[0] < self.x + self.width:
            if position[1] > self.y and position[1] < self.y + self.height:
                return True
        return False

def formatTime(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat

def redrawWindow(win, board, playTime):
    win.fill((255, 255, 255))
    pygame.draw.line(win, (0, 0, 0), (150, 0), (150, 450), 2)
    pygame.draw.line(win, (0, 0, 0), (300, 0), (300, 450), 2)
    pygame.draw.line(win, (0, 0, 0), (0, 150), (450, 150), 2)
    pygame.draw.line(win, (0, 0, 0), (0, 300), (450, 300), 2)
    pygame.draw.line(win, (0, 0, 0), (0, 450), (450, 450), 2)
    #Drawing the timer:
    fnt = pygame.font.SysFont('comicsans', 30)
    text = fnt.render("Time: " + formatTime(playTime), 1, (0, 0, 0))
    win.blit(text, (333, 462))