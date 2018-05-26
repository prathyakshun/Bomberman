from block import *
from bcolors import *


class Bomb(Block):
    ''' Class for bomb'''

    def __init__(self, xpos, ypos):
        ''' Constructor to create an object of Bomb class'''
        Block.__init__(self)
        self.bomb_frames_remaining = -1
        self.xpos = xpos
        self.ypos = ypos
        self.rady = 4
        self.radx = 2
        self.created_time = 0

    def setpos(self, xpos, ypos):
        ''' Function to set the position of the bomb'''
        self.xpos = xpos
        self.ypos = ypos

    def place(self, board):
        ''' Function to place the bomb at a particular position on the board'''
        if (self.bomb_frames_remaining > 0):
            board.board[self.xpos][self.ypos] = bcolors.OKGREEN + '[' + bcolors.ENDC
            board.board[self.xpos][self.ypos + 1] = self.bomb_frames_remaining - 1
            board.board[self.xpos][self.ypos + 2] = self.bomb_frames_remaining - 1
            board.board[self.xpos][self.ypos + 3] = bcolors.OKGREEN + ']' + bcolors.ENDC
            board.board[self.xpos + 1][self.ypos] = bcolors.OKGREEN + '[' + bcolors.ENDC
            board.board[self.xpos + 1][self.ypos + 1] = self.bomb_frames_remaining - 1
            board.board[self.xpos + 1][self.ypos + 2] = self.bomb_frames_remaining - 1
            board.board[self.xpos + 1][self.ypos + 3] = bcolors.OKGREEN + ']' + bcolors.ENDC

    def update_bomb(self, player):
        ''' Function to update the bomb to super explosive if super explosion powerup is collected'''
        checkflag = 0
        for p in player.powerups:
            if p.type == 1 and p.active_collect > 0:
                checkflag = 1
                p.active_collect = p.active_collect - 1
                self.rady = 8
                self.radx = 4
        if checkflag == 0:
            self.rady = 4
            self.radx = 2

    def get_bomb_frames(self):
        ''' Function to return the bomb frames remaining'''
        return self.bomb_frames_remaining

    def reduce_bomb_frames(self):
        ''' Function to reduce the bomb frames by 1'''
        self.bomb_frames_remaining = self.bomb_frames_remaining - 1

    def place_fire(self, board):
        ''' Function to place fire on the board when the bomb explodes'''
        if (self.bomb_frames_remaining == -1):
            till = self.rady + 4
            for i in range(self.rady + 4):
                if (self.ypos + i < board.Y and self.ypos + i >= 0 and board.board[self.xpos][
                        self.ypos + i] == bcolors.HEADER + '#' + bcolors.ENDC):
                    till = i
                    break
            for i in range(till):
                if (self.ypos + i < board.Y and self.ypos + i >= 0 and board.board[self.xpos][
                        self.ypos + i] != bcolors.HEADER + '#' + bcolors.ENDC):
                    board.board[self.xpos][self.ypos + i] = bcolors.OKGREEN + '^' + bcolors.ENDC
                if (self.ypos + i < board.Y and self.ypos + i >= 0 and self.xpos + 1 < board.X and
                   board.board[self.xpos + 1][self.ypos + i] != bcolors.HEADER + '#' + bcolors.ENDC):
                    board.board[self.xpos + 1][self.ypos + i] = bcolors.OKGREEN + '^' + bcolors.ENDC

            till = self.rady
            for i in range(self.rady):
                if (self.ypos - i >= 0 and board.board[self.xpos][
                        self.ypos - i] == bcolors.HEADER + '#' + bcolors.ENDC):
                    till = i
                    break
            for i in range(1, till + 1):
                if (self.ypos - i >= 0 and board.board[self.xpos][
                        self.ypos - i] != bcolors.HEADER + '#' + bcolors.ENDC):
                    board.board[self.xpos][self.ypos - i] = bcolors.OKGREEN + '^' + bcolors.ENDC
                if (self.ypos - i >= 0 and self.xpos + 1 < board.X and board.board[self.xpos + 1][
                        self.ypos - i] != bcolors.HEADER + '#' + bcolors.ENDC):
                    board.board[self.xpos + 1][self.ypos - i] = bcolors.OKGREEN + '^' + bcolors.ENDC

            till = self.radx + 2
            for i in range(self.radx + 2):
                if (self.xpos + i < board.X and self.xpos + i >= 0 and board.board[self.xpos + i][
                   self.ypos] == bcolors.HEADER + '#' + bcolors.ENDC):
                    till = i
                    break
            for i in range(till):
                if (self.xpos + i < board.X and self.xpos + i >= 0 and board.board[self.xpos + i][
                   self.ypos] != bcolors.HEADER + '#' + bcolors.ENDC):
                    board.board[self.xpos + i][self.ypos] = bcolors.OKGREEN + '^' + bcolors.ENDC
                if (self.xpos + i < board.X and self.xpos + i >= 0 and self.ypos + 1 < board.Y and
                   board.board[self.xpos + i][self.ypos + 1] != bcolors.HEADER + '#' + bcolors.ENDC):
                    board.board[self.xpos + i][self.ypos + 1] = bcolors.OKGREEN + '^' + bcolors.ENDC
                if (self.xpos + i < board.X and self.xpos + i >= 0 and self.ypos + 2 < board.Y and
                   board.board[self.xpos + i][self.ypos + 2] != bcolors.HEADER + '#' + bcolors.ENDC):
                    board.board[self.xpos + i][self.ypos + 2] = bcolors.OKGREEN + '^' + bcolors.ENDC
                if (self.xpos + i < board.X and self.xpos + i >= 0 and self.ypos + 3 < board.Y and
                   board.board[self.xpos + i][self.ypos + 3] != bcolors.HEADER + '#' + bcolors.ENDC):
                    board.board[self.xpos + i][self.ypos + 3] = bcolors.OKGREEN + '^' + bcolors.ENDC

            till = self.radx
            for i in range(self.radx):
                if (self.xpos - i >= 0 and board.board[self.xpos - i][
                   self.ypos] == bcolors.HEADER + '#' + bcolors.ENDC):
                    till = i
                    break
            for i in range(1, till + 1):
                if (self.xpos - i >= 0 and board.board[self.xpos - i][
                   self.ypos] != bcolors.HEADER + '#' + bcolors.ENDC):
                    board.board[self.xpos - i][self.ypos] = bcolors.OKGREEN + '^' + bcolors.ENDC
                if (self.xpos - i >= 0 and board.board[self.xpos - i][
                        self.ypos + 1] != bcolors.HEADER + '#' + bcolors.ENDC):
                    board.board[self.xpos - i][self.ypos + 1] = bcolors.OKGREEN + '^' + bcolors.ENDC
                if (self.xpos - i >= 0 and board.board[self.xpos - i][
                        self.ypos + 2] != bcolors.HEADER + '#' + bcolors.ENDC):
                    board.board[self.xpos - i][self.ypos + 2] = bcolors.OKGREEN + '^' + bcolors.ENDC
                if (self.xpos - i >= 0 and board.board[self.xpos - i][
                        self.ypos + 3] != bcolors.HEADER + '#' + bcolors.ENDC):
                    board.board[self.xpos - i][self.ypos + 3] = bcolors.OKGREEN + '^' + bcolors.ENDC

    def clear(self, board):
        ''' Function to clear the fire from the board'''
        startx = self.xpos - self.radx
        starty = self.ypos - self.rady
        for i in range(2 * self.rady + 4):
            if (starty + i < board.Y and starty + i >= 0 and board.board[self.xpos][
                    starty + i] != bcolors.HEADER + '#' + bcolors.ENDC):
                board.board[self.xpos][starty + i] = ' '
                board.board[self.xpos + 1][starty + i] = ' '
        for i in range(2 * self.radx + 2):
            if (startx + i < board.X and startx + i >= 0 and board.board[startx + i][
               self.ypos] != bcolors.HEADER + '#' + bcolors.ENDC):
                board.board[startx + i][self.ypos] = ' '
                board.board[startx + i][self.ypos + 1] = ' '
                board.board[startx + i][self.ypos + 2] = ' '
                board.board[startx + i][self.ypos + 3] = ' '
                board.board[self.xpos][self.ypos] = ' '
                board.board[self.xpos][self.ypos + 1] = ' '
                board.board[self.xpos][self.ypos + 2] = ' '
                board.board[self.xpos][self.ypos + 3] = ' '
                board.board[self.xpos + 1][self.ypos] = ' '
                board.board[self.xpos + 1][self.ypos + 1] = ' '
                board.board[self.xpos + 1][self.ypos + 2] = ' '
                board.board[self.xpos + 1][self.ypos + 3] = ' '
