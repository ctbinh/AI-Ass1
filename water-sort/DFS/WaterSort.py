from Util import *
from DFS import *
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
    
    def solveByDFS(self):
        self.solver = DepthFirstSearch()
        self.solution = self.solver.solve(self)
    
    def generate_steps(self):
        res = []
        for i in range(len(self.steps)):
            step = ''
            for j in range(self.n_tube + self.n_tube_empty):
                step += str(self.steps[i].state[j]) + "\n"
            res += [step]
        return res