import numpy
import math
import random
import sys
import os
sys.path.append(os.path.abspath("D:\\Miacik\\Projects\\2048-game\\lib"))
from sanitize import *
from helper import *

#global variables
board = [
    [0,1,0,0],
    [0,4,5,4],
    [1,2,6,0],
    [1,2,5,4]
]

powers_of_two = [math.pow(2, i) for i in range(12)]



def moveXaxis(board):
    new_board = sanitizex(board, 'right')
    for i in range(len(new_board)):
        for j in range(len(new_board) - 1):
            if(new_board[i][j] in powers_of_two and new_board[i][j+1] == new_board[i][j]):
                new_board[i][j+1] *= 2
                delete(i,j,new_board)

    board = new_board


moveXaxis(board)
print(board)