from DepthFirstSearch import DepthFirstSearch
from BreadthFirstSearch import BreadthFirstSearch
from AStarSearch import AStarSearch
import Constant
from Util import *

DEFAULT_COLOR = (0, 0, 0)

class Kakurasu(Subscriber):
    
    def __init__(self, row_const, col_const, size):
        self.grid = create_square_list(Constant.UNSET, size)
        self.row_const = row_const
        self.col_const = col_const
        self.size = size
        self.solver = None

    def solve_by_dfs(self):
        self.solver = DepthFirstSearch()
        self.solution = self.solver.solve(self)
    
    def solve_by_bfs(self):
        self.solver = BreadthFirstSearch()
        self.solution = self.solver.solve(self)
        
    def solve_by_a_star(self):
        self.solver = AStarSearch()
        self.solution = self.solver.solve(self)
        

    def generate_steps(self):
        
        res = []

        if self.solution:
            res = self.solution.generate_steps()
        return res

    def update_grid(self, row, col):
        pass
    
    