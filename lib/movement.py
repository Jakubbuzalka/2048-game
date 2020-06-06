import sys
import os
import math
sys.path.append(os.path.abspath("D:\\Miacik\\Projects\\2048-game\\lib"))
from sanitize import sanitizex
from helper import delete

#variables
powers_of_two = [math.pow(2, i) for i in range(12)]

#functions
def moveXaxis(board):
    new_board = sanitizex(board, 'right')
    for i in range(len(new_board)):
        for j in range(len(new_board) - 1):
            if(new_board[i][j] in powers_of_two and new_board[i][j+1] == new_board[i][j]):
                new_board[i][j+1] *= 2
                delete(i,j,new_board)

    return new_board

