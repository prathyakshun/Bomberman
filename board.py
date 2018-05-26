from bcolors import *


class Board:
    ''' Class for the board'''

    def __init__(self):
        ''' Constructor to create an object of the board class'''
        self.X = 38
        self.Y = 76
        self.board = [[' ' for i in range(self.Y)] for j in range(self.X)]

    def init_board(self):
        ''' Function to initialise a blank board with the walls'''
        for i in range(self.X):
            for j in range(self.Y):
                if i == 0 or i == 1 or i == self.X - 2 or i == self.X - 1 or j == 0 or j == 1 or j == 2 or j == 3 or j == self.Y - 4 or j == self.Y - 3 or j == self.Y - 2 or j == self.Y - 1:
                    self.board[i][j] = bcolors.HEADER + '#' + bcolors.ENDC
                elif (i % 4 == 0 or i % 4 == 1) and (j % 8 == 0 or j % 8 == 1 or j % 8 == 2 or j % 8 == 3):
                    self.board[i][j] = bcolors.HEADER + '#' + bcolors.ENDC
                else:
                    self.board[i][j] = ' '

    def printboard(self):
        ''' Function to print the board'''
        for i in range(self.X):
            for j in range(self.Y):
                print(self.board[i][j], end='')
            print()
