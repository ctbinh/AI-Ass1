from Util import *
import os
import pathlib
from WaterSort import *
import time
import psutil
import sys
import func_timeout

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
    
def runFunction(f, max_wait, default_value):
    try:
        return func_timeout.func_timeout(max_wait, f)
    except func_timeout.FunctionTimedOut:
        pass
    return default_value

def runtest(fileName, index, type, is_gen_gif, is_gen_both):
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
        solution = runFunction(watersort.solveByDFS, 30, "Timeout 30s!!!")
    elif(type == "A*"):
        solution = runFunction(watersort.solveByASTAR, 30, "Timeout 30s!!!")
    else:
        return None
    end = time.time()
    result = ''
    result += "Memory: " + str(process.memory_info().rss) + '\n'
    if(not solution):
        result = "Cannot solve!!!"
        return result
    if(isinstance(solution, str)):
        return 'Timeout 30s!!!'
    steps = 0
    if(is_gen_gif):
        steps = watersort.generate_steps_gif(index)
        result = 'gif'
    elif(is_gen_both):
        steps = watersort.generate_steps_gif(index)
        steps = watersort.generate_steps()

        result += "WATERSORT solve by " + type + ': \n'
        result += "Time: " + str(end - start) + '\n'
        result += "Steps: " + str(len(steps)) + '\n'
        result += "Solution: \n" + str(print_steps(steps)) + '\n'
    else:
        steps = watersort.generate_steps()

        result += "WATERSORT solve by " + type + ': \n'
        result += "Time: " + str(end - start) + '\n'
        result += "Steps: " + str(len(steps)) + '\n'
        result += "Solution: \n" + str(print_steps(steps)) + '\n'
    return result

def main(argv):
    if(len(argv)==0):
        print("Chỉ xuất output dạng .txt:\n\tpython main.py DFS\n\tor\n\tpython main.py A*\n")
        print("Chỉ xuất output dạng .gif:\n\tpython main.py DFS gif\n\tor\n\tpython main.py A* gif\n")
        print("Xuất cả 2 dạng .txt và .gif:\n\tpython main.py DFS both\n\tor\n\tpython main.py A* both\n")
        return
    filenames = next(os.walk('./input'), (None, None, []))[2]
    for i in range(len(filenames)):
        is_gen_gif = False
        is_gen_both = False
        if(len(argv)==2 and argv[1] == 'gif'):
            is_gen_gif = True
        elif(len(argv)==2 and argv[1] == 'both'):
            is_gen_both = True
        result = runtest(filenames[i], i, argv[0], is_gen_gif, is_gen_both)
        if(not result):
            print("Chỉ xuất output dạng .txt:\n\tpython main.py DFS\n\tor\n\tpython main.py A*\n")
            print("Chỉ xuất output dạng .gif:\n\tpython main.py DFS gif\n\tor\n\tpython main.py A* gif\n")
            print("Xuất cả 2 dạng .txt và .gif:\n\tpython main.py DFS both\n\tor\n\tpython main.py A* both\n")
            return
        if(result != 'gif'):
            open("./output/output-" + str(i) + ".txt", 'w+')
            CreateOutput.write(result, os.path.join(DIR_PATH, 'output' ,"output-" + str(i) + ".txt"))
if __name__ == '__main__':
    main(sys.argv[1:])