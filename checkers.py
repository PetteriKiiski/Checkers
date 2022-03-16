import pygame, sys
from pygame.locals import *
canvas = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Checkers")
class Board:
    def __init__(self):
        self.board = [
        ["BW", "BB", "BW", "BB", "BW", "BB", "BW", "BB"],
        ["BB", "BW", "BB", "BW", "BB", "BW", "BB", "BW"],
        ["BW", "BB", "BW", "BB", "BW", "BB", "BW", "BB"],
        ["BB", "BW", "BB", "BW", "BB", "BW", "BB", "BW"],      
        ["BW", "BB", "BW", "BB", "BW", "BB", "BW", "BB"],
        ["BB", "BW", "BB", "BW", "BB", "BW", "BB", "BW"],
        ["BW", "BB", "BW", "BB", "BW", "BB", "BW", "BB"],
        ["BB", "BW", "BB", "BW", "BB", "BW", "BB", "BW"]]
    def place(self, loc, color):
        self.board[loc[0]][loc[1]] = color
    def remove(self, loc)
        if self.board[loc[0]][loc[1]] not in ["BB", "BW"]:
            self.board[loc[0]][loc[1]] = "BB"
class Checker:
    def __init__(self, color, loc, board):
        self.color = color
        self.loc = loc
        self.board = board
        self.board.place(self.loc, self.color)
board = Board()
Checkers = []
for i in 
while True:
    canvas.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
