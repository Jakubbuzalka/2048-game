import numpy
import random
import sys
import os
sys.path.append(os.path.abspath("D:\\Miacik\\Projects\\2048-game\\lib"))
from sanitize import *
from helper import *
from movement import moveXaxis

#variables
board = [
    [1,0,2,1],
    [0,4,5,4],
    [1,2,6,0],
    [1,2,5,4]
]


print(numpy.matrix(moveXaxis(board)))