from Binairo import *
import pathlib
import time
# importing functools for reduce()
import functools

DIR_PATH = str(pathlib.Path(__file__).parent.resolve()) + '\\'


def readFile(fileName):
    scanner = open(fileName,"r")
    lines = scanner.read().splitlines()
    return lines

if __name__ == '__main__':

    """
    Input format:
    n: first line of input, represent size of grid
    Each of the next line describes a row in grid
    """

    fileName = "input.txt"
    input = readFile(DIR_PATH + fileName)
    size = int(input[0][0])
    
    grid = functools.reduce(lambda res, cur: res + 
    [[int(i) for i in cur.split(' ')]]
    , input[1:], [])

    binairo = Binairo(grid, size)

    binairo.solve_by_dfs()()
    