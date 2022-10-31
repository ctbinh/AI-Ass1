import Constant
from Util import *

class Solver:
    
    # def __init__(self, grid, size):
    #     # self.subscribers = []
    #     self.grid = grid
    #     self.size = size
    
    # def send_data(self, data):

    #     for subscriber in self.subscribers:
    #         subscriber.receive_data(data)
    
    # def add_subcriber(self, new_subcriber):
    #     self.subscribers += [new_subcriber]


    def solve(self):
        pass


class Node:

    def __init__(self, state, position, path):
        self.position = position
        self.path = path
        self.state = deep_copy(state)
        self.size = len(state)

    def set_value_at_pos(self, value):
        self.state[self.position[0]][self.position[1]] = value

    def expand_node(self):

        nodes = []

        for row in range(self.size):
            for col in range(self.size):
                # find first unset cell
                if self.state[row][col] == Constant.UNSET:
                    
                    white_node = Node(self.state, [row, col], self.path + [[row, col]])
                    white_node.set_value_at_pos(Constant.WHITE)
                    nodes += [white_node]
                    black_node = Node(self.state, [row, col], self.path + [[row, col]])
                    black_node.set_value_at_pos(Constant.BLACK)
                    nodes += [black_node]
                    break

        return nodes
    
    
