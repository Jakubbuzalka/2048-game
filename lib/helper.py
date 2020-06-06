def delete(x,y,board):
    """
        Function used to delete nums from board and replace them with 0
    """
    board[x][y] = 0

def turn(board):
    temp = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]

    for i in range(len(board)):
        for j in range(len(board)):
            temp[i][j] = board[j][i]

    return temp