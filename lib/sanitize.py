
board = [
    [0,1,2,3],
    [0,4,5,4],
    [1,2,6,0],
    [1,2,5,4]
]


def sanitize(board, way=0):
    """ 
    Function used to de-zero a list and append them in a way
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
        for k in range(len(cache)):
            if(result.index(res) == cache[k][1]):
                res.append(cache[k][0])

    if(way == "left"):
        pass
    elif(way == "right"):

        for res in result:
            if(len(res) != 4):
                res.insert(0,0)
        return result

    else:
        return "No other way is possible for now"
    
   

print(sanitize(board))
