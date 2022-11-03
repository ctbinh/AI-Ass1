from Util import *
from AStarSearch import *
class WaterSort:
    UNSET = 0
    DOT = 1

    def __init__(self, n_tube, n_tube_empty, tube_size, tube_full):
        self.state = create_list_stack(n_tube, n_tube_empty, tube_full)
        self.n_tube = n_tube
        self.n_tube_empty = n_tube_empty
        self.tube_size = tube_size
        self.solver = None
        self.solution = None
        self.steps = []
    
    def solveByASTAR(self):
        self.solver = AStarSearch()
        self.solution = self.solver.solve(self)
    
    def generate_steps(self):
        res = []
        for i in range(len(self.solution.prev_nodes)):
            step = ''
            for j in range(self.n_tube + self.n_tube_empty):
                step += str(self.solution.prev_nodes[i].state[j]) + "\n"
            res += [step]
        return res