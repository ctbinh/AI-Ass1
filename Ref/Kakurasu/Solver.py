from ctypes import util
from os import stat
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


    def solve(self, kakurasu):
        pass


class Node:

    def __init__(self, state, row_const, col_const, path):

        self.state = deep_copy(state)
        self.row_const = [number for number in row_const]
        self.col_const = [number for number in col_const]
        self.path = path
        self.size = len(self.row_const)
        if len(self.path) > 0:
            row = self.path[len(self.path) - 1][0]
            col = self.path[len(self.path) - 1][1]
            self.row_const[row] -= (col + 1)
            self.col_const[col] -= (row + 1)
            self.state[row][col] = Constant.SET
        
    def expand_at(self, row, col):
        node = (type(self)) (self.state, self.row_const, self.col_const, self.path + [[row, col]])
        
        return node

    def is_valid_cell(self, row, col):
        if self.state[row][col] == Constant.SET or \
        self.row_const[row] < (col + 1) or self.col_const[col] < (row + 1):
                return False
        return True

    # def is_legal_state(self):
    #     for i in range(0, len(self.row_const)):
    #         if self.row_cons[i] < 0 or self.col_const[i] < 0:
    #             return False

    def is_goal_state(self):
        count = 0
        for i in range(0, self.size):
            
            if self.row_const[i] != 0 or self.col_const[i] != 0:
                return False
            count += 1
        
        return True

    def expand_node(self):
        nodes = []
        for row in range(self.size):
            for col in range(self.size):
                if self.is_valid_cell(row, col):
                    nodes += [self.expand_at(row, col)]

        return nodes

    def generate_steps(self):

        state = create_square_list(Constant.UNSET, self.size)
        res = []

        res += [str_square_list(state, "\n")]

        for pos in self.path:
            state[pos[0]][pos[1]] = Constant.SET
            
            res += [str_square_list(state, "\n")]
        
        return res