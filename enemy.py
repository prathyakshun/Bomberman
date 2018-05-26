from block import *
from bcolors import *
import random


class Enemy(Block):
    ''' Class for enemy'''

    def __init__(self, board):
        ''' Constructor for creating an object of enemy class'''
        Block.__init__(self)
        self.valid_move = 0
        self.valid_pos = 0
        while (self.valid_pos != 1):
            self.xpos = random.randint(0, board.X - 1)
            self.ypos = random.randint(0, board.Y - 1)
            if board.board[self.xpos][
               self.ypos] != bcolors.HEADER + '#' + bcolors.ENDC and self.xpos * self.ypos > 26 * 10 and self.xpos % 2 == 0 and self.ypos % 4 == 0:
                self.valid_pos = 1
        self.enemy_destroyed = 0
        self.no_of_times_destroyed = random.randint(1, 3)

    def place(self, board):
        ''' Function to place an enemy in a particular position on the board'''
        board.board[self.xpos][self.ypos] = bcolors.FAIL + 'E' + bcolors.ENDC
        board.board[self.xpos][self.ypos + 1] = bcolors.FAIL + str(self.no_of_times_destroyed) + bcolors.ENDC
        board.board[self.xpos][self.ypos + 2] = bcolors.FAIL + str(self.no_of_times_destroyed) + bcolors.ENDC
        board.board[self.xpos][self.ypos + 3] = bcolors.FAIL + 'E' + bcolors.ENDC
        board.board[self.xpos + 1][self.ypos] = bcolors.FAIL + 'E' + bcolors.ENDC
        board.board[self.xpos + 1][self.ypos + 1] = bcolors.FAIL + str(self.no_of_times_destroyed) + bcolors.ENDC
        board.board[self.xpos + 1][self.ypos + 2] = bcolors.FAIL + str(self.no_of_times_destroyed) + bcolors.ENDC
        board.board[self.xpos + 1][self.ypos + 3] = bcolors.FAIL + 'E' + bcolors.ENDC

    def move(self, board):
        ''' Function to move an enemy randomly on the board'''
        self.valid_move = 0
        while (self.valid_move == 0):
            enemy_moving = random.randrange(0, 4)
            if (enemy_moving == 0):
                if (self.xpos - 2 >= 0 and board.board[self.xpos - 2][self.ypos] == ' ' or board.board[self.xpos - 2][
                   self.ypos] == bcolors.OKBLUE + 'B' + bcolors.ENDC):
                    self.valid_move = 1
                    self.xpos = self.xpos - 2
            elif (enemy_moving == 1):
                if (self.ypos - 4 >= 0 and board.board[self.xpos][self.ypos - 4] == ' ' or board.board[self.xpos][
                        self.ypos - 4] == bcolors.OKBLUE + 'B' + bcolors.ENDC):
                    self.valid_move = 1
                    self.ypos = self.ypos - 4
            elif (enemy_moving == 2):
                if (self.xpos + 2 < board.X and board.board[self.xpos + 2][self.ypos] == ' ' or
                   board.board[self.xpos + 2][self.ypos] == bcolors.OKBLUE + 'B' + bcolors.ENDC):
                    self.valid_move = 1
                    self.xpos = self.xpos + 2
            elif (enemy_moving == 3):
                if (self.ypos + 4 < board.Y and board.board[self.xpos][self.ypos + 4] == ' ' or board.board[self.xpos][
                        self.ypos + 4] == bcolors.OKBLUE + 'B' + bcolors.ENDC):
                    self.valid_move = 1
                    self.ypos = self.ypos + 4

    def clear(self, board):
        ''' Function to clear an enemy from the board'''
        board.board[self.xpos][self.ypos] = ' '
        board.board[self.xpos][self.ypos + 1] = ' '
        board.board[self.xpos][self.ypos + 2] = ' '
        board.board[self.xpos][self.ypos + 3] = ' '
        board.board[self.xpos + 1][self.ypos] = ' '
        board.board[self.xpos + 1][self.ypos + 1] = ' '
        board.board[self.xpos + 1][self.ypos + 2] = ' '
        board.board[self.xpos + 1][self.ypos + 3] = ' '

    def check_enemy_die(self, board, player):
        ''' Function to check if an enemy has died'''
        if board.board[self.xpos + 1][self.ypos] == bcolors.OKGREEN + '^' + bcolors.ENDC:
            self.no_of_times_destroyed = self.no_of_times_destroyed - 1
        if (self.no_of_times_destroyed == 0 and self.enemy_destroyed == 0):
            player.score = player.score + 100
            self.enemy_destroyed = 1

    def is_enemy_dead(self):
        ''' Function to check if the enemy is dead'''
        return self.enemy_destroyed
