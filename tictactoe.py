#!/usr/bin/env python

__author__ = 'Darren Carpenter'
__license__ = 'GPL'
__version__ = '0.0.1'
__email__ = 'germz@protonmail.ch'

# Notes: make it so you can play it one player

import sys
import itertools

firstplayer = raw_input('What is the name of player one: ')
secondplayer = raw_input('What is the name of player two: ')
available = ['1','2','3','4','5','6','7','8','9']
firstmoves = []
secondmoves = []
wincollection = [('1','2','3'), ('4','5','6'), ('7','8','9'),
                 ('1','4','7'), ('2','5','8'), ('3','6','9'),
                 ('1','5','9'), ('7','5','3'), ('3','2','1'),
                 ('6','5','4'), ('9','8','7'), ('7','4','1'),
                 ('8','5','2'), ('9','6','3'), ('9','5','1'),
                 ('3','5','7')]
board = '''

_1_|_2_|_3_
_4_|_5_|_6_
 7 | 8 | 9

'''

print '''

############################
# Tic Tac Toe - by: Darren #
############################

Rules: Select the position for your move by choosing the number in the
       corresponding space.

_1_|_2_|_3_
_4_|_5_|_6_
 7 | 8 | 9

'''

# the loop will continue until the available moves are exhausted
while len(available) >= 1:
    win1 = []
    win2 = []

    try:
        move1 = raw_input(firstplayer + ', your move: ')
        available.remove(move1)
        firstmoves.append(move1)
        board = str.replace(board, move1, "X", 1)
        print board
        win1.append(list(itertools.combinations(firstmoves, 3)))
        x = set(win1[0]) & set(wincollection)
        if len(list(x)) >= 1:
            winner = firstplayer
            print winner + ', you have won the game!'
            sys.exit(0)
        move2 = raw_input(secondplayer + ', your move: ')
        available.remove(move2)
        secondmoves.append(move2)
        board = str.replace(board, move2, "O", 1)
        print board
        win2.append(list(itertools.combinations(secondmoves, 3)))
        y = set(win2[0]) & set(wincollection)
        if len(list(y)) >= 1:
            winner = secondplayer
            print winner + ', you have won the game!'
            sys.exit(0)
    except ValueError:
        print "You made an invalid choice."
        continue
    except KeyboardInterrupt:
        quit = raw_input('\nWould you like to quit? [y/n] ')
        if quit.lower() == "y":
            sys.exit(0)
        if quit.lower() == "n":
            continue
