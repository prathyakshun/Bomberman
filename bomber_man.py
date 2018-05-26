from board import *
from player import *
from enemy import *
from bomb import *
from bricks import *
from bcolors import *
from block import *
import subprocess
import sys
import time

# Initialize the variables
num_of_bricks = 20
num_of_enemies = 0
timecount = 0
levels = 3

# Run the game number of levels times
for level in range(levels):

    # Each level the number of bricks and the number of enemies increase by 5
    num_of_bricks = num_of_bricks + 5
    num_of_enemies = num_of_enemies + 5
    # Initializing the list to empty lists
    brick_obj_list = []
    enemy_obj_list = []
    powerup_obj_list = []

    # Creating the objects of each class
    board_obj = Board()
    board_obj.init_board()
    player_obj = Player()
    bomb_obj = Bomb(0, 0)

    # Creating the bricks and the enemies
    for i in range(num_of_bricks):
        brick_obj = Bricks(board_obj)
        brick_obj_list.append(brick_obj)

    for i in range(num_of_enemies):
        enemy_obj = Enemy(board_obj)
        enemy_obj_list.append(enemy_obj)

    # Placing the objects created on the board
    player_obj.place(board_obj)

    for i in range(num_of_bricks):
        if (brick_obj_list[i].is_brick_destroyed() == 0):
            brick_obj_list[i].place(board_obj)

    for i in range(num_of_enemies):
        if (enemy_obj_list[i].is_enemy_dead() == 0):
            enemy_obj_list[i].place(board_obj)

    # Printing the board
    board_obj.printboard()

    # Loop till the player loses all his lives
    while (player_obj.get_lives() > 0):

        # Slowing down the timer for powerup active time when the bomberman
        # has move fast powerup enabled
        if (player_obj.fast == 1):
            if (timecount % 10 == 0):
                for p in powerup_obj_list:
                    if (p.get_active() > 0):
                        p.reduce_active()
                    p.clear(board_obj)
        else:
            for p in powerup_obj_list:
                if (p.get_active() > 0):
                    p.reduce_active()
                p.clear(board_obj)

        # Clear the existing position (older positions)
        # of the objects from the board
        for i in range(num_of_bricks):
            brick_obj_list[i].clear(board_obj)
        bomb_obj.clear(board_obj)
        player_obj.clear(board_obj)

        # Initialzing the board with just the wall
        board_obj.init_board()

        # Slowing down the timer to check whether the powerup is enabled
        # when the bomberman has move fast powerup enabled
        if (player_obj.is_fast() == 1):
            if (timecount % 10 == 0):
                player_obj.player_pass_wall()
                player_obj.player_check_immortal()
                player_obj.check_player_fast()
                bomb_obj.update_bomb(player_obj)
        else:
            player_obj.player_pass_wall()
            player_obj.player_check_immortal()
            player_obj.check_player_fast()
            bomb_obj.update_bomb(player_obj)

        # Placing the objects in the updated positions on the board
        for i in range(num_of_bricks):
            if (brick_obj_list[i].is_brick_destroyed() == 0):
                brick_obj_list[i].place(board_obj)

        for p in powerup_obj_list:
            if (p.is_brick_destroyed() == 0 and p.get_active() > 0):
                p.place(board_obj)

        # Slowing down the bomb timer when the
        # bomberman has move fast powerup enabled
        if (player_obj.is_fast() == 1):
            if (bomb_obj.get_bomb_frames() > 0):
                if (timecount % 10 == 0):
                    bomb_obj.reduce_bomb_frames()
                bomb_obj.place(board_obj)
        else:
            if (bomb_obj.get_bomb_frames() > 0):
                bomb_obj.reduce_bomb_frames()
                bomb_obj.place(board_obj)

        # Call the function to move the player
        player_obj.move(board_obj, bomb_obj, powerup_obj_list, player_obj)

        # Timecount which is useful when the bomberman has fast powerup enabled
        timecount = timecount + 1
        if timecount % 10 == 0:
            timecount = 0

        # Clear the shell
        tmp = subprocess.call('clear', shell=True)

        for i in range(num_of_enemies):
            enemy_obj_list[i].clear(board_obj)

        # Slowing down the enemy when the bomberman has fast powerup enabled
        if (player_obj.is_fast() == 1):
            if (timecount % 10 == 0):
                for i in range(num_of_enemies):
                    enemy_obj_list[i].move(board_obj)
        else:
            for i in range(num_of_enemies):
                enemy_obj_list[i].move(board_obj)

        # Print the bomb timer
        print("bomb frames remaining " + str(bomb_obj.get_bomb_frames()))

        # Place the objects on the updated positions on the board
        player_obj.place(board_obj)
        for i in range(num_of_enemies):
            if (enemy_obj_list[i].is_enemy_dead() == 0):
                enemy_obj_list[i].place(board_obj)

        if (bomb_obj.get_bomb_frames() == 0):
            bomb_obj.reduce_bomb_frames()
            bomb_obj.place_fire(board_obj)

        # Call the function to print the board on every iteration
        board_obj.printboard()

        # Display the player's score, lives and powerups active time
        print (bcolors.HEADER)
        print("Player's score : " + str(player_obj.get_score()))
        print("Player's lives : " + str(player_obj.get_lives()))
        print("Level " + str(level + 1))
        for p in player_obj.powerups:
            if p.type == 1:
                print("Super Explosion " + str(p.get_active_collect()))
            elif p.type == 2:
                print("Pass through Wall " + str(p.get_active_collect()))
            elif p.type == 3:
                print("Player immortal " + str(p.get_active_collect()))
            elif p.type == 4:
                print("Player fast " + str(p.get_active_collect()))
        print(bcolors.ENDC)

        # Call function to check if the player or enemy dies
        for i in range(num_of_enemies):
            enemy_obj_list[i].check_enemy_die(board_obj, player_obj)

        if (player_obj.check_player_die(board_obj, bomb_obj) == 1):
            board_obj.printboard()
            print (bcolors.HEADER)
            print("Player's score :", end=' ')
            print(player_obj.get_score())
            print("Player's lives :", end=' '),
            print(player_obj.get_lives())
            print("GAME OVER! TRY AGAIN?")
            print(bcolors.ENDC)
            sys.exit()

        # Call function to check if the powerup has been collected
        for p in powerup_obj_list:
            p.collected_power(board_obj, player_obj)

        # Check if brick has been destroyed on bomb explosion
        for i in range(num_of_bricks):
            brick_obj_list[i].check_brick_destroyed(board_obj, player_obj)

        # Check if the player has won the level
        if (player_obj.check_player_win(enemy_obj_list, num_of_enemies) == 1):
            print(bcolors.WARNING + "CONGRATULATIONS, YOU HAVE WON THE GAME!" + bcolors.ENDC)
            break
