from bcolors import *
from bricks import *


class Powerup(Bricks):
    '''  Class for powerups '''

    powerdict = {1: bcolors.OKGREEN + 'S' + bcolors.ENDC, 2: bcolors.OKGREEN + 'W' + bcolors.ENDC,
                 3: bcolors.OKGREEN + 'I' + bcolors.ENDC, 4: bcolors.OKGREEN + 'F' + bcolors.ENDC}

    def __init__(self, board, player):
        ''' Constructor to create and object of Powerup class'''
        # Inheritance from the brick class
        Bricks.__init__(self, board)
        self.type = random.randint(1, 4)
        self.active = 25
        self.active_collect = 0

    def place(self, board):
        ''' Function to place the powerup on the board'''
        for i in range(4):
            board.board[self.xpos][self.ypos + i] = self.powerdict[self.type]
            board.board[self.xpos + 1][self.ypos + i] = self.powerdict[self.type]

    def collected_power(self, board, player):
        ''' Function to check if a powerup has been collected or destroyed on bomb explosion'''
        if (board.board[self.xpos][self.ypos]) == bcolors.OKGREEN + '^' + bcolors.ENDC:
            self.brick_destroyed = 1
        if (board.board[self.xpos][self.ypos] == bcolors.OKBLUE + 'B' + bcolors.ENDC and self.active > 0 and self.brick_destroyed == 0):
            self.brick_destroyed = 1
            checkflag = 0
            for p in player.powerups:
                if p.type == self.type:
                    p.active_collect = 30
                    checkflag = 1
            if checkflag == 0:
                self.active_collect = 30
                player.powerups.append(self)

    def get_active(self):
        ''' Function to return the actve count'''
        return self.active

    def get_active_collect(self):
        ''' Function to return the active_collect'''
        return self.active_collect

    def reduce_active(self):
        ''' Function to reduce the active count'''
        self.active = self.active - 1
