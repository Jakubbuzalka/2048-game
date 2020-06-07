import numpy
import random
import sys
import os
from time import sleep
sys.path.append(os.path.abspath("D:\\Miacik\\Projects\\2048-game\\lib"))
from movement import moveXaxis, moveYaxis
from helper import plot

#variables
board = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

#functions
def win():
    winrate = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i][j] == 2048):
                winrate += 1

    if(winrate == 0):
        return False
    else:
        return True


def lose():
    temp = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i][j] != 0):
                temp += 1

    if (temp == 16):
        return True
    else:
        return False

def insertsomestuff():
    possible_plots = [2*i for i in range(3)]
    possible_plots.append(1)

    pos = random.randint(1,len(board)) - 1

    ite = random.randint(1, 4)

    for j in range(ite):
        varone = random.randint(1, 4) - 1
        vartwo = random.randint(1, 4) - 1
        plot(varone, vartwo, board, possible_plots[pos])

#Start
insertsomestuff()


#Gameplay
print("HI human, welcome to the 2048 game !")
sleep(1)
print("Here is your starting board :")
sleep(1)
print(numpy.matrix(board))
print("\n")
sleep(1)
print("You can go [L]eft, [R]ight, [U]p, or [D]own")
print("Also you can exit whenever you want by typing [E]xit")
print("Good luck!")
sleep(1)
print("Game is starting.")

while True:
    print(numpy.matrix(board))
    inp = input("Your move: ")

    if(inp == "L" or inp == "left"):
        board = moveXaxis(board, "left")
    elif(inp == "R" or inp == "right"):
        board = moveXaxis(board, "right")
    elif(inp == "U" or inp == "up"):
        board = moveYaxis(board, "up")
    elif(inp == "D" or inp == "down"):
        board = moveYaxis(board, "down")
    elif(inp == "E"):
        print("Ok, bye!")
        break
    else:
        print("Enter valid move !")
        break

    if(win()):
        print("Congratulations you won !")
        break
    elif(lose()):
        print("So sad man you lost :(")
        break

    insertsomestuff()