import sys
import time
import random
from bomb import *
from block import *
from bcolors import *
from getch import *
from bricks import *
from powerup import *


class Player(Block):
    ''' Class for the bomberman '''

    def __init__(self):
        ''' Constructor for bomberman '''
        Block.__init__(self)
        self.xpos = 2
        self.ypos = 4
        self.score = 0
        self.lives = 3
        self.powerups = []
        self.passwalls = 0
        self.immortal = 0
        self.fast = 0

    def move(self, board, bomb, powerup_obj_list, player):
        ''' Function to move the player on keyboard press '''

        # If fast powerup is enabled print the screen every 0.05 seconds
        if (self.fast == 1):
            time.sleep(0.04)
        else:
            time.sleep(0.5)
        inp = get_char_keyboard_nonblock()  # Gets keypress from the user

        # Keys to move up, down, left and right
        if (inp == 'a'):
            self.move_left(board, powerup_obj_list)
        elif (inp == 'w'):
            self.move_up(board, powerup_obj_list)
        elif (inp == 'd'):
            self.move_right(board, powerup_obj_list)
        elif (inp == 's'):
            self.move_down(board, powerup_obj_list)

        # Place bomb
        elif (inp == 'b'):
            if bomb.bomb_frames_remaining == -1:
                bomb.setpos(self.xpos, self.ypos)
                bomb.created_time = time.time()
                bomb.bomb_frames_remaining = 4

        # For powerup
        elif (inp == 'p'):
            powerup_obj = Powerup(board, player)
            powerup_obj_list.append(powerup_obj)

        # Quit the game
        elif (inp == 'q'):
            print("\n" + bcolors.WARNING + "YOU QUIT THE GAME" + bcolors.ENDC)
            sys.exit()

    def move_left(self, board, powerup_obj_list):
        ''' Function to move the bomberman to the left if possible'''
        if self.passwalls == 1:
            if (self.ypos - 4 >= 0):
                self.ypos = self.ypos - 4
        elif (self.ypos - 4 >= 0 and (
                board.board[self.xpos][self.ypos - 4] == ' ' or board.board[self.xpos][self.ypos - 4] in [
                    bcolors.OKGREEN + 'S' + bcolors.ENDC, bcolors.OKGREEN + 'W' + bcolors.ENDC,
                    bcolors.OKGREEN + 'F' + bcolors.ENDC, bcolors.OKGREEN + 'I' + bcolors.ENDC])):
            self.ypos = self.ypos - 4

    def move_up(self, board, powerup_obj_list):
        ''' Function to move the bomberman upwards if possible'''
        if self.passwalls == 1:
            if (self.xpos - 2 >= 0):
                self.xpos = self.xpos - 2
        elif (self.xpos - 2 >= 0 and (
                board.board[self.xpos - 2][self.ypos] == ' ' or board.board[self.xpos - 2][self.ypos] in [
                    bcolors.OKGREEN + 'S' + bcolors.ENDC, bcolors.OKGREEN + 'W' + bcolors.ENDC,
                    bcolors.OKGREEN + 'F' + bcolors.ENDC, bcolors.OKGREEN + 'I' + bcolors.ENDC])):
            self.xpos = self.xpos - 2

    def move_right(self, board, powerup_obj_list):
        ''' Function to move to the bomberman to the right if possible'''
        if self.passwalls == 1:
            if (self.ypos + 4 < board.Y):
                self.ypos = self.ypos + 4
        elif (self.ypos + 4 < board.Y and (
                board.board[self.xpos][self.ypos + 4] == ' ' or board.board[self.xpos][self.ypos + 4] in [
                    bcolors.OKGREEN + 'S' + bcolors.ENDC, bcolors.OKGREEN + 'W' + bcolors.ENDC,
                    bcolors.OKGREEN + 'F' + bcolors.ENDC, bcolors.OKGREEN + 'I' + bcolors.ENDC])):
            self.ypos = self.ypos + 4

    def move_down(self, board, powerup_obj_list):
        ''' Function to move the bomberman downwards if possible'''
        if self.passwalls == 1:
            if (self.xpos + 2 < board.X):
                self.xpos = self.xpos + 2
        elif (self.xpos + 2 < board.X and (
                board.board[self.xpos + 2][self.ypos] == ' ' or board.board[self.xpos + 2][self.ypos] in [
                    bcolors.OKGREEN + 'S' + bcolors.ENDC, bcolors.OKGREEN + 'W' + bcolors.ENDC,
                    bcolors.OKGREEN + 'F' + bcolors.ENDC, bcolors.OKGREEN + 'I' + bcolors.ENDC])):
            self.xpos = self.xpos + 2

    def clear(self, board):
        ''' Function to remove the bomberman from a particular position on the board'''
        board.board[self.xpos][self.ypos] = ' '
        board.board[self.xpos][self.ypos + 1] = ' '
        board.board[self.xpos][self.ypos + 2] = ' '
        board.board[self.xpos][self.ypos + 3] = ' '
        board.board[self.xpos + 1][self.ypos] = ' '
        board.board[self.xpos + 1][self.ypos + 1] = ' '
        board.board[self.xpos + 1][self.ypos + 2] = ' '
        board.board[self.xpos + 1][self.ypos + 3] = ' '

    def place(self, board):
        ''' Function to place the bomberman on a particular position on the board'''
        board.board[self.xpos][self.ypos] = bcolors.OKBLUE + 'B' + bcolors.ENDC
        board.board[self.xpos][self.ypos + 1] = bcolors.OKBLUE + 'B' + bcolors.ENDC
        board.board[self.xpos][self.ypos + 2] = bcolors.OKBLUE + 'B' + bcolors.ENDC
        board.board[self.xpos][self.ypos + 3] = bcolors.OKBLUE + 'B' + bcolors.ENDC
        board.board[self.xpos + 1][self.ypos] = bcolors.OKBLUE + 'B' + bcolors.ENDC
        board.board[self.xpos + 1][self.ypos + 1] = bcolors.OKBLUE + 'B' + bcolors.ENDC
        board.board[self.xpos + 1][self.ypos + 2] = bcolors.OKBLUE + 'B' + bcolors.ENDC
        board.board[self.xpos + 1][self.ypos + 3] = bcolors.OKBLUE + 'B' + bcolors.ENDC

    def check_player_win(self, enemy_list, num_of_enemies):
        ''' Function to check if all the enemies are dead => player wins'''
        for i in range(num_of_enemies):
            if (enemy_list[i].enemy_destroyed == 0):
                return 0
        return 1

    def check_player_die(self, board, bomb):
        ''' Function to check if the bomberman is dead'''
        if self.immortal == 1:
            return 0
        if board.board[self.xpos + 1][self.ypos] == bcolors.OKGREEN + '^' + bcolors.ENDC or board.board[self.xpos][
           self.ypos] == bcolors.FAIL + 'E' + bcolors.ENDC:
            self.xpos = 2
            self.ypos = 4
            self.lives = self.lives - 1
            bomb.bomb_frames_remaining = -1
            if (self.lives == 0):
                return 1
        return 0

    def get_lives(self):
        ''' Function to return the number of lives'''
        return self.lives

    def get_score(self):
        ''' Function to return the score'''
        return self.score

    def check_player_fast(self):
        ''' Function to check if the player has speed up powerup enabled'''
        checkflag = 0
        for p in self.powerups:
            if p.type == 4 and p.active_collect > 0:
                checkflag = 1
                p.active_collect = p.active_collect - 1
                self.fast = 1
        if checkflag == 0:
            self.fast = 0

    def is_fast(self):
        ''' Function to check if the self.fast attribute is set or not'''
        return self.fast

    def player_pass_wall(self):
        ''' Function to check if the player has pass through wall powerup enabled'''
        checkflag = 0
        for p in self.powerups:
            if p.type == 2 and p.active_collect > 0:
                checkflag = 1
                p.active_collect = p.active_collect - 1
                self.passwalls = 1
        if checkflag == 0:
            self.passwalls = 0

    def player_check_immortal(self):
        ''' Function to check if the immortal powerup enabled'''
        checkflag = 0
        for p in self.powerups:
            if p.type == 3 and p.active_collect > 0:
                checkflag = 1
                p.active_collect = p.active_collect - 1
                self.immortal = 1
        if checkflag == 0:
            self.immortal = 0
