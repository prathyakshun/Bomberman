import random
from block import *
from bcolors import *
from bricks import *


class Bricks(Block):
    ''' Class for the bricks placed on the board'''

    def __init__(self, board):
        ''' Constructor to create an object of Bricks class'''
        Block.__init__(self)
        self.valid_brick = 0
        self.brick_destroyed = 0
        while (self.valid_brick != 1):
            self.xpos = random.randint(0, board.X - 1)
            self.ypos = random.randint(0, board.Y - 1)
            if board.board[self.xpos][
               self.ypos] == ' ' and self.xpos * self.ypos > 26 * 10 and self.xpos % 2 == 0 and self.ypos % 4 == 0:
                self.valid_brick = 1

    def place(self, board):
        ''' Function to place the bricks at a particular position on the board'''
        for i in range(4):
            board.board[self.xpos][self.ypos + i] = bcolors.WARNING + '%' + bcolors.ENDC
            board.board[self.xpos + 1][self.ypos + i] = bcolors.WARNING + '%' + bcolors.ENDC

    def clear(self, board):
        ''' Functino to clear the brick from a particular position on the board'''
        for i in range(4):
            board.board[self.xpos][self.ypos + i] = ' '
            board.board[self.xpos + 1][self.ypos + i] = ' '

    def check_brick_destroyed(self, board, player):
        ''' Function to check if the brick has been destroyed due to a bomb explosion'''
        if board.board[self.xpos][self.ypos] == bcolors.OKGREEN + '^' + bcolors.ENDC:
            player.score = player.score + 20
            self.brick_destroyed = 1

    def is_brick_destroyed(self):
        ''' Function to return whether the brick is destroyed'''
        return self.brick_destroyed
