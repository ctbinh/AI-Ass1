from Util import *
import os
import pathlib
from WaterSort import *
import time
import psutil

DIR_PATH = str(pathlib.Path(__file__).parent.resolve())

def readFile(fileName):
    scanner = open(fileName, "r")
    lines = scanner.read().splitlines()
    for i in range(len(lines)):
        lines[i] = lines[i].split(' ')
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
    fileName = "input-00.txt"
    process = psutil.Process(os.getpid())
    input = readFile(os.path.join(DIR_PATH, 'input' ,fileName))
    n_tube = int(input[0][0])
    n_tube_empty = int(input[0][1])
    tube_size = int(input[0][2])
    tube_full = []
    for i in range(n_tube):
        tube = Stack()
        for j in range(tube_size):
            tube.push(int(input[i + 1][j]))
        tube_full += [tube]

    watersort = WaterSort(n_tube, n_tube_empty, tube_size, tube_full)
    
    start= time.time()
    watersort.solveByASTAR()
    end = time.time()
    print(process.memory_info().rss)
    
    steps = watersort.generate_steps()
    print("WATERSORT solve by DFS:")
    print("Time: ",end - start)
    print("Steps:",len(steps))
    print("Solution:")
    print(steps[len(steps) - 1])
    
    CreateOutput.write(print_steps(steps), os.path.join(DIR_PATH, 'output' ,"output.txt"))