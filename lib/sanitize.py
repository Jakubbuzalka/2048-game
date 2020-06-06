import math
import sys
import os
sys.path.append(os.path.abspath("D:\\Miacik\\Projects\\2048-game\\lib"))
import helper

def sanitizex(board, way):
    """ 
    Function used to de-zero a list and append zeros in a horizontal axis in right or left
    """
    cache=[]
    result=[
        [],
        [],
        [],
        []
    ]

    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j] != 0):
                cache.append((board[i][j], i, j))

    for res in result:
        index = result.index(res)
        for k in range(len(cache)):
            if(index == cache[k][1]):
                res.append(cache[k][0])
                
    if(way == "left"):

        for res in result:
            while len(res) != 4:
                res.append(0)
        return result

    elif(way == "right"):

        for res in result:
            while len(res) != 4:
                res.insert(0,0)
        return result

    else:
        raise Exception("Choose right type, left or right !")
    
def sanitizey(board, way):
    """
    Function used to de-zero a list in a vertical axis and insert zeros back in position
    """
    
    vertical=[]
    cache = []
    new_board = [
        [],
        [],
        [],
        []
    ]

    vertical = helper.turn(board)
    

    for i in range(len(vertical)):
        for j in range(len(vertical)):
            if(vertical[i][j] != 0):
                cache.append((vertical[i][j], i, j))

    for nu in new_board:
        index = new_board.index(nu)
        for i in range(len(cache)):
            if(index == cache[i][1]):
                nu.append(cache[i][0])

    if(way == "up"):

        for nu in new_board:
            while len(nu) != 4:
                nu.append(0)
        return new_board

    elif(way == "down"):

        for nu in new_board:
            while len(nu) != 4:
                nu.insert(0,0)
        return new_board

    else:
        raise Exception("Choose right type, up or down !")
    

    return helper.turn(new_board)
            


