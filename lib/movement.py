import sys
import os
import math
sys.path.append(os.path.abspath("D:\\Miacik\\Projects\\2048-game\\lib"))
from sanitize import sanitizex, sanitizey
from helper import delete, turn

#variables
powers_of_two = [math.pow(2, i) for i in range(12)]

#functions
def moveXaxis(board, way):
    """
    Function used to move in list on x axis a.k.a. horzontal axis.
    """

    if(way == "right"):
        new_board = sanitizex(board, 'right')
        for i in range(len(new_board)):
            for j in range(len(new_board) - 1):
                if(new_board[i][j] in powers_of_two and new_board[i][j+1] == new_board[i][j]):
                    new_board[i][j+1] *= 2
                    delete(i,j,new_board)

        return new_board

    elif(way == "left"):
        new_board = sanitizex(board, 'left')
        for i in range(len(new_board)):
            for j in range(len(new_board) - 1):
                if(new_board[i][j] in powers_of_two and new_board[i][j-1] == new_board[i][j]):
                    new_board[i][j-1] *= 2
                    delete(i,j,new_board)

        return new_board

    else:
        raise Exception("Type in correct way !")

def moveYaxis(board, way):

    """
    Function used to move in list on y axis a.k.a. vertical axis.
    """

    if(way == "up"):
        new_board = turn(sanitizey(board, "up"))
        for i in range(len(new_board)):
            for j in range(len(new_board)):
                if(new_board[i][j] in powers_of_two and new_board[i][j] == new_board[i][j+1]):
                    new_board[i][j] *= 2
                    delete(i,j+1, new_board)

        return sanitizey(turn(new_board), "up")

    if(way == "down"):
        new_board = turn(sanitizey(board, "down"))
        for i in range(len(new_board)):
            for j in range(len(new_board) - 1):
                if(new_board[i][j] in powers_of_two and new_board[i][j+1] == new_board[i][j]):
                    new_board[i][j+1] *= 2
                    delete(i,j,new_board)

        return sanitizey(turn(new_board), "down")

    else:
        raise Exception("Type in correct way !")
