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
            font = pygame.font.SysFont('comicsans', 60)
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