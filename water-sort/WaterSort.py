from Util import *
from AStarSearch import *
from DFS import *
from genImg import createImg
import imageio
import os

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
        return self.solution
    
    def solveByDFS(self):
        self.solver = DepthFirstSearch()
        self.solution = self.solver.solve(self)
        return self.solution
    
    def generate_steps(self, index):
        dir = './images'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        for i in range(len(self.solution.prev_nodes)):
            createImg(self.solution.prev_nodes[i].state, self.tube_size, i, len(self.solution.prev_nodes))
        step = self.generate_gif(index)
        return step

    def generate_gif(self, index):
        filenames = next(os.walk('./images'), (None, None, []))[2]
        images = []
        for filename in filenames:
            images.append(imageio.imread("./images/" + filename))
        imageio.mimsave('./output-gif/output-' + str(index) + '.gif', images, fps = 2)
        return len(filenames)