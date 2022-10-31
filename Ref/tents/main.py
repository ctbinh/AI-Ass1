from Tents import *
from SearchAlgo import *
from HeuristicSearch import HeuristicSearch
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
    n = int(input[0][0])
    
    grid = functools.reduce(lambda res, cur: res + 
    [[int(i) for i in cur.split(' ')]]
    , input[1:], [])
    
    forest = grid[0 : n]
    row_const = grid[n]
    col_const = grid[n + 1]
    
    tents = Tents(forest, row_const, col_const, n)

    # dfs = DepthFirstSearch()
    a_star = AStarSearch()
    bfs = BreadthFirstSearch()


    

    start = time.time()
    solution = a_star.let_me_solve(tents)
    end = time.time()
    print("Time: ",end - start)
    
    print("Solution: ",solution)

    # start = time.time()
    # solution = bfs.let_me_solve(tents)
    # end = time.time()
    # print("Time: ",end - start)
    
    # print("Solution: ",solution)

    # visited = []
    
    # for state in a_star.visited:
    #     visited += [tents.get_all_icon(state)]
        

    # game_manager = GameManager.GameManager(tents.title,tents.get_all_icon(tents.state), visited)
    
    # game_manager.display_all_data()