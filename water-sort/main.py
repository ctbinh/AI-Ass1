from Util import *
import os
import pathlib
from WaterSort import *
import time
import psutil
import sys

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
    
def runtest(fileName, index, type):
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
    solution = None
    if(type == 'DFS'):
        solution = watersort.solveByDFS()
    elif(type == "A*"):
        solution = watersort.solveByASTAR()
    else:
        return None
    end = time.time()
    result = ''
    result += "Memory: " + str(process.memory_info().rss) + '\n'
    if(not solution):
        result = "Cannot solve!!!"
        return result
    steps = watersort.generate_steps(index)

    result += "WATERSORT solve by DFS:\n"
    result += "Time: " + str(end - start) + '\n'
    result += "Steps:" + str(steps) + '\n'
    return result

def main(argv):
    filenames = next(os.walk('./input'), (None, None, []))[2]
    for i in range(len(filenames)):
        result = runtest(filenames[i], i, argv[0])
        if(not result):
            print("DFS or A*")
            return
        file = open("./output/output-" + str(i) + ".txt", 'w+')
        CreateOutput.write(result, os.path.join(DIR_PATH, 'output' ,"output-" + str(i) + ".txt"))
if __name__ == '__main__':
    main(sys.argv[1:])