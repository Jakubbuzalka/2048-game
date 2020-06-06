import numpy

board = [
    [0,1,0,0],
    [0,4,5,4],
    [1,2,6,0],
    [1,2,5,4]
]


def sanitizex(board, way):
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


    print(cache)

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
    
print(numpy.matrix(sanitizex(board, "right")))

