from Util import *
import os
import pathlib
from Kakurasu import *
import time

DIR_PATH = str(pathlib.Path(__file__).parent.resolve())

def readFile(fileName):
    scanner = open(fileName, "r")
    lines = scanner.read().splitlines()
    return lines

class CreateOutput:

    @staticmethod
    def truncate_file(fileName):
        file = open(fileName,"r+")
        file.truncate(0)
        file.close()

    @staticmethod
    def write(data, fileName):
        CreateOutput.truncate_file(fileName)
        f = open(fileName, "w")
        f.write(data)
        f.close()
    
if __name__ == '__main__':
    fileName = "input.txt"
    input = readFile(os.path.join(DIR_PATH, 'input' ,fileName))
    size = int(input[0][0])
    row = []
    col = []
    for i in range(size):
        row.insert(i, int(input[i + 1]))
    for i in range(size):
        col.insert(i + size, int(input[i + size + 1]))
    kaku = Kakurasu(row, col, size)
    
    start= time.time()
    kaku.solveByDFS()
    end = time.time()
    
    steps = kaku.generate_steps()
    print("KAKURASU solve by DFS:")
    print("Time: ",end - start)
    print("Solution:")
    print(steps[len(steps) - 1])
    
    CreateOutput.write(print_steps(steps), os.path.join(DIR_PATH, 'output' ,"output.txt"))