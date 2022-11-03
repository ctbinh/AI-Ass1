from Util import *
from AStarSearch import *
from genImg import createImg
import imageio
from os import walk

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
        for i in range(len(self.solution.prev_nodes)):
            createImg(self.solution.prev_nodes[i].state, self.tube_size, i)
        self.generate_gif()

    def generate_gif(self):
        filenames = next(walk('./images'), (None, None, []))[2]
        images = []
        for filename in filenames:
            images.append(imageio.imread("./images/" + filename))
        print(filenames)
        imageio.mimsave('./output/out.gif', images, fps = 1)