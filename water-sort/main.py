from Kakurasu import *
import pathlib
import time
import os
import Util

DIR_PATH = str(pathlib.Path(__file__).parent.resolve())


class WriteSolution:

    @staticmethod
    def truncate_file(fileName):
        file = open(fileName,"r+")
        file.truncate(0)
        file.close()

    @staticmethod
    def write(data, fileName):
        WriteSolution.truncate_file(fileName)
        f = open(fileName, "w")
        f.write(data)
        f.close()

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
    input = readFile(os.path.join(DIR_PATH, 'input' ,fileName))
    size = int(input[0][0])

    row_const = [int(number) for number in input[1].split(' ')]
    col_const = [int(number) for number in input[2].split(' ')]

    kakurasu = Kakurasu(row_const, col_const, size)

    kakurasu.solve_by_a_star()
    steps = kakurasu.generate_steps()

    WriteSolution.write(Util.print_steps(steps), os.path.join(DIR_PATH, 'output' ,"output.txt"))

    