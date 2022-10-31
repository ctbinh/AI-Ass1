from Util import *
from DFS import *
class Kakurasu:
    UNSET = 0
    DOT = 1

    def __init__(self, row_const, col_const, size):
        self.state = create_matrix(0, size)
        self.row_const = row_const
        self.col_const = col_const
        self.size = size
        self.solver = None
        self.solution = None
    
    def solveByDFS(self):
        self.solver = DepthFirstSearch()
        self.solution = self.solver.solve(self)
    
    def generate_steps(self):
        res = []
        if self.solution:
            res = self.solution.generate_steps()
        return res