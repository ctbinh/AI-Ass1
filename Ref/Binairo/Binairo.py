from DepthFirstSearch import DepthFirstSearch
from BreadthFirstSearch import BreadthFirstSearch
import Constant
from Util import *

DEFAULT_COLOR = (0, 0, 0)

class Binairo(Subscriber):
    
    def __init__(self, grid, size):
        self.grid = grid

    def solve_by_dfs(self):
        self.solver = DepthFirstSearch()
        self.solution = self.solver.solve(self)
        if self.solution:
            print(self.solution.state)
    
    def solve_by_bfs(self):
        self.solver = BreadthFirstSearch()
        self.solution = self.solver.solve(self)
        if self.solution:
            print(self.solution.state)

    def update_grid(self, row, col):
        pass
    
    # check have more than two adjacent cells
    def have_mt_adj_cells(self, grid, row, col):
        
        if grid[row][col] == Constant.UNSET:
            return False

        if row > 1 and grid[row][col] == grid[row -1][col] and \
        grid[row - 2][col] == grid[row][col] :
            return True
        
        if col > 1 and grid[row][col] == grid[row][col - 1] and \
        grid[row][col - 2] == grid[row][col] :
            return True

        return False

    def check_redundant_cell(self, grid, row, col):
        row_count = [0, 0]
        col_count = [0, 0]
        size = len(grid)
        for i in range(size):
            if grid[row][i] == Constant.BLACK:
                row_count[0] += 1
            elif grid[row][i] == Constant.WHITE:
                row_count[1] += 1
            if grid[i][col] == Constant.BLACK:
                col_count[0] += 1
            elif  grid[i][col] == Constant.WHITE:
                col_count[1] += 1
        limit = size // 2
        return row_count[0] > limit or row_count[1] > limit \
            or col_count[0] > limit or col_count[1] > limit

    def is_legal_state(self, grid):

        for row in range(len(grid)):
            for col in range(len(grid)):
                if self.have_mt_adj_cells(grid, row, col) or self.check_redundant_cell(grid, row, col):
                    return False

        return True

    
    def is_goal_state(self, grid):

        # count number of black cell and whitecell
        row_count = []
        col_count = []
        size = len(grid)
        for i in range(size):
            row_count += [[0, 0]] # (black, white)
            col_count += [[0, 0]]
        
        for row in range(size):
            for col in range(size):
                if grid[row][col] == Constant.BLACK:
                    row_count[row][0] += 1
                    col_count[col][0] += 1
                elif grid[row][col] == Constant.WHITE:
                    row_count[row][1] += 1
                    col_count[col][1] += 1


        for i in range(size):
            if row_count[i][0] != (size // 2) or row_count[i][0] != row_count[i][1]:
                return False
            if col_count[i][0] != (size // 2) or col_count[i][0] != col_count[i][1]:
                return False

        return True
    